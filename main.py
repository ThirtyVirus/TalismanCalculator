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
        if self.netMagicPower != 0:
            self.coinsPerMagicPower = cost / self.netMagicPower
        else:
            self.coinsPerMagicPower = sys.maxsize

    def haschild(self, other):
        if self.previous is None:
            return 0
        return self.previous == other


def compare(x, y):
    if x.haschild(y):
        return 1

    if x.coinsPerMagicPower < y.coinsPerMagicPower:
        return -1
    elif x.coinsPerMagicPower > y.coinsPerMagicPower:
        return 1
    else:
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


if __name__ == '__main__':
    # name, previous talisman, rarity, cost, description
    Talisman("Vaccine Talisman", None, Rarity.COMMON, 0, "potato collection 3, craft w/ 9 poisonous potato from the zombies found @ graveyard")
    Talisman("Potion Affinity Talisman", None, Rarity.COMMON, 400, "netherwart collection 3, craft w/ 128 netherwart & 1 chest")
    Talisman("Potion Affinity Ring", "Potion Affinity Talisman", Rarity.UNCOMMON, 2500, "netherwart collection 7, craft w/ 8 ench netherwart & Potion Affinity Talisman")
    Talisman("Potion Affinity Artifact", "Potion Affinity Ring", Rarity.RARE, 81000, "netherwart collection 9, craft w/ 256 ench netherwart & Potion Affinity Ring")
    Talisman("Melody's Hair", None, Rarity.EPIC, 0, "obtained by completing all harp songs @ Melody NPC in the Park")
    Talisman("Wolf Talisman", None, Rarity.COMMON, 1200000, "rare drop from old wolves at the castle) (cannot be BIN’D on AH, not worth buying")
    Talisman("Wolf Ring", "Wolf Talisman", Rarity.RARE, 70000, "craft w/ Wolf talisman & Weak Wolf Catalyst & 14 ench bone [obtained by killing wolves @ spirit cave]")
    Talisman("Spider Talisman", None, Rarity.UNCOMMON, 120000, "travel to the peak of the spider’s den, kill a broodmother. The broodmother spawns exactly 1 hour after the previous broodmother has died. The only surefire way to find one is to wait up there")
    Talisman("Spider Ring", "Spider Talisman", Rarity.RARE, 3300, "tarantula slayer 1, craft w/ spider talisman & 64 tarantula web")

    from functools import cmp_to_key
    talismans = sorted(talismans, key=cmp_to_key(compare))

    counter = 1
    for talisman in talismans:
        print("%d: %s [%s coins] [+%d mp] [%s coins / mp] (%s)" % (counter, talisman.name, "{:,}".format(talisman.cost), talisman.netMagicPower, "{:,}".format(round(talisman.coinsPerMagicPower)), talisman.description))
        # print(counter, talisman.name, talisman.netMagicPower, round(talisman.coinsPerMagicPower))
        counter += 1
