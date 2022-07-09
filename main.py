# coding=utf-8
import sys
from enum import Enum
talismans = []


class Rarity(Enum):
    NONE = 0
    SPECIAL = 3
    VERY_SPECIAL = 5
    COMMON = 3
    UNCOMMON = 5
    RARE = 8
    EPIC = 12
    LEGENDARY = 16
    MYTHIC = 22


class Talisman:
    name = ""
    previous = None
    next = None
    rarity = Rarity.NONE
    cost = 0
    description = ""
    netMagicPower = 0.0
    coinsPerMagicPower = 0.0

    def __init__(self, name, previous, rarity, cost, description):
        talismans.append(self)
        self.name = name
        self.previous = findtalisman(previous)
        self.rarity = rarity
        self.cost = cost
        self.description = description
        self.netMagicPower = rarity.value
        if previous is not None:
            self.netMagicPower -= self.previous.rarity.value
            self.previous.next = self
        if self.netMagicPower != 0:
            self.coinsPerMagicPower = cost / self.netMagicPower

    def haschild(self, other):
        if self.previous is None:
            return 0
        elif self.previous == other:
            return 1
        else:
            return self.previous.haschild(other)


# the case where y is compared to x
def compare(x, y):
    if x.coinsPerMagicPower > y.coinsPerMagicPower:
        return 1
    elif x.coinsPerMagicPower < y.coinsPerMagicPower:
        return -1

    if x.netMagicPower > y.netMagicPower:
        return -1
    elif x.netMagicPower < y.netMagicPower:
        return 1

    else:
        return 0

def findtalisman(name):
    if name is None or name == "None":
        return None

    for talisman in talismans:
        if talisman.name == name:
            return talisman
    return None

# NOTE: Defining a talisman upgrade before a previous iteration will cause problems
def inittalismans():
    # name, previous talisman, rarity, cost, description
    Talisman("Vaccine Talisman", None, Rarity.COMMON, 0, "potato collection 3, craft w/ 9 poisonous potato from the zombies found @ graveyard")
    Talisman("Farming Talisman", None, Rarity.COMMON, 0, "wheat collection 4, craft w/ 5 hay bales & 4 seeds")
    Talisman("Speed Talisman", None, Rarity.COMMON, 0, "sugarcane collection 2, craft w/ 108 sugarcane")
    Talisman("Campfire Initiate Badge", None, Rarity.COMMON, 0, "obtained via the Fire Trial in the Park")
    Talisman("Campfire Adept Badge", "Campfire Initiate Badge", Rarity.UNCOMMON, 0, "Campfire Initiate Badge & 160 dark oak logs [armor needed N/A]")
    Talisman("Shiny Yellow Rock", None, Rarity.COMMON, 0, "obtained via the Romero & Juliette quest in the Park")
    Talisman("Yellow Rock of Love", "Shiny Yellow Rock", Rarity.COMMON, 0, "Shiny Yellow Rock and 15 poppies")
    Talisman("Cat Talisman", None, Rarity.UNCOMMON, 0, "obtained by completing one of the 4/4 races in the Dungeon Hub")
    Talisman("Lynx Talisman", "Cat Talisman", Rarity.RARE, 0, "obtained by completing two of the 4/4 races in the Dungeon Hub")
    Talisman("Melody's Hair", None, Rarity.EPIC, 0, "obtained by completing all harp songs @ Melody NPC in the Park")
    Talisman("Frozen Chicken", None, Rarity.RARE, 0, "obtained by completing the second checkpoint of the chicken race during the season of Jerry event")
    Talisman("King Talisman", None, Rarity.COMMON, 0, "obtained by talking to every King at the table in the Dwarven Mines, they rotate every skyblock day")
    Talisman("Talisman of Coins", None, Rarity.COMMON, 120, "emerald collection 2, craft w/ 20 emeralds & 5 gold")
    Talisman("Zombie Talisman", None, Rarity.COMMON, 500, "bought at the adventure NPC in the main hub town")
    Talisman("Zombie Ring", "Zombie Talisman", Rarity.UNCOMMON, 350, "zombie slayer 2, craft w/ zombie talisman & 64 rev flesh")
    #Talisman("name", None, Rarity.NONE, 0, "description")
    #Talisman("name", None, Rarity.NONE, 0, "description")
    #Talisman("name", None, Rarity.NONE, 0, "description")
    #Talisman("name", None, Rarity.NONE, 0, "description")
    #Talisman("name", None, Rarity.NONE, 0, "description")
    #Talisman("name", None, Rarity.NONE, 0, "description")

    Talisman("Potion Affinity Talisman", None, Rarity.COMMON, 400, "netherwart collection 3, craft w/ 128 netherwart & 1 chest")
    Talisman("Potion Affinity Ring", "Potion Affinity Talisman", Rarity.UNCOMMON, 2500, "netherwart collection 7, craft w/ 8 ench netherwart & Potion Affinity Talisman")
    Talisman("Potion Affinity Artifact", "Potion Affinity Ring", Rarity.RARE, 81000, "netherwart collection 9, craft w/ 256 ench netherwart & Potion Affinity Ring")
    Talisman("Wolf Talisman", None, Rarity.COMMON, 1200000, "rare drop from old wolves at the castle) (cannot be BIN’D on AH, not worth buying")
    Talisman("Wolf Ring", "Wolf Talisman", Rarity.RARE, 70000, "craft w/ Wolf talisman & Weak Wolf Catalyst & 14 ench bone [obtained by killing wolves @ spirit cave]")
    Talisman("Spider Talisman", None, Rarity.UNCOMMON, 120000, "travel to the peak of the spider’s den, kill a broodmother. The broodmother spawns exactly 1 hour after the previous broodmother has died. The only surefire way to find one is to wait up there")
    Talisman("Spider Ring", "Spider Talisman", Rarity.RARE, 3300, "tarantula slayer 1, craft w/ spider talisman & 64 tarantula web")


if __name__ == '__main__':
    inittalismans()

    # sort talismans by from least coins per mp to most
    from functools import cmp_to_key
    talismans = sorted(talismans, key=cmp_to_key(compare))

    # shove up talisman upgrades which are less expensive than previous iteration
    # (requiring that you get the previous upgrade first)
    finaltalismans = []
    waitingtalismans = []
    for talisman in talismans:
        if talisman.previous is None and talisman.next is None:
            finaltalismans.append(talisman)
        elif talisman.previous is not None:
            if not finaltalismans.__contains__(talisman.previous):
                waitingtalismans.append(talisman)
            else:
                finaltalismans.append(talisman)
        elif talisman.next is not None:
            if waitingtalismans.__contains__(talisman.next):
                finaltalismans.append(talisman)
                finaltalismans.append(talisman.next)
            else:
                finaltalismans.append(talisman)

    print("PRE-FIXED")
    counter = 1
    for talisman in talismans:
        print("%d: %s [%s coins] [+%d mp] [%s coins / mp] (%s)" % (counter, talisman.name, "{:,}".format(talisman.cost), talisman.netMagicPower, "{:,}".format(round(talisman.coinsPerMagicPower)), talisman.description))
        counter += 1

    print("FIXED")
    counter = 1
    for talisman in finaltalismans:
        print("%d: %s [%s coins] [+%d mp] [%s coins / mp] (%s)" % (counter, talisman.name, "{:,}".format(talisman.cost), talisman.netMagicPower, "{:,}".format(round(talisman.coinsPerMagicPower)), talisman.description))
        counter += 1