import socket
from pynput import keyboard

#Defining socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(('127.0.0.1', 1234))
s.listen(10) 

#Connection to the server
s, address = s.accept()
print(f"Connection from {address} has been established")

speed_inputs = ['0','1','2','3','4','5']

#Within the loop, all inputs from the client are received. The program then compares the input to the array above
#and checks whether or not it matches. If it matches, the message is set as a speed input, otherwise it will check
#to see if the input matches any valid inputs (wasd). If it is (wasd) then the server will output an instruction
while True:
    c_msg = s.recv(1024).decode()
    for i in range (6):
        if c_msg == speed_inputs[i]:
            global speed_value
            speed_value = int(c_msg) * 51
            print (f"The speed has been set to {c_msg}")
    if c_msg == 'w':
        print(f"[f{speed_value}][f{speed_value}][f{speed_value}][f{speed_value}]")
    elif c_msg == 'a':
        print(f"[r{speed_value}][r{speed_value}][f{speed_value}][f{speed_value}]")
    elif c_msg == 's':
        print(f"[r{speed_value}][r{speed_value}][r{speed_value}][r{speed_value}]")
    elif c_msg == 'd':
        print(f"[f{speed_value}][f{speed_value}][r{speed_value}][r{speed_value}]")