import psycopg2
from psycopg2.extras import RealDictCursor

DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "898989"
DB_PORT = "5432"

def run_query(query, params=None):
    """
    Executes a SQL query and returns results if SELECT,
    commits if INSERT/UPDATE/DELETE.
    """
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT,
        cursor_factory=RealDictCursor
    )
    cur = conn.cursor()
    cur.execute(query, params or [])
    result = None
    if cur.description:   # means query returned something (SELECT or RETURNING)
        result = cur.fetchall()
        conn.commit()
    else:
        conn.commit()
    cur.close()
    conn.close()
    return result
