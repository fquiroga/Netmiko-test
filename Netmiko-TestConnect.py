#!/usr/bin/env python
from __future__ import print_function
from netmiko import ConnectHandler
from getpass import getpass
import json
import os
import sys
import time
 
# Define el log y formato 
timestr = time.strftime("%Y%m%d_%H%M%S")
outputfile = timestr + '-output.log'
 
# Define the login info
device = {
    'device_type': 'cisco',
    'host': '192.168.1.1',
    'username': 'fquiroga',
    'password': 'password',
} 
 
# ConnectHandler using device Tuple 
net_connect = ConnectHandler(**device)
 
# open logfile 
log = open(outputfile,'a')
 
# abrir la lista de comandos 
# y hace loop hasta la ultima linea 
# pass commands to send_command method as arg
commands = open('commands.txt')
for line in commands:
    output = net_connect.send_command(line, strip_command=False)
    print(output, file=log) 
    print("*"*64, file=log) 
    print(" ", file=log)
commands.close()
 
# print the file end notice
print("\n"*3, file=log)
print("#"*42, file=log)
print("###!ThIS IS THE END OF DATA COLLECTION!###", file=log)
print("#"*42, file=log)
