#!/usr/bin/python3
""" Script that lists all states from the database"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    curr = db.cursor()
    curr.execute("SELECT * FROM states ORDER BY states.id ASC;")
    data = curr.fetchall()
    for row in data:
        print(row)
