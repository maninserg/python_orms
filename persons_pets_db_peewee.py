from peewee import *
from datetime import date
from config import db_config


user = db_config['postgres']['user']
password = db_config['postgres']['user']
host = db_config['postgres']['host']
port = db_config['postgres']['port']

db = PostgresqlDatabase('demo4', user=user, password=password, host=host,
                        port=port)


class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta():
        database = db


class KindPets(Model):
    kind_pets = CharField()

    class Meta():
        database = db


class Pet(Model):
    name = CharField()
    kind_pets = ForeignKeyField(KindPets)
    owner = ForeignKeyField(Person)

    class Meta():
        database = db



if __name__ == "__main__":

    Pet.drop_table()
    Person.drop_table()
    KindPets.drop_table()


    Person.create_table()
    KindPets.create_table()
    Pet.create_table()


    kinds_pets = ["cat", "dog", "bird", "fish"]
    for i,item in enumerate(kinds_pets):
        add_kind_pets = KindPets(kind_pets=item)
        add_kind_pets.save()


    persons = [{"name": "Bob", "birth": (1980,12,23), "is_rel": True},
               {"name": "Alice", "birth": (1983,7,5), "is_rel": True},
               {"name": "Grandma L", "birth": (1960,5,14), "is_rel": True},
               {"name": "Herb", "birth": (1977,10,3), "is_rel": False}]
    for i,item in enumerate(persons):
        date_iso = date(item["birth"][0],item["birth"][1],item["birth"][2])
        add_person = Person.create(name=item["name"],birthday=date_iso,
                                   is_relative=item["is_rel"])
        add_person.save()


    pets = [{"name": "Kitty", "kind_pets": 1, "owner": 1},
            {"name":"Fido", "kind_pets": 2, "owner": 3},
            {"name": "Mittens", "kind_pets": 1, "owner": 4},
            {"name": "Mittens Jr", "kind_pets": 1, "owner": 4}]
    for i,item in enumerate(pets):
        add_pet = Pet.create(name=item["name"], kind_pets=item["kind_pets"],
                             owner=item["owner"])
        add_pet.save()
