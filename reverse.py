#!/usr/bin/python3

wordx = input("Give me the word: ")
wordy = list(wordx)
print(wordy)
lenx = int(len(wordx))
i,j = 0,0

while i < lenx:
    print(wordx[i])
    j = lenx - i 
    print(i)
    print(j)
    wordy[j - 1] = wordx[i]
    i = i + 1
print(wordy)

print(lenx)

#for 


