import socket
from pynput import keyboard

#Defining socket object
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
c.connect(('127.0.0.1', 1234))

print("You must begin by setting a speed value")
print("Press 'ESC' at any time to stop the program")

#This function listens to what keys are pressed and sends them all to the server
def on_press(key):
    try:
        c.send(bytes(format(key.char),"utf-8"))          
    except AttributeError:
        if key == keyboard.Key.esc:
            print("Aborted")
            c.close()
            listener.stop()

# Collect events until released
with keyboard.Listener(
        on_press=on_press,) as listener:
    listener.join()