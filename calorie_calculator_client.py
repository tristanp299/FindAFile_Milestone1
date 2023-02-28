# Name: Maggie Wu
# Github UN: wumag
# Date: 02/14/2023
# Description: Client code to send requests

import zmq
import time
import os

# Lambda function that clears the console
clear = lambda: os.system('clear')

context = zmq.Context()

print("Connecting to Calorie Calculator...")
time.sleep(5)
clear()

# ZeroMQ socket object connects to the Calorie Calculator service
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:6666")

# Read the path from a text file and get the filename and extension
with open('request.txt', 'r') as f:
    path = f.read().strip()
filename = os.path.basename(path)
name_without_extension, extension = os.path.splitext(filename)

requests = ["{}{} {}".format(name_without_extension, extension, "gender"),
            "{}{} {}".format(name_without_extension, extension, "weight"),
            "{}{} {}".format(name_without_extension, extension, "height"),
            "{}{} {}".format(name_without_extension, extension, "age"),
            "{}{} {}".format(name_without_extension, extension, "activity"),
            "{}{} {}".format(name_without_extension, extension, "calories")]

for request in requests:
    print(f"Sending request '{request}'...")
    socket.send_string(request)

    message = socket.recv()
    message = message.decode('UTF-8')
    history = message.split(',')
    print()
    print(f"Your calorie calculation history: ")
    for variable in history:
        print(variable)
    print("--------------------------------")