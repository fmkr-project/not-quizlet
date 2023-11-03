#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main entry point"""

import deck
import db

import sqlite3 as sql
import os

DATABASE_LOCATION = "res/data.db"

if __name__ == '__main__' :
    # Create the db if it does not exist
    with open('res/create_database.sql') as sqlfile:
        script = sqlfile.read()
    
    data = db.Database(sql.connect(DATABASE_LOCATION))

    data.execute_sql(script)

    # Put here the main loop code