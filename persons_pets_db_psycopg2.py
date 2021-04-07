import psycopg2
from datetime import date
from config import db_config

def up_connect_to_database():
    user = db_config['postgres']['user']
    password = db_config['postgres']['pass']
    host = db_config['postgres']['host']
    port = db_config['postgres']['port']
    conn = psycopg2.connect(database="demo3", user=user, password=password,
                            host=host, port=port)
    return conn


def drop_table_pets():
    conn = up_connect_to_database()
    cursor = conn.cursor()
    cursor.execute("""DROP TABLE IF EXISTS pets""")
    conn.commit()
    conn.close()


def drop_table_persons():
    conn = up_connect_to_database()
    cursor = conn.cursor()
    cursor.execute("""DROP TABLE IF EXISTS persons""")
    conn.commit()
    conn.close()


def drop_table_kinds_pets():
    conn = up_connect_to_database()
    cursor = conn.cursor()
    cursor.execute("""DROP TABLE IF EXISTS kinds_pets""")
    conn.commit()
    conn.close()


def create_table_persons():
    conn = up_connect_to_database()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE persons(id SERIAL PRIMARY KEY,
                   name varchar(255) NOT NULL, birthday date NOT NULL,
                   is_relative boolean NOT NULL)""")
    conn.commit()
    conn.close()


def create_table_kinds_pets():
    conn = up_connect_to_database()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE kinds_pets(id SERIAL PRIMARY KEY,
                   kind_pets varchar(255) NOT NULL)""")
    conn.commit()
    conn.close()


def create_table_pets():
    conn = up_connect_to_database()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE pets(id SERIAL PRIMARY KEY,
                   name varchar(255) NOT NULL,
                   kind_pets integer NOT NULL REFERENCES kinds_pets(id),
                   owner integer NOT NULL REFERENCES persons(id))""")
    conn.commit()
    conn.close()


if __name__ == "__main__":

    drop_table_pets()
    drop_table_persons()
    drop_table_kinds_pets()

    create_table_persons()
    create_table_kinds_pets()
    create_table_pets()
