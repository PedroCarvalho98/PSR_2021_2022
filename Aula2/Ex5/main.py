#!/usr/bin/python

import readchar
from colorama import Fore, Back, Style

def countNumbersUpto(stop_char):
    total_numbers = 0
    total_others = 0
    pressed_keys = []

    while(True):
        print('Type something (X to stop): ')
        pressed_key = readchar.readkey()

        if pressed_key == 'X':
            print('You typed ' + Fore.RED + str(pressed_key) + Style.RESET_ALL + ' terminating.')
            break
        else:
            # print('You typed: ' + Fore.RED + (pressed_key) + Style.RESET_ALL)
            pressed_keys.append(pressed_key)

    print('The keys you pressed were: ' + str(pressed_keys))

    pressed_numbers = []
    pressed_others = []
    for pressed_key in pressed_keys:
        if str.isnumeric(pressed_key):
            total_numbers += 1
            pressed_numbers.append(pressed_key)
        else:
            total_others += 1
            pressed_others.append(pressed_key)

    print('You entered ' + str(total_numbers) + ' numbers: ' + str(pressed_numbers))
    print('You entered ' + str(total_others) + ' others:' +  str(pressed_others))

    text = ''
    colors = [Fore.RED, Fore.YELLOW, Fore.BLACK, Fore.CYAN, Fore.BLUE, Fore.GREEN, Fore.MAGENTA] * len(pressed_others)
    idx = 0
    for press_other in pressed_others:
        color = colors[idx]
        text += color + press_other + Style.RESET_ALL
        idx += 1

    print('Colored text: ')
    print(text)

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