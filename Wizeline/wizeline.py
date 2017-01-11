#!/usr/bin/python3

import sqlite3
# INPUT_A = ['banana','apple','apple','lemon','banana','pineapple','lemon','orange']
# INPUT_B = ['orange','apple','papaya','lemon','banana']
# OUTPUT 
inputa = ['banana','apple','apple','lemon','banana','pineapple','lemon','apple','orange']
inputb = ['orange','apple','papaya','lemon','banana','pineapple','banana','orange']

db = sqlite3.connect('test.db')
db.row_factory = sqlite3.Row

print('CREATE TABLE test1...')
db.execute('DROP TABLE IF EXISTS test1')
db.execute('CREATE TABLE test1 ( t1 text )')
print('CREATE TABLE test2...')
db.execute('DROP TABLE IF EXISTS test2')
db.execute('CREATE TABLE test2 ( t1 text )')

def disp_rows1(db):
    cursor = db.execute('SELECT t1, count() as cx FROM test1 GROUP BY t1 ')
    for row in cursor:
        print('  {}: {}'.format(row['t1'], row['cx']))

def disp_rows2(db):
    cursor = db.execute('SELECT t1, count() as cx FROM test2 GROUP BY t1 ')
    for row in cursor:
        print('  {}: {}'.format(row['t1'], row['cx']))

i = 0
print('INSERT rows')
while i < len(inputa):
    db.execute('INSERT INTO test1 ( t1 ) VALUES (?)', (inputa[i],))
    db.commit()
    i = i + 1
disp_rows1(db)

i = 0
print('INSERT rows')
while i < len(inputb):
    db.execute('INSERT INTO test2 ( t1 ) VALUES (?)', (inputb[i],))
    db.commit()
    i = i + 1
disp_rows2(db)

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
