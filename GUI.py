from ast import Continue
import tkinter as TK
import subprocess, sys

frame = TK.Tk()
frame.title("Gather AutoPilot Data AD")
frame.geometry('400x200')

OUlbl = TK.Label(frame, text="OU Path", anchor= "w", pady=5)
OU = TK.Text(frame,
                    height= 1,
                    width = 20,)

SharePathlbl = TK.Label(frame, text="Share Path", anchor= "w", pady=5)
SharePath = TK.Text(frame,
                    height= 1,
                    width = 20,)


def getInput(txt):
    inp =txt.get(1.0, 'end-1c')
    return inp

OUInput = getInput(OU)
ShareInput = getInput(SharePath)

def runscript():
    Continue


submitButton =TK.Button(frame,
                        text = "Submit",
                        command = runscript())



OUlbl.pack()
OU.pack()
SharePathlbl.pack()
SharePath.pack()
submitButton.pack()
frame.mainloop()