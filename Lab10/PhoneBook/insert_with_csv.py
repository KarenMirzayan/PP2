import psycopg2
import csv
from config import config

def insert_with_csv(list):
    sql = """INSERT INTO users(user_name) VALUES(%s);
    INSERT INTO phones(phone_number, phone_id) VALUES(%s, %s);"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.executemany(sql,list)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("[INFO]", error)
    finally:
        if conn is not None:
            cur.close()
            conn.close()
s = []
with open(r"Lab10\PhoneBook\phonebook.csv", 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        s.append((row[1], row[2], row[0]))
insert_with_csv(s)
