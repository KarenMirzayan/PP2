#!/usr/bin/python

import psycopg2
from config import config

def insert_user_list(user_list):
    sql = "INSERT INTO users(user_name) VALUES(%s)"
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,user_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_phone_numbers(phone_list):
    sql = """INSERT INTO phones(phone_number, phone_id) VALUES(%s, %s)"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.executemany(sql,phone_list)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            cur.close()
            conn.close()


if __name__ == '__main__':
    insert_user_list([
        ('Homer Simpson',),
        ('Jhony Bravo',),
        ('Sponge Bob',),
        ('Gumball',),
        ('Mike Wazowsky',)
    ])
    insert_phone_numbers([
        ('+77771231213', 1,),
        ('+77002348586', 2,),
        ('+77276549192', 3,),
        ('+77005351284', 4,),
        ('+77073766484', 5,)
    ])