import os
import sys
import subprocess
from subprocess import *

# Text file with a list of Wifis to chech. 
# One Per Line
sWifiListFilename = "WiFilist.txt"
SSIDs = open(sWifiListFilename,'r').read().split()
sMethod = 'NETSH'
print SSIDs


def main():
        RefreshLists()
        CurrentID = GetCurrentID()
        print "Currently connected to " + CurrentID
        StrongSignalID = GetStrongSignal(SSIDs)
        
        print "Strong signal coming from " + StrongSignalID
        if StrongSignalID and CurrentID != StrongSignalID:
            print "Connecting to " + StrongSignalID
            ConnectTo(StrongSignalID)
def RefreshLists():
    if sMethod == 'NETSH':
        RefreshListsNETSH()

def GetCurrentID():
    if sMethod == 'NETSH':
        return GetCurrentIDNETSH()
def ConnectTo(SSID):
    if sMethod == 'NETSH':
        return ConnectToNETSH(SSID)
def GetStrongSignal(SSID):
    if sMethod == 'NETSH':
        return GetStrongSignalNETSH(SSID)
    
    rongSignalNETSH()
def RefreshListsNETSH():
    sCommand = "netsh wlan refresh".split()
    SUInfo = subprocess.STARTUPINFO()
    SUInfo.dwFlags = subprocess.STARTF_USESHOWWINDOW
    SUInfo.sShowWindow = SW_HIDE
    Popen(sCommand,startupinfo=SUInfo)
def GetCurrentIDNETSH():
    sCommand = ["netsh", "wlan", "show", "interfaces"]
    SUInfo = subprocess.STARTUPINFO()
    SUInfo.dwFlags = subprocess.STARTF_USESHOWWINDOW
    SUInfo.sShowWindow = SW_HIDE
    netshcmd = Popen(sCommand,startupinfo=SUInfo,stdout=PIPE)
    for line in netshcmd.stdout:
        if line.strip():
            if "SSID" == line.split()[0]:
                return line.split()[-1]
def ConnectToNETSH(SSID):
    sCommand = ["netsh","wlan","Connect",SSID]
    SUInfo = subprocess.STARTUPINFO()
    SUInfo.dwFlags = subprocess.STARTF_USESHOWWINDOW
    SUInfo.sShowWindow = SW_HIDE
    Popen(sCommand,startupinfo=SUInfo)
def GetStrongSignalNETSH(SSIDs):
    sNetSHCMD=["netsh", "wlan", "show", "all"]
    SUInfo = subprocess.STARTUPINFO()
    SUInfo.dwFlags = subprocess.STARTF_USESHOWWINDOW
    SUInfo.sShowWindow = SW_HIDE
    Sig=[0,0]
    netsh = Popen(sNetSHCMD,startupinfo=SUInfo,stdout=PIPE)
    Strongest = 0
    stdoutiter=netsh.stdout.__iter__()
    for line in stdoutiter:
        # print line
        for SSID in SSIDs:
                if line.split():
                    if len(line.split()) > 3 and "SSID" in line and not("name" in line) and line.split()[-1] == SSID:
                        line = stdoutiter.next()
                        line = stdoutiter.next()
                        line = stdoutiter.next()
                        line = stdoutiter.next()
                        line = stdoutiter.next()
                        CurSig = line.split()[-1][:-1].strip()

                        if int(CurSig) > int(Strongest):
                            #print SSID
                            Strongest = CurSig
                            SID = SSID
                       # print SSID + " Has a Strength of " + CurSig
                        

                        
    netsh=""
    return SID                    
                        
if __name__ == "__main__":
    main()
