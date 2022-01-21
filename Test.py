
OUInput = "Test1"
ShareInput = "Test2"
PSScript = "PowerShell -ExecutionPolicy ByPass -NoProfile -File .\ADAPT.ps1 -Command" + " " + '"& {Start-Process PowerShell' + " " + "-ArgumentList'" + " " + '-File .\ADAPT.ps1' + " " + OUInput + " " + ShareInput + " " + " -Verb RunAs}"
print(PSScript)