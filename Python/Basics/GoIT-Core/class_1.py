class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self,color):
        Animal.color = color

first_animal= Animal('Alma', 12)
second_animal= Animal('Freia', 20)
second_animal.change_color('red')
print((second_animal))