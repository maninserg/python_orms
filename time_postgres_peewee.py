import cProfile
from persons_pets_db_postgres_peewee import main

cProfile.run("main()", sort="time")
