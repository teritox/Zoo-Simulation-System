from classes.animals import Elephant, Lion, Monkey
from classes.visitors import Visitor
import random


def create_animals():
    animals = []
    animals.append(Elephant('Ella', 34))
    animals.append(Lion('Sophie', 12))
    animals.append(Monkey('Momo', 3))

    return animals


def proceed(animals):
    for animal in animals:
        animal.energy -= 10

        roll_sound = random.randint(1, 4)
        if roll_sound <= 1:
            animal.make_sound()

        roll_unique = random.randint(1, 4)
        if roll_unique <= 1:
            animal.unique_behaviour()


def feed_animals(animals):
    for animal in animals:
        animal.eat()


def end_day(animals):
    for animal in animals:
        animal.sleep()


def visitor_watching(animals):
    roll_watching = random.randint(1, 4)
    if roll_watching >= 3:
        animal = random.choice(animals)
        Visitor.watch_animal(animal)


def visitor_feeding(animals):
    for animal in animals:
        if animal.energy <= 30:
            Visitor.feed_animal(animal)
            animal.eat()
