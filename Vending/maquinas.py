#!/usr/bin/python3

import sqlite3

def insert(db, row):
    db.execute('INSERT INTO maquinas (maqsn, maqmod, maqloc) VALUES (?, ?, ?)', (row['maqsn'], row['maqmod'], row['maqloc']))
    db.commit()

def retrieve(db, maqsn):
    cursor = db.execute('SELECT * FROM maquinas WHERE maqsn = ?', (maqsn,))
    return cursor.fetchone()

def disp_rows(db):
    cursor = db.execute('SELECT * FROM maquinas ORDER BY maqsn')
    for row in cursor:
        print('  {}: {}: {}'.format(row['maqsn'], row['maqmod'], row['maqloc']))

##### Main #####
def main():
    db = sqlite3.connect('maquinas.db')
    db.row_factory = sqlite3.Row
    print('Create table maquinas')
    db.execute('DROP TABLE IF EXISTS maquinas')
    db.execute('CREATE TABLE maquinas ( maqsn text, maqmod text, maqloc text )')

# Ask for the values

    maqsnx = input("Numero Serial? ")
    maqmodx = input("Modelo? ")
    maqlocx = input("Localidad? ")

    print('Create rows')
    insert(db, dict(maqsn = maqsnx, maqmod = maqmodx, maqloc = maqlocx))
    disp_rows(db)
	
if __name__ == "__main__": main()
