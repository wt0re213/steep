class Character:
    def __init__(self, name='Vasya', health=100, damage=5, defense=0):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense

    def print_stats(self):
        print(f' -- {self.name}')
        print(f'Здровье {self.health}')
        print(f'Урон {self.damage}')
        print(f'Защита {self.defense}')

    def attack(self, enemy):
        return enemy.take_damage(self.damage)

    def take_damage(self, damage):
        damage = max(damage, 0)
        self.health -= damage
        return damage

    def alive(self):
        return self.health > 0