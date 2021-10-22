#!/usr/bin/python

import readchar

def printAllCharsUpTo():
    print('Insira um caracter: ')
    press_char = readchar.readchar()
    print('Printing all caracters from space to ' + str(press_char))
    for i in range(ord(' '), ord(press_char)):
        print(chr(i))


def readAllUpTo(stop_char):

    while(True):
        print('Type something (X to stop): ')
        pressed_key = readchar.readkey()
        print('You typed: ' + str(pressed_key))
        if pressed_key == 'X':
            print('Stoped')
            break

def main():
    print('Start')
    ## Alinea a
    # printAllCharsUpTo()
    readAllUpTo('X')
    print('End')

if __name__ == '__main__':
    main()