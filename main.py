from charactor import Character
from berserk import Berserk


player1 = Character(name='Motya', damage=10)
player2 = Berserk(name='Valera')

player1.print_stats()
print()
player2.print_stats()

while player1.health > 0 and player2.health > 0:
    print()
    damage_p1 = player1.attack(player2)
    damage_p2 = player2.attack(player1)
    print(f'{player1.name} атаковал {player2.name} и нанес {damage_p1} урона.')
    print(f'{player2.name} атаковал {player1.name} и нанес {damage_p2} урона.')
    print(f'Y {player1.name} осталось {player1.name} здоровья.')
    print(f'Y {player2.name} осталось {player2.name} здоровья.')

player1.print_stats()
print()
player2.print_stats()