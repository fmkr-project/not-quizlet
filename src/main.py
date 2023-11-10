#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main entry point"""
import debug

if __name__ == '__main__' :
    # Create the db if it does not exist
    debug = debug.Debug()             #Debug contains db.Database object as the data field and will be used for testing purposes
    debug.reset_database()