import os
import webbrowser
from requests import get
import pyautogui


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


def flood_attack(ip):
    try:
        os.system(f"ping -t -l 65500 {ip}")
    except:
        print("Invalid ip")


def shutdown(mode="s"):
    try:
        os.system(f"shutdown /{mode}")
    except:
        print("Invalid shutdown mode")


def get_wifi_connnections():
    os.system("netsh wlan show profiles")


def get_wifi_pass(wifi_name):
    try:
        os.system(f"netsh wlan show profile {wifi_name} key=clear")
    except:
        print("Please provide a wifi name as an argument.")


def systeminfo():
    try:
        os.system("systeminfo")
    except:
        print("Error getting system info.")


def open_url(url):
    try:
        webbrowser.get('windows-default').open("http://"+url)
    except:
        print("Error opening \"{url}\"")


def get_hostname():
    os.system("hostname")


def spam(string):
    print("Spam will start in 5 seconds")
    time.sleep(5)
    print("Spam started, move cursor to the corner of the screen to stop.")
    while True:
        pyautogui.type(string)
        pyautogui.press("enter")
# by kar1m hany
