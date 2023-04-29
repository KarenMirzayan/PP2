from config import config
import psycopg2

def add_users(user_list, user_phones):
    sql = 'CALL add_users (%s,%s)'
    
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(sql, (user_list, user_phones) )
        
        messages = conn.notices
        for i in messages:
            print(i)
        
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

add_users(['John', 'Mary', 'Bob'],['+77001744819', '+77472993984', '+77005966949'])