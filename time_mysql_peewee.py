import cProfile
from persons_pets_db_myssql_peewee import main

cProfile.run("main()", sort="time")
