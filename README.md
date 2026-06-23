# hookspy 

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

idk i just wanted to see how webhooks can be used to exfiltrate data. basic python script that sends outputs from commands to a webhook.
wip so no proper readme for now lol

### ⚠️ DISCLAIMER / WARNING
**THIS IS A PURELY EDUCATIONAL PROOF OF CONCEPT.** It's made just to demonstrate how webhooks can be abused in spyware contexts. Don't use this for malicious stuff. I am not responsible for any damage caused by this code.

### features (or whatever)
- sends login info on startup
- pseudo interactive shell (with working `cd` kinda)
- gets system info using `fastfetch`
- takes screenshot (`scrot`) and sends it over
- logs clipboard content
- grabs network info & external ip
- grabs .bashrc file

### how to use
1. open the script
2. replace `WEBHOOK = "webhook"` with your actual Discord/Slack/whatever webhook URL
3. install dependencies: `pip install requests pyperclip`
4. run it: `python main.py` (or whatever you named it)
5. select options from the menu

### todo / bugs
- `cd` is buggy sometimes
- only works nicely on linux because of `scrot`, `ifconfig`, `fastfetch` etc.
- messy code, might clean later lol

## license
mit
