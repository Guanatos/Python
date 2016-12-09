#!/usr/bin/env python
f = open('file.txt')
print("Entire content:", f.read())
print("Just a line:", f.readline())
for line in open('file.txt'):
    print("Line per line:",line)
