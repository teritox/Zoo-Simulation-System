class Visitor:

    @staticmethod
    def feed_animal(animal):
        print(f'A visitor feeds {animal.name}')

    @staticmethod
    def watch_animal(animal):
        print(f'A visitor is watching {animal.name}')
