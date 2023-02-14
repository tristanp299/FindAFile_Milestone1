# Name: Tristan Pereira
# Github UN: tristanp299
# Date: 02/13/2023
# Description:

import os
import time

from FindAFile import find_a_file

def main():

    while(True):

        with open(r'example.txt', 'r') as f:
            data = f.readline()

        if data:
            find_a_file(data)

        time.sleep(1)

main()