import os, time
import win32com.shell.shell as shell

commanda, commandb = "schtasks /End /TN Charging_Sound", "schtasks /Delete /TN Charging_Sound /F"

shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commanda)
time.sleep(1)
shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commandb)
