#!/usr/bin/env python3

class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

class Pet(Animal):
    def describe(self):
        descr = f'Pet name: {self.name}\n'f'Pet age: {self.age}\n'f'Pet weight: {self.weight}\n'
        print(descr)

class dog(Pet):
    def __init__(self, name, age, weight, kind='dog'):
        super().__init__(name, age, weight)
        self.kind = kind

class beaver(Pet):
    def __init__(self, name, age, weight, kind='beaver'):
        super().__init__(name, age, weight)
        self.kind = kind

class cow(Pet):
    def __init__(self, name, age, weight, kind='cow'):
        super().__init__(name, age, weight)
        self.kind = kind

class Person:
    def __init__(self, full_name, age, sex):
        self.full_name = full_name
        self.age = age
        self.sex = sex

class Owner(Person):
    def __init__(self, full_name, age, sex, pets_arr=None):
        super().__init__(full_name, age, sex)
        if pets_arr is None:
            pets_arr = []
        self.pets_arr = pets_arr

    def add_pet(self, pet):
        self.pets_arr.append(pet)

    def remove_pet(self, pet):
        if pet in self.pets_arr:
            self.pets_arr.remove(pet)

    def describe_by_kind(self, kind):
        print('\nOwner:', self.full_name)
        print('Pets:')
        for pet in self.pets_arr:
            if(pet.kind == kind):
                print(f'- {pet.name}')

    def describe(self):
        print('\nOwner:', self.full_name)
        print('Pets:')
        for pet in self.pets_arr:
            print(f'- {pet.name}')

    def transfer_pet(self, *pets, target_owner):
        for pet in pets:
            if pet in self.pets_arr:
                self.pets_arr.remove(pet)
                target_owner.add_pet(pet)

    def __contains__(self, pet):
        print(f'\n{self.full_name} has {len(self.pets_arr)} pet(s).')        
        if pet in self.pets_arr:
            print(f'{self.full_name} has {pet.name}')
        else:
            print(f'{self.full_name} doesn`t have {pet.name}')

if __name__ == '__main__':

    vivarok = dog('Vivarok', 2, 3)
    tolik = dog('Tolik', 7, 4)
    bober = beaver('Bober', 5, 9)
    doris = beaver('Doris', 12, 11)
    marisya = cow('Marisya', 5, 6)

    Rostyk = Owner('Rostyk', 18, 'M', [tolik, bober, marisya])
    Solya = Owner('Solya', 24, 'F', [vivarok, doris])

    print('\nOriginal pets of an owner')
    Rostyk.describe()

    print('\nAdded Marisya the cow')
    Rostyk.add_pet(marisya)
    Rostyk.describe()

    print('\nDeleted the cow :(')
    Rostyk.remove_pet(marisya)  
    Rostyk.describe()

    print('\nPrints elements with similar kind argument: ')
    Rostyk.describe_by_kind('beaver')

    print('\nTransfering pets to other owner: ')
    Rostyk.transfer_pet(tolik, bober, marisya, target_owner=Solya)
    Solya.describe()
    Rostyk.describe()

    print('\nPrints quantity of pets and checks if there are specified pet')
    Solya.__contains__(tolik)
