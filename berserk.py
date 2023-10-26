from charactor import Character

class Berserk(Character):
    def __init__(self, name='Vasya', health=100, damage=5, defense=0):
        Character.__init__(self, name, health, damage, defense)
        self.max_health = self.health

    def get_damage(self):
        return self.damage + self.damage * \
            (self.max_health - self.health) / self.max_health

    def attack(self, enemy):
        return enemy.take_damage(self.get_damage())