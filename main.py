# -*- coding: utf-8 -*-
# Author: Furkan CALISKAN, 2017
import wmi
c = wmi.WMI("HOSTNAME",user="HOSTNAMEORDOMAINNAME\USER",password="PASSWORD")
print "\n\nOperating System"
print "--------------------------------"
for os in c.Win32_OperatingSystem():
  print os.Caption
  
print "\n\nStartup Items"
print "--------------------------------"
for s in c.Win32_StartupCommand():
  print "[%s] %s <%s>" % (s.Location, s.Caption, s.Command)

print "\n\nNetwork shares"
print "------------------------"

for share in c.Win32_Share():
  print share.Name, share.Path

print "\n\nRunning processes"
print "---------------------"

for process in c.Win32_Process():
  print process.ProcessId, process.Name
