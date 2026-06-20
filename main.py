import os
import requests

WEBHOOK = "" #put your here
cwd = os.getcwd()
while True:
    print(f"""
    1 - Shell
    2 - System Info
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
                    print("cd error")
                continue
            out = os.popen(cmd).read()
            print(out)
            requests.post(WEBHOOK, data={"content": f"```[{cwd}]> {cmd}```"})
            requests.post(WEBHOOK, data={"content": f"```{out}```"})
    elif uput == "2":
        out = os.popen("fastfetch --logo none --pipe").read()
        requests.post(WEBHOOK, data={"content": f"```{out}```"})
