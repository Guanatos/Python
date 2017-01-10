#!/usr/bin/python3
########################
# daniel.nuno@gmail.com
########################

##########
# Import #
##########
import sqlite3
import datetime

##########
# Global #
##########
db = sqlite3.connect('vending.db')
db.row_factory = sqlite3.Row

#############
# Functions #
#############
def insert(db, tbl,  row):
    if tbl == 'maquinas':
    	db.execute('INSERT INTO maquinas (maqid, maqmod, maqloc) VALUES (?, ?, ?)', (row['maqid'], row['maqmod'], row['maqloc']))
    elif tbl == 'producto':
    	db.execute('INSERT INTO producto (prodid, prodname, prodcate, proddesc) VALUES (?, ?, ?, ?)', (row['prodid'], row['prodname'], row['prodcate'], row['proddesc']))
    db.commit()

def retrieve(db, maqid):
    cursor = db.execute('SELECT * FROM maquinas WHERE maqid = ?', (maqid,))
    return cursor.fetchone()

def disp_rows(db, tbl):
    if tbl == 'maquinas':
        cursor = db.execute('SELECT * FROM maquinas ORDER BY maqid')
        for row in cursor:
            print('  {}: {}: {}'.format(row['maqid'], row['maqmod'], row['maqloc']))
    elif tbl == 'producto':
        cursor = db.execute('SELECT * FROM producto ORDER BY prodid')
        for row in cursor:
            print('  {}: {}: {}: {}'.format(row['prodid'], row['prodname'], row['prodcate'], row['proddesc']))
    elif tbl == 'visitas':
        cursor = db.execute('SELECT * FROM visitas ORDER BY visitid')
        for row in cursor:
            print('  {}: {}: {}: {}'.format(row['visitid'], row['visitdate'], row['maqloc'], row['visitamount']))

#################
# Create tables #
#################
def create_db():
    print('Creating tables...')
    tablesx = ['maquinas','producto','visitas']
    for i in tablesx:
        print('CREATE TABLE ',i)
        db.execute('DROP TABLE IF EXISTS {tn}'.format(tn=i))
        print('DROP TABLE ',i)
        if i == 'maquinas':
           db.execute('CREATE TABLE maquinas ( maqid text PRIMARY KEY NOT NULL, maqmod text NOT NULL, maqloc text NOT NULL)')
        elif i == 'producto':
           db.execute('CREATE TABLE producto ( prodid int PRIMARY KEY NOT NULL, prodname text NOT NULL, prodcate text NOT NULL, proddesc text)')
        elif i == 'visitas':
           db.execute('CREATE TABLE visitas ( visitid int PRIMARY KEY NOT NULL, visitdate date NOT NULL, maqloc text NOT NULL, visitamount REAL)')

###############
# Insert data #
###############
def test_insert_db():
# Ask for the values
#   maqidx = input("Numero Serial? ")
#   maqmodx = input("Modelo? ")
#   maqlocx = input("Localidad? ")
#   insert(db,'maquinas',dict(maqid = maqidx, maqmod = maqmodx, maqloc = maqlocx))

# maquinas ( maqid text PRIMARY KEY NOT NULL, maqmod text NOT NULL, maqloc text NOT NULL)')
    print('Inserting rows for maquinas...')
    insert(db,'maquinas',dict(maqid = '1234a', maqmod = 'AMS-360' , maqloc = 'PROGRESO'))
    insert(db,'maquinas',dict(maqid = '1234A', maqmod = 'AMS-360' , maqloc = 'FEDEX'))
# Duplicates should not be allowed,  A != a
#    insert(db, dict(maqid = '1234A', maqmod = 'AMS-360' , maqloc = 'COMUDE'))
    insert(db,'maquinas',dict(maqid = '1234b', maqmod = 'AMS-360' , maqloc = 'TOSHIBA'))
    insert(db,'maquinas',dict(maqid = '1234c', maqmod = 'AMS-360' , maqloc = 'COTTON'))
    print('Inserting successfully')
# Retriving rows
    disp_rows(db,'maquinas')

# producto ( prodid int PRIMARY KEY NOT NULL, prodname text NOT NULL, prodcate text NOT NULL, proddesc text)')
    print('Inserting rows for producto...')
    insert(db,'producto',dict(prodid = '1234a', prodname = 'AMS-360' , prodcate = 'PROGRESO', proddesc = ''))
    insert(db,'producto',dict(prodid = '1234b', prodname = 'AMS-360' , prodcate = 'PROGRESO', proddesc = ''))
# Duplicates should not be allowed,  A != a
#    insert(db, dict(prodid = '1234a', prodname = 'AMS-360' , prodcate = 'PROGRESO', proddesc = ''))
    insert(db,'producto',dict(prodid = '1234c', prodname = 'AMS-360' , prodcate = 'PROGRESO', proddesc = ''))
    insert(db,'producto',dict(prodid = '1234d', prodname = 'AMS-360' , prodcate = 'PROGRESO', proddesc = ''))
    print('Inserting successfully')
# Retriving rows
    disp_rows(db,'producto')

#  visitas ( visitid int PRIMARY KEY NOT NULL, visitdate date NOT NULL, maqloc text NOT NULL, visitamount REAL)')
    print('Inserting rows for visitas...')
    today = datetime.date.today()
    print(today)
    insert(db,'visitas',dict(visitid = '123', visitdate = today, maqloc = 'FEDEX', visitamount = '2000'))
    insert(db,'visitas',dict(visitid = '234', visitdate = today, maqloc = 'COTTON', visitamount = '2000'))
    insert(db,'visitas',dict(visitid = '345', visitdate = today, maqloc = 'COMUDE', visitamount = '2000'))
    insert(db,'visitas',dict(visitid = '456', visitdate = today, maqloc = 'TOSHIBA', visitamount = '2000'))
# Retriving rows
    disp_rows(db,'visitas')

################
##### Main #####
################
def main():
    create_db()
    test_insert_db()
	
if __name__ == "__main__": main()
