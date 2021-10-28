#!/usr/bin/python3
# --------------------------------------------------
# A python script for complex number operations using named tuples and classes
# Rafael Inacio Siopa.
# PSR, November 2021.
# --------------------------------------------------

import argparse
import math
from colorama import Fore, Back, Style
import readchar
from time import time, ctime

parser = argparse.ArgumentParser(description='Definition of test mode')
parser.add_argument('-mv', '--max_value', type=int, required=True, help='Max number of seconds for time mode or maximum number of inputs for number of inputs mode.\n ')
parser.add_argument('-utm', '--use_time_mode', action='store_true', help='Max number of secs for time mode or maximum number of inputs for number of inputs mode.\n ')
args = vars(parser.parse_args())
print(args)

def main():
    seconds = time()
    print(Fore.RED + 'PARI' + Style.RESET_ALL + ' Typing Test, P2, Grupo 7, ' + ctime(seconds))
    print('Test running up to ' + str(args['max_value']) + ' seconds.')

    if args['use_time_mode']:
        tstop = args['max_value']      #max time set
        N = math.inf
    else:
        tstop = math.inf
        N = args['max_value']     #max inputs set!

    print('Press any key to start the test')
    readchar.readchar()
    t1 = time()
    t2 = time()
    count = 0

    while (count < N) and (t2 - t1 < tstop):
        a = t2 - t1
        print(a)
        readchar.readchar()
        count = count + 1
        t2 = time()



if __name__ == '__main__':
    main()