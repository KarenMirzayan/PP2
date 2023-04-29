#!/usr/bin/python
import psycopg2
from config import config


def add_or_update_user(user_name, phone):

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute('CALL add_or_update_user(%s,%s)', (user_name, phone))

        conn.commit()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    add_or_update_user('Oleg', '+77006574319')
