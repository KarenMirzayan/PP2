import psycopg2
from config import config

def update_data(s):
    sql = """UPDATE users SET user_name=%s WHERE user_id=%s;
    UPDATE phones SET phone_number=%s WHERE phone_id=%s;"""
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,s)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    update_data([
        ('Bart Simpson', '1', '+77073819341', '1',),
        ('Squidward', '3', '+77478745613', '3',)
        ])