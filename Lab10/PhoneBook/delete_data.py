import psycopg2
from config import config

def delete_user(user_name):
    conn = None
    rows_deleted = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE user_name = %s", (user_name,))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    delete_user()