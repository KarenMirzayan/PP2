from config import config
import psycopg2

def delete_user(user):
    sql = '''CALL delete_user_data(%s)'''
    
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(sql, (user,))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

delete_user("Bob")