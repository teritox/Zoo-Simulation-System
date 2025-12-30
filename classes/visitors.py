from classes.animals import Elephant, Lion, Monkey


class Visitor:

    @staticmethod
    def feed_animal(animal):
        animal.change_energy(20)
        print(f'A visitor feeds {animal.name}')

    @staticmethod
    def watch_animal(animal):
        animal.change_energy(5)
        print(f'A visitor is watching {animal.name}')
