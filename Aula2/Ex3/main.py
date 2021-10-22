#!/usr/bin/python3

from colorama import Fore, Back, Style
import argparse
from my_functions import *

def main():

    parser = argparse.ArgumentParser(description='Ask for maximum number')
    parser.add_argument('--maximum_number', type = int, help='Maximum number to search for primes')
    parser.add_argument('--showfinaltext', action = 'store_true', help='print to the terminal or not')
    args = vars(parser.parse_args())
    print(args)

    print("Starting to compute prime numbers up to " + str(args['maximum_number']))
    count = 0 # initialize the counter
    for i in range(1, args['maximum_number']):
        if my_functions(i):
            print('Number ' + Fore.YELLOW + Back.GREEN + str(i) + Style.RESET_ALL + ' is prime.' )
            count = count + 1
        else:
            print('Number ' + str(i) + ' is not prime.')

    if args['showfinaltext']:
        print(Fore.BLUE  + 'I found ' + str(count) + ' prime numbers between 1 and ' + str(args['maximum_number']) + Style.RESET_ALL)

if __name__ == "__main__":
    main()