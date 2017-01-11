#!/usr/bin/python3
# daniel.nuno@gmail.com

import sqlite3

db = sqlite3.connect('test.db')
db.row_factory = sqlite3.Row

print('CREATE TABLE morgan...')
db.execute('DROP TABLE IF EXISTS morgan')
db.execute('CREATE TABLE morgan ( tcsid int, tcsname text, tcsrole text )')

def disp_rows(db):
    cursor = db.execute('SELECT tcsid, tcsname, tcsrole FROM morgan ORDER BY tcsid ')
    for row in cursor:
        print('  {}: {}'.format(row['tcsid'], row['tcsname'], row['tcsrole']))

# reading from a file
#f = open('morgan.txt')
#print("Entire content:", f.read())
#print("Just a line:", f.readline())
for line in open('morgan2.txt'):
    print(line.strip().split("\t"))
    tcsidx,tcsnameix,tcsrolex = line.strip().split("\t")
    db.execute('INSERT INTO morgan (tcsid, tcsname, tcsrole) VALUES (?, ?, ?)',(tcsidx,tcsnameix,tcsrolex))
db.commit()
disp_rows(db)
cursor = db.execute('SELECT tcsrole, count() AS amount FROM morgan GROUP BY tcsrole')
for row in cursor:
    print('  {}: {}'.format(row['tcsrole'].strip(), row['amount']))
