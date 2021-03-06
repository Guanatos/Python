#!/usr/bin/python3

class Hero():
# Class Object Attribute
    honesty = True
# Constructor
    def __init__(self,power,level): 
        print('Hero Contructor')
        self.power = power
        print('Strenght Level')
        self.level = level

    def getAlien(self, alien):
        return "Yes" if alien else "No"

    def fly(self): print('Can fly')

    @staticmethod
    def make_car_sound():
        print('VRoooommmm')

class Human(Hero):
# Class Object Attribute
    honesty = False
# Constructor
    def __init__(self): 
        print('Human Contructor')

    def walk(self): print('can walk')


def main():
    batman = Hero(power='Think',level=5)
    print('Batman can', batman.power)
    print('Batman strenght level', batman.level)
    print('Is Batman a hero?', batman.honesty)
    print('Is Batman an alien?', batman.getAlien(False))

    superman = Hero(power='Fly',level=10)
    print('Superman can', superman.power)
    print('Superman strenght level', superman.level)
    print('Is Superman a hero?', superman.honesty)

    daniel = Human()
    daniel.walk()
    daniel.fly()
    daniel.make_car_sound()

if __name__ == "__main__": main()
