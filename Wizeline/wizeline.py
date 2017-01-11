#!/usr/bin/python3
#
# daniel.nuno@gmail.com
#

import sqlite3

# INPUT_A = ['banana','apple','apple','lemon','banana','pineapple','lemon','orange']
# INPUT_B = ['orange','apple','papaya','lemon','banana']
# OUTPUT 
inputa = ['banana','apple','apple','lemon','banana','pineapple','lemon','apple','orange','pineapple','kiwi']
inputb = ['orange','apple','papaya','lemon','banana','pineapple','banana','orange']

print("IA:",inputa)
print("IB:",inputb)

db = sqlite3.connect('test.db')
db.row_factory = sqlite3.Row

#print('CREATE TABLE test1...')
db.execute('DROP TABLE IF EXISTS test1')
db.execute('CREATE TABLE test1 ( t1 text )')
#print('CREATE TABLE test2...')
db.execute('DROP TABLE IF EXISTS test2')
db.execute('CREATE TABLE test2 ( t1 text )')

def disp_rows1(db):
    cursor = db.execute('SELECT t1, count() AS cx FROM test1 GROUP BY t1 ')
    for row in cursor:
        print('A  {}: {}'.format(row['t1'], row['cx']))

def disp_rows2(db):
    cursor = db.execute('SELECT t1, count() AS cx FROM test2 GROUP BY t1 ')
    for row in cursor:
        print('B {}: {}'.format(row['t1'], row['cx']))

i = 0
#print('INSERT rows')
while i < len(inputa):
    db.execute('INSERT INTO test1 ( t1 ) VALUES (?)', (inputa[i],))
    db.commit()
    i = i + 1
#disp_rows1(db)

i = 0
#print('INSERT rows')
while i < len(inputb):
    db.execute('INSERT INTO test2 ( t1 ) VALUES (?)', (inputb[i],))
    db.commit()
    i = i + 1
#disp_rows2(db)

# We should put the elements on a dictionary structure
d1 = {}
cursor = db.execute('SELECT t1, count() AS cx FROM test1 GROUP BY t1 ')
for row in cursor:
#    print(row['t1'])
#    print(row['cx'])
    d1[row['t1']] = row['cx']
#print(d1)
d2 = {}
cursor = db.execute('SELECT t1, count() AS cx FROM test2 GROUP BY t1 ')
for row in cursor:
#    print(row['t1'])
#    print(row['cx'])
    d2[row['t1']] = row['cx']
#print(d2)
# review d1
keysx = list(d1.keys())
#print(keysx)
print("Parsing IA...")
for i in keysx:
#   print(i)
#   print(d1[i])
#   print(d2[i])
   if not i in d2:
      print("D1:",i,d1[i])
      continue
   if d1[i] <= d2[i]:
      print("D1:",i,d1[i])
   elif d1[i] > d2[i]:
      print("D2:",i,d2[i])
   else:
      print("key not found on D1:",i)
keysy = list(d2.keys())
#print(keysy)
print("Parsing IB...")
for i in keysy:
#   print(i)
#   print(d1[i])
#   print(d2[i])
   if not i in d1:
      print("D2:",i,d2[i])
      continue
   if d2[i] <= d1[i]:
      print("D2:",i,d2[i])
   elif d2[i] > d1[i]:
      print("D1:",i,d1[i])
   else:
      print("key not found on D2:",i)
