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


def insert_into_kinds_pets(kind_pets):
    conn = up_connect_to_database()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO kinds_pets(kind_pets) VALUES
                   (%s)""", (kind_pets,))
    conn.commit()
    conn.close()


def insert_into_persons(name, birth, is_relative):
    conn = up_connect_to_database()
    cursor = conn.cursor()
    birthday_iso = date(birth[0], birth[1], birth[2])
    cursor.execute("""INSERT INTO persons(name, birthday, is_relative)
                   VALUES
                   (%s,%s,%s)""", (name, birthday_iso, is_relative))
    conn.commit()
    conn.close()


def insert_into_pets(name, kind_pets, owner):
    conn = up_connect_to_database()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO pets(name, kind_pets, owner)
                   VALUES
                   (%s,%s,%s)""", (name, kind_pets, owner))
    conn.commit()
    conn.close()


def drop_all_tables():
    drop_table_pets()
    drop_table_persons()
    drop_table_kinds_pets()


def create_all_tables():
    create_table_persons()
    create_table_kinds_pets()
    create_table_pets()


def insert_into_kinds_pets_all():
    insert_into_kinds_pets("cat")
    insert_into_kinds_pets("dog")
    insert_into_kinds_pets("bird")
    insert_into_kinds_pets("fish")


def insert_into_persons_all():
    insert_into_persons("Bob", (1980, 12, 23), True)
    insert_into_persons("Alice", (1983, 7, 5), True)
    insert_into_persons("Grandma L.", (1960, 5, 14), True)
    insert_into_persons("Herb", (1977, 10, 3), False)


def insert_into_pets_all():
    insert_into_pets("Kitty", 1, 1)
    insert_into_pets("Fido", 2, 3)
    insert_into_pets("Mittens", 1, 4)
    insert_into_pets("Mittens Jr", 1, 4)


def main():
    drop_all_tables()
    create_all_tables()
    insert_into_kinds_pets_all()
    insert_into_persons_all()
    insert_into_pets_all()


if __name__ == "__main__":

    main()
