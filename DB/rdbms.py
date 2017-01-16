#!/usr/bin/python3
# Based on sqlite3-class.py by Bill Weinman [http://bw.org/]
# daniel.nuno@gmail.com

import sqlite3

# This class will be used to handle sqlite3 databases
class database:

# Contructor, taking filename and table name, default table name 'test'
# **kwargs, take an arbitrary number of keyword arguments, dictionary
# *params, tuple 

    def __init__(self, **kwargs):
        self.filename = kwargs.get('filename')
        self.table = kwargs.get('table', 'test')

    def sql_do(self, sql, *params):
        self._db.execute(sql, params)
        self._db.commit()

    @property
    def filename(self): return self._filename

    @filename.setter
    def filename(self, fn):
        self._filename = fn
        self._db = sqlite3.connect(fn)
        self._db.row_factory = sqlite3.Row

    @filename.deleter
    def filename(self): self.close()

    @property
    def table(self): return self._table

    @table.setter
    def table(self, t): self._table = t

    @table.deleter
    def table(self): self._table = 'test'

    def close(self):
        self._db.close()
        del self._filename

# Crear Tablas
def create_table(db,tablex):
    if tablex == 'visitas':
        db.sql_do('DROP TABLE IF EXISTS visitas')
        db.sql_do('CREATE TABLE visitas (visitid INTEGER PRIMARY KEY AUTOINCREMENT, visitdate date NOT NULL, maqloc text NOT NULL, visitamount real)')
#    elsif:
#    else:

# Insertar Registros
# visitid int PRIMARY KEY NOT NULL, visitdate date NOT NULL, maqloc text NOT NULL, visitamount

def insert(db):
    continuax = True
    while continuax == True:
        vdatex = input("Fecha de visita: ")
        maqlocx = input("Localidad: ")
        vamountx = input("Venta: ")
        db.sql_do('INSERT INTO visitas (visitdate, maqloc, visitamount) VALUES (?, ?, ?)',vdatex,maqlocx,vamountx)
        db.commit()
        answerx = input("Agregar otro registro? (y/n) ")
        answerx = answerx.upper()
#        print(answerx)
        if answerx == 'Y':
           continuax = True
        else:
           continuax = False

# Main body
def main():
    db = database(filename = 'test.db', table = 'test')
    create_table(db,'visitas')
    insert(db)

if __name__ == "__main__": main()
