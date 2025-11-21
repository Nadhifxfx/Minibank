import pymysql
from contextlib import contextmanager

@contextmanager
def db_connection():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="ebanking",
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield conn
        conn.commit()
    except:
        conn.rollback()
        raise
    finally:
        conn.close()
