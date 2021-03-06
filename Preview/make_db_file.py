#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    make_db_file.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.06   10:35
-------------------------------------------------------------------------------
   @Change:   2020.05.06
-------------------------------------------------------------------------------
"""

dbfilename = 'people-file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'


def store_dbase(db, dbfilename=dbfilename):
    dbfile = open(dbfilename, 'w')
    for key in db:
        print(key, file=dbfile)
        for (name, value) in db[key].items():
            print(name + RECSEP + repr(value), file=dbfile)
        print(ENDREC, file=dbfile)
    print(ENDDB, file=dbfile)
    dbfile.close()


def load_dbase(dbfilename=dbfilename):
    dbfile = open(dbfilename)
    import sys
    sys.stdin = dbfile
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = input()
        db[key] = rec
        key = input()
    return db


if __name__ == '__main__':
    from initdata import db
    store_dbase(db)
