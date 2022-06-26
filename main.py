class Entity:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.__weight = weight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        self.__weight = value

    def __str__(self):
        return f"{self.name} {self.height} {self.weight}"

    def go(self):
        print("Какое то существо")


class Temirlan(Entity):
    def __init__(self, name, height, weight, iq):
        Entity.__init__(self, name, height, weight)
        self.iq = iq

    def go(self):
        print("Шагать")

    def test(self):
        if self.iq >= 50:
            print(f"{self.name} is a Human")
        else:
            print(f"{self.name} he is not human, he is animal or ameba")


entity = Temirlan("Temirlan", 186, 70, 120)
Temirlan.test(entity)
