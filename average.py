#!/usr/bin/python3

import sys

def main():
    print("Enter the numbers: ")
    data = sys.stdin.readlines()
    #numbers = input("Numeros: ")
    num = int(len(data))
    print(num)
#    print("The average is:",numbers)

if __name__ == "__main__": main()
