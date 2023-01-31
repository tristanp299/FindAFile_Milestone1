# Name: Tristan Pereira
# Github UN: tristanp299
# Date: 01/30/2023
# Description:
import os

def find_a_file():
    print('*********** Find-A-File ************')
    print('This program can locate a file, folder, or application.\nPlease type in any words or letters you think is '
          'in the name!\nPress \'Ctrl-c\' to go back.')
    try:
        keyword = input('>:')

        search = []

        for path, dirs, file in os.walk(os.path.abspath('/')):
            if keyword in file:
                search.append(path)
                break

        if not search:
            print('Sorry this file cannot be found. Would you like to try again?')
            reponse = input('(y/n):')

            if reponse == 'y': find_a_file()
            elif reponse == 'n': return 0

        else:
            print('Here are your results!')
            for i in search:
                print(i)

            print('Would you like to go again?')
            reponse = input('(y/n):')

            if reponse == 'y':
                find_a_file()
            elif reponse == 'n':
                return 0

    except KeyboardInterrupt as err:
        main()

def main():
    print('Welcome to Find-A-File!')
    print('Here you can locate any file on your system! Please enter an option:')

    response = input('1) Find File\n2) Options\n3) About\n4) Quit')

    if response == '1':
        find_a_file()

if __name__ == '__main__':
    main()

