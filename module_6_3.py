import random


class Animal:
    live = True
    sound = None # звук(изначально отсутствует)
    _DEGREE_OF_DANGER = 0 #степень опасности существа

    def __init__(self, speed):
        self._cords = [0, 0, 0] # координаты в пространстве.
        self.speed = speed

    def move(self, dx, dy, dz):
        if self.speed >= 0:
            new_dx = self._cords [0] + dx * self.speed
            new_dy = self._cords[1] + dy * self.speed
            new_dz = self._cords[2] + dz * self.speed
            self._cords = [new_dx, new_dy, new_dz]
        else:
            print("It's too deep, i can't dive :(")

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True # наличие клюва
    def lay_eggs(self):
        print(f"Here are(is) {random.randint(1, 4)} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz): # В решении почему то ответ X: 10 Y: 20 Z: 0
        new_dz = abs(self._cords[2]) / 2
        self._cords[2] = new_dz


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(AquaticAnimal, Bird, PoisonousAnimal):
    sound = "Click-click-click"

db = Duckbill(10)
print(db.live)
print(db.beak)

db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()