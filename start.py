import os
import sys
import socket

os.system("clear")













#url
target = raw_input("Enter Target website: ")
print "*********************"
print "* IP: " + socket.gethostbyname(target) + " *"
print "*********************"
socket.gethostbyname(target)



raw_input("\n\n\nPress Enter to Start")
#config
os.system("python th.py -t " + target +  " -r 999999")


