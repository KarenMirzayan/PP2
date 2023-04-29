from config import config
import psycopg2

def get_users(limit, offset):
    sql = '''SELECT * FROM get_users(%s, %s)'''
    
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(sql, (limit, offset))
        result = cur.fetchall()
        print(result)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

get_users(5, 1)