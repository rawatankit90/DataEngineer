import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    # connect to default database
    init_conn = "host=127.0.0.1 dbname=studentdb user=student password=student"
    conn = psycopg2.connect(init_conn)
    
    # setting autocommit in database 
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    drop_database = "DROP DATABASE IF EXISTS sparkifydb"
    cur.execute(drop_database)
    create_database = """CREATE DATABASE sparkifydb 
    WITH ENCODING 'utf8' TEMPLATE template0"""
    cur.execute(create_database)
    
    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    sparkify_conn = """host=127.0.0.1 dbname=sparkifydb
    user=student password=student"""
    conn = psycopg2.connect(sparkify_conn)
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
