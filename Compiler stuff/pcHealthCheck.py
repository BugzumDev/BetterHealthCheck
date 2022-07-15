# Making PC health check better: 
# A program/video made by BugzumDev

# Notes:
# PC health check window size: 897x896

# Libraries
import eel
import os
import subprocess
from tkinter import messagebox
from pathlib import Path

ogloc = os.path.abspath(__file__).replace(Path(__file__).name, "")
os.chdir(ogloc)

eel.init("gui")
# Value get
@eel.expose
def getValue_computername():
    return os.environ["computername"]

@eel.expose
def getValue_username():
    return os.environ["username"]

@eel.expose
def scan_suggestions():
    memoryusage = subprocess.Popen('wmic diskdrive get status', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    if "fail" in memoryusage:
        suggestion = "Fix drive issues"
    else:
        suggestion = "No suggestions"
    return suggestion

# Health check functions
@eel.expose
def checkdisk():
    startCheck = messagebox.askokcancel("PC health check | CheckDisk", "Do you want to start CheckDisk?\nThis can take a long time.")
    if startCheck:
        memoryusage = subprocess.Popen('CHKDSK /F', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
        showLog = messagebox.askyesno("PC health check | CheckDisk", "CheckDisk repair success! \n Do you want to see the scan log?")
        if showLog:
            with open("checkdisk.log", "w") as f:
                f.write(memoryusage)
                f.close()
            os.system("notepad checkdisk.log")
        else:
            pass
    else:
        messagebox.showerror("PC health check | CheckDisk", "CheckDisk repair failed!\nOperation cancelled!")

@eel.expose
def sfcscanner():
    startCheck = messagebox.askokcancel("PC health check | CorruptCheck", "Do you want to start CorruptCheck?\nThis can take a long time.")
    if startCheck:
        cclog = subprocess.Popen('sfc /scannow', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
        showLog = messagebox.askyesno("PC health check | CorruptCheck", "CorruptCheck done! \n Do you want to see the scan log?")
        if showLog:
            with open("corruptcheck.log", "w") as f:
                f.write(cclog)
                f.close()
            os.system("notepad corruptcheck.log")
        else:
            pass
    else:
        messagebox.showerror("PC health check | CorruptCheck", "Scanning for corrupt OS files failed!\nOperation cancelled!")

# Automatic stuff here

eel.start("index.html")