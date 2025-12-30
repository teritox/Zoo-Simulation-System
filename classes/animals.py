class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.energy = 50

    def eat(self):
        print(f'{self.name} eats some food.')

    def sleep(self):
        self.change_energy(30)
        print(f'{self.name} lays down to sleep.')

    def change_energy(self, amount):
        new_energy = self.energy + amount

        if new_energy > 100:
            new_energy = 100
        elif new_energy < 0:
            new_energy = 0

        return new_energy

    def make_sound(self):
        raise NotImplementedError

    def unique_behaviour(self):
        raise NotImplementedError


class Herbivore(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def eat(self):
        self.energy = self.change_energy(25)
        print(f'{self.name} ate some plants')


class Carnivore(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def eat(self):
        self.energy = self.change_energy(35)
        print(f'{self.name} ate a chunk of meat')


class Elephant(Herbivore):
    species = 'Elephant'

    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        self.energy = self.change_energy(-10)
        print(f'{self.name} made a loud trumpetsounding noise')

    def unique_behaviour(self):
        self.energy = self.change_energy(-20)
        print(f'{self.name} is splashing aroung in the pond.')


class Lion(Carnivore):
    species = 'Lion'

    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        self.energy = self.change_energy(-10)
        print(f'{self.name} roars loudly!')

    def unique_behaviour(self):
        self.energy = self.change_energy(-40)
        print(f'{self.name} is hunting a small critter.')


class Monkey(Herbivore):
    species = 'Monkey'

    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        self.energy = self.change_energy(-10)
        print(f'{self.name} makes a playful chatter sound up in a tree.')

    def unique_behaviour(self):
        self.energy = self.change_energy(-30)
        print(f'{self.name} steels food from one of the visitors!')
