#!/usr/bin/python3
# daniel.nuno@gmail.com

import sqlite3

# This class will be used to handle sqlite3 databases
class rdbms:

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

# Main body
def main():
    db = rdbms(filename = 'test.db', table = 'test')
    print(db)
    print(db.filename)
    print(db.table)

if __name__ == "__main__": main()
