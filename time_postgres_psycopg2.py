import cProfile
from persons_pets_db_psycopg2 import main

cProfile.run("main()", sort="time")
