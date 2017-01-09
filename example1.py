#!/usr/bin/python3

def swapx():
    a = int(input("Value of A: "))
    b = int(input("Value of B: "))
    a = a + b # 5 = 3 + 2
    b = a - b # 3 = 5 - 2
    a = a - b # 2 = 5 - 3
    print("Swapping values: A=",a,"B=",b)

def filex():
    myfile = open("dmesg.txt")
    i,x,y = 0,0,0
    for line in myfile:
# Lenght of the current line
        print("Lenght: ",len(line))
        if line.count('pid'):
           x = x + 1
        if line.count('parent'):
           y = y + 1
# Amount of lines of the file
        i = i + 1
    print("Lineas: ",i)
    print("pid: ",x)
    print("parent: ",y)

def main():
#    swapx()
    filex()

if __name__ == "__main__": main()
