

class Monster:
    def __init__(self, name, weaknesses):
        self.name = name
        self.weaknesses = weaknesses

    def printOut(self):
        print(self.name, self.weaknesses, sep=' ')

    @staticmethod
    def biggest_weakness(weakness_list):
        elements = ['Fire', 'Water', 'Thunder', 'Ice', 'Dragon', 'Poison', 'Sleep', 'Paralysis', 'Blast', 'Stun']
        strongest_elements = []
        most_effective = 3
        weaknesses = []
        spot = 0
        for x in weakness_list:
            if x == most_effective:
                weaknesses.append(spot)
            spot = spot + 1
        for y in weaknesses:
            strongest_elements.append(elements[y])
        return strongest_elements


monsters = []

weaknessesList = [3, 0, 2, 2, 1, 3, 3, 3, 3, 3]
monsters.append(Monster('Great Jagras', weaknessesList))

weaknessesList = [2, 3, 2, 2, 2, 2, 2, 2, 2, 2]
monsters.append(Monster('Kulu-Ya-Ku', weaknessesList))

weaknessesList = [2, 0, 3, 2, 1, 1, 3, 3, 2, 2]
monsters.append(Monster('Pukei-Pukei', weaknessesList))

weaknessesList = [2, 3, 0, 2, 1, 3, 2, 2, 2, 2]
monsters.append(Monster('Tobi-Kadachi', weaknessesList))

weaknessesList = [0, 3, 2, 2, 2, 1, 2, 2, 1, 2]
monsters.append(Monster('Anjanath', weaknessesList))

requestedMonster = input("Which Monster? ")
for obj in monsters:
    if obj.name == requestedMonster:
        print(requestedMonster, "is weakest to", obj.biggest_weakness(obj.weaknesses))
