

import socket
import termcolor

def banner():
	print(" ____            _       ____                                  ")
	print("|  _ \ ___  _ __| |_    / ___|  ___ __ _ _ __  _ __   ___ _ __ ")
	print("| |_) / _ \| '__| __|___\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|")
	print("|  __/ (_) | |  | ||_____|__) | (_| (_| | | | | | | |  __/ |   ")
	print("|_|   \___/|_|   \__|   |____/ \___\__,_|_| |_|_| |_|\___|_|   ")

	print("____Coded by PRATEEK____")

banner()

def scan(target, ports):
	print('\n' + ' Starting Scan For ' + str(target))
	for port in range(1,ports):
		scan_port(target,port)


def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print("[+] Port Opened " + str(port))
		sock.close()
	except:
		pass


targets = input("[*] Enter Targets To Scan(split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
if ',' in targets:
	print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets,ports)
