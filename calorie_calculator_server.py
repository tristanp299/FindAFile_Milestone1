# Name: Maggie Wu
# Github UN: wumag
# Date: 02/14/2023
# Description: Server code to receive data

import zmq
import time
import os

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:6666")

# Read the path from the request.txt file and read the contents of the file into a list
with open('request.txt', 'r') as f:
    path = f.read().strip()
with open(path, 'r') as f:
    history = [line.strip() for line in f]

# Lambda function that clears the console
clear = lambda: os.system('clear')

print("Connecting to Calorie Calculator...")
time.sleep(5)
clear()

def main():
    while True:
        msg = socket.recv()
        print("Waiting for request from client...")
        print(f"Request received: {msg}")

        # Decode the message and split it into separate parts
        msg = msg.decode('UTF-8')
        params = msg.split(' ')
        variable = str(params[1])

        # Determine which element of the history list to send back to the client based on the requested variable
        var_dict = {'gender': 0, 'weight': 1, 'height': 2, 'age': 3, 'activity': 4, 'calories': 5}
        i = var_dict.get(variable, -1)  # Returns -1 if variable is not found in var_dict

        socket.send_string(history[i])
        print("Response sent to client!")
        print("--------------------------------")

if __name__ == '__main__':
    main()