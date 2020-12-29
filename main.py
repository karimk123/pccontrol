import os
from requests import get


def get_ip():
	ip = get('https://api.ipify.org').text
	if ip == None or '':
		print("ERORR getting IP.")
	else:
		return ip
def get_users():
	os.system("net user")

def change_pass(user, new_pass):
	try:
		os.system(f"net user {user}")
		os.system(f"{new_pass}")
	except:
		print("please provide the user and new pass")

def task_manager():
	os.system("tasklist")

def arp():
	os.system("arp -a")

def get_active_connections():
	os.system("netstat")

def cmd_history():
	os.system("doskey/history")

def get_mac_adress():
	os.system("getmac")
