from textwrap import wrap
import tkinter as TK
import subprocess, sys, os
from tkinter.scrolledtext import *

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


Output = ScrolledText(frame, height='10', width='45', wrap="word")

# OUInput = OU.get(1.0, 'end-1c')
# ShareInput = SharePath.get(1.0, 'end-1c')
# PSScript = "PowerShell -ExecutionPolicy ByPass -NoProfile -File .\ADAPT.ps1 -Command" + " " + '"& {Start-Process PowerShell' + " " + "-ArgumentList'" + " " + '-File .\ADAPT.ps1' + " " + OUInput + " " + ShareInput + " " + " -Verb RunAs}"

def runscript():
    try:
        OUInput = OU.get(1.0, 'end-1c')
        ShareInput = SharePath.get(1.0, 'end-1c')
        PSScript = "PowerShell -ExecutionPolicy ByPass -NoProfile -File .\ADAPT.ps1 -Command" + " " + '"& {Start-Process PowerShell' + " " + "-ArgumentList'" + ' ' + '-File .\ADAPT.ps1' + ' "' + OUInput + '" "' + ShareInput + '" ' + " -Verb RunAs}"
        Output.insert(TK.INSERT,PSScript)
        stdout = os.popen(PSScript)
        stdout
        Output.insert(TK.INSERT, stdout)


    except subprocess.CalledProcessError as e:
        error = "command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output)
        Output.config(text=error)
        raise RuntimeError(error)

def printcommand():
    OUInput = OU.get(1.0, 'end-1c')
    ShareInput = SharePath.get(1.0, 'end-1c')
    PSScript = "PowerShell -ExecutionPolicy ByPass -NoProfile -File .\ADAPT.ps1 -Command" + " " + '"& {Start-Process PowerShell' + " " + "-ArgumentList'" + " " + '-File .\ADAPT.ps1' + " " + OUInput + " " + ShareInput + " " + " -Verb RunAs}"
    Output.insert(TK.INSERT, PSScript)
    print(OUInput)
    print(ShareInput)


submitButton =TK.Button(frame,
                        text = "Submit",
                        command = runscript)

OUlbl.pack()
OU.pack()
SharePathlbl.pack()
SharePath.pack()
submitButton.pack()
Output.pack()
frame.mainloop()