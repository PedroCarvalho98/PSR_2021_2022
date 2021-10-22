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
            print('Stopped')
            break

def countNumbersUpto(stop_char):
    total_numbers = 0
    total_others = 0
    while(True):
        print('Type something (X to stop): ')
        pressed_key = readchar.readkey()
        print('You typed: ' + str(pressed_key))
        if str.isnumeric(pressed_key):
            total_numbers += 1
        else:
            total_others += 1
        if pressed_key == 'X':
            print('Stopped')
            break
    print('You entered ' + str(total_numbers) + ' numbers.')
    print('You entered ' + str(total_others) + ' others.')

def main():
    print('Start')
    # # Alinea a
    # printAllCharsUpTo()
    # # Alinea b
    # readAllUpTo('X')
    # Alinea c
    countNumbersUpto('X')
    print('End')

if __name__ == '__main__':
    main()