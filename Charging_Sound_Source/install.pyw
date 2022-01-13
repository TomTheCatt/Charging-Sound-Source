import os, time
import xml.etree.ElementTree as ET
import win32com.shell.shell as shell
from main import main_name, main_direc, main_ext

#Modifies .xml file for user.
tree = ET.parse('Format.xml')
tree.find('.//{http://schemas.microsoft.com/windows/2004/02/mit/task}Command').text = f"{main_direc}\\{main_name}{main_ext}"
tree.find('.//{http://schemas.microsoft.com/windows/2004/02/mit/task}Arguments').text = f"/c python {main_direc}\\{main_name}{main_ext}"
tree.find('.//{http://schemas.microsoft.com/windows/2004/02/mit/task}WorkingDirectory').text = f"{main_direc}"
ET.register_namespace("", "http://schemas.microsoft.com/windows/2004/02/mit/task")
tree.write("Format.xml")

#Creates task via system terminal.
commanda, commandb = f'schtasks /Create /XML {os.getcwd()}\\Format.xml /TN Charging_Sound /RU "NT AUTHORITY\SYSTEM"', "schtasks /Run /TN Charging_Sound"
shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commanda)
time.sleep(1)
shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commandb)
