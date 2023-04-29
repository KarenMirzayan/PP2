import psycopg2
from config import config

def get_phones():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT users.user_id, users.user_name, phones.phone_number FROM users, phones WHERE users.user_id=phones.phone_id ORDER BY users.user_id;")
        rows = cur.fetchall()
        print("The number of users: ", cur.rowcount)
        for row in rows:
            print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    get_phones()
