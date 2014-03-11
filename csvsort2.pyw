#THIS IS PYTHON 3.X  !!!!

from tkinter import *
from tkinter import filedialog
import csv
import datetime

class Sortcsv(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.inpvar = StringVar()
        self.outvar = StringVar()
        self.mailrow = StringVar()
        self.initUI()

    def initUI(self):

        self.parent.title("CSV Success Compiler")
        #Frames for alignment
        leftside = Frame(self.parent)
        #WIDGET SETS
        self.openbut = Button(leftside, text='CSV input', command=self.onOpen)
        openmsg = Message(leftside, textvariable=self.inpvar, width=440)
        openlab = Label(leftside, text="Current Input:")

        emaillab = Label(leftside, text="Which row is Email on?")
        emailsel = Entry(leftside, textvariable=self.mailrow, width=6)

        startbut = Button(self.parent, text='CREATE', command=self.start)
        #WIDGET PACKS
        leftside.pack(side=TOP)

        openlab.pack(side=TOP)
        openmsg.pack(side=TOP)
        self.openbut.pack(side=TOP)
        emaillab.pack(side=RIGHT)
        emailsel.pack(side=RIGHT)

        startbut.pack(side=BOTTOM)

    def onOpen(self):
        ftypes = [('CSV Files', '*.csv')]
        opening = filedialog.askopenfilename(filetypes = ftypes)

        if opening != '':
            self.inpvar.set(opening)
            self.openInp()
            outchange = opening
            new = outchange.split('/')
            new.remove(new[-1])
            new.append(str(datetime.date.today()) + 'success.csv')
            new2 = '/'.join(new)
            self.outvar.set(new2)
            self.openbut.pack_forget()

    def openInp(self):
        rightside = Frame(self.parent)
        outmsg = Message(rightside, textvariable=self.outvar, width=440)
        outent = Entry(rightside, textvariable=self.outvar, width=60)
        outlab = Label(rightside, text="Desired Output:")

        rightside.pack(side=BOTTOM)
        outlab.pack(side=TOP)
        outmsg.pack(side=TOP)
        outent.pack(side=TOP)

    def start(self):
        rownum = int(self.mailrow.get()) - 1
        emails = []
        with open(self.inpvar.get(), 'r') as csvfile, open(self.outvar.get(), 'w') as csvwrite:
            readvar = csv.reader(csvfile, delimiter=',', quotechar='"')
            writevar = csv.writer(csvwrite, delimiter='\n', quotechar='"')
            for row in readvar:
                if row[0] == 'd':
                    #print(row[rownum])
                    emails.append(row[rownum])
                else:
                    pass
            writevar.writerow(emails)
            self.finished()

    def finished(self):
        finishtext = Label(self.parent, text="Finshed!", fg='#00B837')
        finishtext.pack(side=BOTTOM)

    def onExit(self):
        self.quit()

def main():

    root = Tk()
    app = Sortcsv(root)
    root.geometry("400x200+300+300")
    root.mainloop()

if __name__ == '__main__':
    main()
