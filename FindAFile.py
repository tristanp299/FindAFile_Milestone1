# Name: Tristan Pereira
# Github UN: tristanp299
# Date: 01/30/2023
# Description:
import os

def find_a_file(options = None):
    print('*********** Find-A-File ************')
    print('This program can locate a file, folder, or application.\nPlease type in any words or letters you think is '
          'in the name!\nPress \'Ctrl-c\' to go back.')
    try:
        keyword = input('>:')

        search = []
        found = False

        for root, dirs, files in os.walk(os.path.abspath('/Users')):
            print('Looking at.....'+root)

            for name in files:
                if keyword in name:
                    search.append(os.path.join(root,name))
                    found = True
                    break


           # for name in dirs:
            #    if keyword in name:
           #         search.append(os.path.join(root,name))
           #         break

        if not search:
            print('Sorry this file cannot be found. Would you like to try again?')
            reponse = input('(y/n):')

            if reponse == 'y': find_a_file()
            elif reponse == 'n': return 0

        else:
            print('\n******************************')
            print('\nHere are your results!')
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

def options():

    first_match = True
    find_all = False
    find_multiple = False

    print('************ Options **********\n')
    print('1) Find firt match (Quickest)\n2) Find all matches (May take awhile)\n3)Find multiple matches\n4)Go back\n')
    response = ('>:')

    if response == '2':
        find_all = True
        first_match = False
        return [first_match, find_all, find_multiple]

    elif response == '4':
        return None


def main():
    print('Welcome to Find-A-File!')
    print('Here you can locate any file on your system! Please enter an option:')

    response = input('1) Find File\n2) Options\n3) About\n4) Quit\n>:')

    if response == '1':
        find_a_file()

    elif response == '2':
        option = options()
        find_a_file(option)


    elif response == '3':
        print('************** About ************\n')
        print('LLC Find-A-File is a free program dedicated to helping those\nthat are lost. For more information '
              'please visit https://www.not-a-website.com')

        answer = input('Press 1) to go back')

        if answer == '1':
            main()

        else:
            return 0

if __name__ == '__main__':
    main()

