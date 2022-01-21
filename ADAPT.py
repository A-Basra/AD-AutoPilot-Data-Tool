from textwrap import wrap
import tkinter as TK
import subprocess, sys
from tkinter.scrolledtext import *
from turtle import ScrolledCanvas

frame = TK.Tk()
frame.title("AD AutoPilot Tool")
frame.geometry('500x500')

OUlbl = TK.Label(frame, text="OU Path", anchor= "w", pady=5)
OU = TK.Text(frame,
                    height= 1,
                    width = 50,)

SharePathlbl = TK.Label(frame, text="Share Path", anchor= "w", pady=5)
SharePath = TK.Text(frame,
                    height= 1,
                    width = 50,)


def getInput(txt):
    inp =txt.get(1.0, 'end-1c')
    return inp

OUInput = getInput(OU)
ShareInput = getInput(SharePath)

PSScript = "PowerShell -ExecutionPolicy ByPass -NoProfile -File .\ADAPT.ps1 -Command" + " " + '"& {Start-Process PowerShell' + " " + "-ArgumentList'" + " " + '-File .\ADAPT.ps1' + " " + OUInput + " " + ShareInput + " " + " -Verb RunAs}"

def runscript():
    output = subprocess.check_output(["powershell", PSScript])
    Output.config(text="ouput")


submitButton =TK.Button(frame,
                        text = "Submit",
                        command = runscript())

Output = ScrolledText(frame, height='10', width='45', wrap="word", text="")

OUlbl.pack()
OU.pack()
SharePathlbl.pack()
SharePath.pack()
submitButton.pack()
Output.pack()
frame.mainloop()