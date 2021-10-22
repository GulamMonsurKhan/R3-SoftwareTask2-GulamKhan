# Controlling a 4-wheel Rover
For this task simple rover navigation controls were programmed. This program works by receiving input from the client and sends it to the server. This was achieved using the socket and pynput imports. A connection is established to the server, and all the keystrokes inputted from the client side are logged by the listener function. All the inputs are then sent to the server. The server then reads the inputs, and if it matches any of the values in a predefined speedvalues array, it sets the message to equal a speed variable. If the sent data is not in the predefined array, it is checked to see if it matches any movement inputs that are valid, in the case of this program, 'wasd'. If it is equal to any of the valid keystrokes, a movement command is issued using the appropriate speed values. The rover is controlled using differential steering. Pressing 'ESC' will abort the connection to the server.





https://user-images.githubusercontent.com/91355029/138376295-f96c9c62-3ab2-4c60-b536-7dcbc127c2fc.mp4



# Note
Pressing 'ESC' will sever the connection, but the server will remain operational

# Known bugs
The program will break if a speed value is not set first.
