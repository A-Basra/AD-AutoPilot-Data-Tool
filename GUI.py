import tkinter as TK
import subprocess, sys

frame = TK.Tk()
frame.title("Gather AutoPilot Data AD")
frame.geometry('400x600')

OUlbl = TK.Label(frame, text="OU Path", anchor= "w", pady=5)
OU = TK.Text(frame,
                    height= 1,
                    width = 20,)

Usernamelbl = TK.Label(frame, text="Username", anchor= "w", pady=5)
Username = TK.Text(frame,
                    height= 1,
                    width = 20,)

Passwordlbl = TK.Label(frame, text="Password", anchor= "w", pady=5)
Password = TK.Text(frame,
                    height= 1,
                    width = 20,)

SharePathlbl = TK.Label(frame, text="Share Path", anchor= "w", pady=5)
SharePath = TK.Text(frame,
                    height= 1,
                    width = 20,)

Filelbl = TK.Label(frame, text="File Path", anchor= "w", pady=5)
File = TK.Text(frame,
                    height= 1,
                    width = 20)

def getInput(txt):
    inp =txt.get(1.0, 'end-1c')

def runscript(self, cmd):
    p = subprocess.check_output(["powershell.exe", ""])

submitButton =TK.Button(frame,
                        text = "Submit",
                        command = getInput)



OUlbl.pack()
OU.pack()
Usernamelbl.pack()
Username.pack()
Passwordlbl.pack()
Password.pack()
SharePathlbl.pack()
SharePath.pack()
Filelbl.pack()
File.pack()
submitButton.pack()
frame.mainloop()