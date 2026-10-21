class Hero:
    def __init_(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        self.hp -= amount

arthur = Hero("Arthur", 100)
arthur.take_damage(10)
print(arthur.hp)