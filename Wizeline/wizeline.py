#!/usr/bin/python3

import sqlite3

db = sqlite3.connect('test.db')
db.row_factory = sqlite3.Row

print('CREATE TABLE test...')
db.execute('DROP TABLE IF EXISTS test')
db.execute('CREATE TABLE test ( t1 text )')

def disp_rows(db):
    cursor = db.execute('SELECT t1, count() as cx FROM test GROUP BY t1 ')
    for row in cursor:
        print('  {}: {}'.format(row['t1'], row['cx']))

# INPUT_A = ['banana','apple','apple','lemon','banana','pineapple','lemon','orange']
# INPUT_B = ['orange','apple','papaya','lemon','banana']
# OUTPUT 
inputa = ['banana','apple','apple','lemon','banana','pineapple','lemon','orange']
inputb = ['orange','apple','papaya','lemon','banana','pineapple']

i = 0
print('INSERT rows')
while i < len(inputa):
    db.execute('INSERT INTO test ( t1 ) VALUES (?)', (inputa[i],))
    db.commit()
    i = i + 1
disp_rows(db)
# len proporciona la longitud
#lenx = len(inputa)
#leny = len(inputb)
# set proporciona elementos unicos
#uniqa = set(inputa)
#uniqb = set(inputb)
#print(uniqa)
#print(uniqb)
# list transforma un set en una lista
#tempax = list(uniqa)
#tempbx = list(uniqb)
# 
#print('listas unicas')
#print(tempax)
#print(tempbx)
# convert the sorted list to dictionary
#d1 = {}
#print(len(tempbx))
#i = 0 
#while i < len(tempbx):
#    d1[tempbx[i]] = tempbx[i]
#    i = i + 1
#print(d1)
