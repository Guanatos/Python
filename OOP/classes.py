#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Cow:
    def mou(self):
        print('Mooouu!')

    def run(self):
        print ('Runs like a cow')

class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

    clarabella = Cow()
    clarabella.mou()
    clarabella.run()

if __name__ == "__main__": main()
