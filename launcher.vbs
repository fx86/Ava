Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c main_engine.bat"
oShell.Run strArgs, 0, false