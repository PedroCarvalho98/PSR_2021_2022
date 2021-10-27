#!/usr/bin/python

from time import time, ctime
from colorama import Fore, Back, Style

max_number = 50000000

def tic():
    seconds = time()
    return seconds

def toc(seconds):
    return time() - seconds

def main():
    seconds = tic()
    print("This is " + Fore.RED + "Ex1" + Style.RESET_ALL + " and the current date is " + Back.YELLOW + Fore.BLUE + ctime(seconds) + Style.RESET_ALL)
    for i in range(1, max_number):
        raiz = i ** -2
    time = toc(seconds)
    print("Ellapsed time " + str(time) + " seconds.")

if __name__ == '__main__':
    main()