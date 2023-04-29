#!/usr/bin/python
import psycopg2
from config import config


def part_of_name(name_pattern):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.callproc("search_phonebook", (name_pattern,))
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("[INFO]", error)
    finally:
        if conn is not None:
            conn.close()

part_of_name('Kar')