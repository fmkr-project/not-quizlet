#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main entry point"""

import deck
import db

import sqlite3 as sql

if __name__ == '__main__' :
    # Create the db if it does not exist
    with open('res/create_database.sql') as sqlfile:
        script = sqlfile.read()
    
    data = db.Database()
    data.connect()
    data.execute_sql(script)
    data.create_card("Front_card", "Back_card")
    data.delete_card(1)
    data.create_deck("deck_0", "description_0")

    # Put here the main loop code