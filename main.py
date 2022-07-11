# coding=utf-8
import sys
from enum import Enum
talismans = []
finaltalismans = []


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
    LEG_RECOMB = 6
    RARE_EPIC_RECOMB = 4
    UNCOMMON_RECOMB = 3
    COMMON_RECOMB = 2
    LEG_HEGEMONY = 32


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

    def printme(self, counter):
        print("%d: %s [%s coins] [+%d mp] [%s coins / mp] (%s)" % (
        counter, self.name, "{:,}".format(self.cost), self.netMagicPower,
        "{:,}".format(round(self.coinsPerMagicPower)), self.description))

    def haschild(self, other):
        if self.previous is None:
            return 0
        elif self.previous == other:
            return 1
        else:
            return self.previous.haschild(other)


def compare(x, y):
    if x.coinsPerMagicPower > y.coinsPerMagicPower:
        return 1
    elif x.coinsPerMagicPower < y.coinsPerMagicPower:
        return -1

    if x.netMagicPower > y.netMagicPower:
        return -1
    elif x.netMagicPower < y.netMagicPower:
        return 1

    if x.rarity.value > y.rarity.value:
        return -1
    elif x.rarity.value < y.rarity.value:
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


def calculatebudget(budget):
    print("")
    print("Calculating what talismans and upgrades you can buy with", "{:,}".format(budget), "coins:")

    totalcoins = 0
    totalmp = 0
    counter = 0
    for talisman in finaltalismans:
        if totalcoins + talisman.cost < budget:
            totalcoins += talisman.cost
            totalmp += talisman.netMagicPower
            talisman.printme(counter)
            counter += 1
        else:
            break

    print("Total Coins Spent:", totalcoins)
    print("Total MP Gained:", totalmp)


# NOTE: Defining a talisman upgrade before a previous iteration will cause problems
# TODO add case where a talisman isn't worth getting, and the player should skip to buying the better version?
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
    Talisman("Mediocre Ring of Love", "Yellow Rock of Love", Rarity.UNCOMMON, 370, "Yellow Rock of Love & 64 emeralds")
    Talisman("Potion Affinity Talisman", None, Rarity.COMMON, 400, "netherwart collection 3, craft w/ 128 netherwart & 1 chest")
    Talisman("Zombie Talisman", None, Rarity.COMMON, 500, "bought at the adventure NPC in the main hub town")
    Talisman("Zombie Ring", "Zombie Talisman", Rarity.UNCOMMON, 350, "zombie slayer 2, craft w/ zombie talisman & 64 rev flesh")
    Talisman("Skeleton Talisman", None, Rarity.COMMON, 500, "bought at the adventure NPC in the main hub town")
    Talisman("Magnetic Talisman", None, Rarity.UNCOMMON, 690, "emerald collection 3, craft w/ 128 emeralds & 32 redstone")
    Talisman("Sea Creature Talisman", None, Rarity.COMMON, 833, "sponge collection 4, craft w/ 18 sponges")
    Talisman("Wood Affinity Talisman", None, Rarity.UNCOMMON, 1000, "oak wood collection 8, craft w/ 1 ench oak wood & 8 oak leaves")
    Talisman("Red Claw Talisman", None, Rarity.UNCOMMON, 1800, "wolf slayer level 1, craft w/ an ench bone & 8 wolf teeth")
    Talisman("Gravity Talisman", None, Rarity.UNCOMMON, 2200, "obsidian collection 3, craft w/ 144 obsidian")
    Talisman("Village Affinity Talisman", None, Rarity.COMMON, 2500, "bought at the adventure NPC in the main hub town")
    Talisman("Mine Affinity Talisman", None, Rarity.COMMON, 2500, "bought at the adventure NPC in the main hub town")
    Talisman("Potion Affinity Ring", "Potion Affinity Talisman", Rarity.UNCOMMON, 2500, "netherwart collection 7, craft w/ 8 ench netherwart & Potion Affinity Talisman")
    Talisman("Wolf Paw", None, Rarity.UNCOMMON, 3000, "obtained by completing 2nd wood race @ Gustav, need grappling hook (& preferably AOTE)")
    Talisman("Pig's Foot", None, Rarity.RARE, 3000, "obtained by completing the end race, need a grappling hook (& preferably AOTE)")
    Talisman("Sea Creature Ring", "Sea Creature Talisman", Rarity.UNCOMMON, 4100, "sponge collection 6, craft w/ 6 sponge & 2 ench sponge & sea creature talisman")
    Talisman("Raggedy Shark Tooth Necklace", None, Rarity.COMMON, 4200, "craft w/ 1 nurse shark tooth & 8 shark fin")
    Talisman("Dull Shark Tooth Necklace", "Raggedy Shark Tooth Necklace", Rarity.UNCOMMON, 3600, "craft w/ Raggedy Shark Tooth Necklace & 4 nurse shark teeth")
    Talisman("Night Vision Charm", None, Rarity.COMMON, 5500, "mushroom collection 7, craft w/ 4 ench mushrooms each type")
    Talisman("Scavenger Talisman", None, Rarity.COMMON, 10000, "bought at the adventure NPC in the main hub town")
    Talisman("Intimidation Talisman", None, Rarity.COMMON, 10000, "bought at the adventure NPC in the main hub town")
    Talisman("Campfire Cultist Badge", "Campfire Adept Badge", Rarity.RARE, 10000, "Campfire Adept Badge & 1000 spruce logs [growth 5 mush armor set at night to survive]")
    Talisman("Lava Talisman", None, Rarity.UNCOMMON, 11100, "magma cream collection 7, craft w/ 9 ench magma cream")
    Talisman("Talisman of Power", None, Rarity.COMMON, 12000, "gemstone 2, craft w/ 45 flawed ruby gemstone")
    Talisman("Candy Talisman", None, Rarity.UNCOMMON, 12400, "bought w/ 16 green candy @ fear mongerer NPC")
    Talisman("Honed Shark Tooth Necklace", "Dull Shark Tooth Necklace", Rarity.RARE, 16000, "craft w/ Dull Shark Tooth Necklace & 4 blue shark teeth")
    Talisman("Fire Talisman", None, Rarity.COMMON, 17700, "blaze rod collection 5, craft w/ 9 ench blaze powder")
    Talisman("Speed Ring", "Speed Talisman", Rarity.UNCOMMON, 30400, "sugar collection 5, craft w/ 96 ench sugar & speed talisman")
    Talisman("Emerald Ring", None, Rarity.UNCOMMON, 30500, "emerald collection V, craft w/ 32 ench emeralds")
    Talisman("Fish Affinity Talisman", None, Rarity.RARE, 45000, "rare drop from the Water Hydra, which can be fished up at fishing level 19")
    Talisman("Candy Ring", "Candy Talisman", Rarity.RARE, 49600, "bought w/ Candy Talisman & 64 green candy @ fear mongerer NPC")
    Talisman("Piggy Bank", None, Rarity.UNCOMMON, 54100, "pork collection 5, craft w/ 40 ench raw pork")
    Talisman("Feather Talisman", None, Rarity.COMMON, -1, "feather collection 4, craft w/ 108 feathers")
    Talisman("Feather Ring", "Feather Talisman", Rarity.UNCOMMON, -1, "feather collection 7, craft w/ 7 ench feathers & feather talisman")
    Talisman("Feather Artifact", "Feather Ring", Rarity.RARE, 63000, "feather collection 9, craft w/ 128 ench feathers & feather ring")
    Talisman("Farmer Orb", None, Rarity.UNCOMMON, 67000, "pumpkin collection 6, craft w/ 8 ench pumpkin & 1 ench glowstone block")
    Talisman("Healing Talisman", None, Rarity.COMMON, 69100, "lily pad collection 3, craft w/ 144 lily pads")
    Talisman("Healing Ring", "Healing Talisman", Rarity.UNCOMMON, 69100, "lily pad collection 8, craft w/ 4 ench lily pads & healing talisman")
    Talisman("Rubbish Ring of Love", "Mediocre Ring of Love", Rarity.UNCOMMON, 8500, "Mediocre Ring of Love & 1 ench red mushroom block")
    Talisman("Modest Ring of Love", "Rubbish Ring of Love", Rarity.RARE, 62800, "Rubbish Ring of Love & 1 rabbit 6 potion (ench rabbit’s foot & ench glowstone block) w/ cheap or decent coffee base")
    Talisman("Intimidation Ring", "Intimidation Talisman", Rarity.UNCOMMON, 77500, "bought w/ Intimidation Talisman & 100 green candy @ fear mongerer NPC")
    Talisman("Potion Affinity Artifact", "Potion Affinity Ring", Rarity.RARE, 81000, "netherwart collection 9, craft w/ 256 ench netherwart & potion affinity ring")
    Talisman("Bat Talisman", None, Rarity.RARE, 100000, "rare drop from bats, use roofed forest island to spawn them")
    Talisman("Bat Ring", "Bat Talisman", Rarity.EPIC, 49600, "bought w/ 1 bat talisman & 64 green candy @ fear mongerer NPC")
    Talisman("Cheetah Talisman", "Lynx Talisman", Rarity.EPIC, 200000, "obtained by completing three of the 4/4 races in the Dungeon Hub, horse pet + saddle")
    Talisman("Campfire Scion Badge", "Campfire Cultist Badge", Rarity.EPIC, 82700, "Campfire Cultist Badge & 100 ench acacia logs [growth 5 mush armor at night w/ several health 5 potions to survive trial]")
    Talisman("Spider Talisman", None, Rarity.UNCOMMON, 120000, "travel to the peak of the spider’s den, kill a broodmother. The broodmother spawns exactly 1 hour after the previous broodmother has died. The only surefire way to find one is to wait up there")
    Talisman("Spider Ring", "Spider Talisman", Rarity.RARE, 3300, "tarantula slayer 1, craft w/ spider talisman & 64 tarantula web")
    Talisman("Sea Creature Artifact", "Sea Creature Ring", Rarity.RARE, 124000, "sponge collection 8, craft w/ 64 ench sponge & sea creature ring")
    Talisman("Mineral Talisman", None, Rarity.RARE, 155000, "craft w/ 9 refined minerals")
    Talisman("Sharp Shark Tooth Necklace", "Honed Shark Tooth Necklace", Rarity.EPIC, 0, "craft w/ Honed Shark Tooth Necklace & 4 tiger shark teeth")
    Talisman("Personal Compactor 4000", None, Rarity.UNCOMMON, 218000, "redstone collection 9, craft w/ 7 ench redstone blocks & a Super Compactor 3000")
    Talisman("BeastMaster Crest (Common)", None, Rarity.COMMON, 229000, "craft w/ 40 ancient claws & 4 griffin feathers")
    Talisman("Candy Artifact", "Candy Ring", Rarity.EPIC, 240000, "bought w/ Candy Ring & 32 purple candy @ fear mongerer NPC")
    Talisman("Haste Ring", None, Rarity.RARE, 247000, "cobblestone collection 9, craft w/ 256 ench cobblestone")
    Talisman("Pocket Espresso Machine", None, Rarity.COMMON, 248000, "enderman slayer 4, rare drop from tier IV voidgloom seraph")
    Talisman("Treasure Talisman", None, Rarity.RARE, 250000, "obtained via random drop from secret chests in the catacombs floor 4 and above")
    Talisman("New Year Cake Bag (empty)", None, Rarity.UNCOMMON, 250000, "can be purchased at the baker during the new year's festival")
    Talisman("Night Crystal", None, Rarity.RARE, 268000, "quartz collection 7, craft w/ 1 ench quartz block & 4 ench quartz")
    Talisman("Day Crystal", None, Rarity.RARE, 268000, "quartz collection 8, craft w/ 1 ench quartz block & 4 ench quartz")
    Talisman("Refined Ring of Love", "Modest Ring of Love", Rarity.RARE, 270000, "Modest Ring of Love & 1 ench lava bucket")
    Talisman("Bat Person Talisman", None, Rarity.COMMON, 294000, "obtained via rare drop from a Trick of Treat choice chest during the spooky festival")
    Talisman("Experience Artifact", None, Rarity.EPIC, 300000, "lapis lazuli collection 9, craft w/ 9 ench lapis blocks")
    Talisman("Classy Ring of Love", "Refined Ring of Love", Rarity.RARE, 350000, "1291 base intel (get Sighted Power, 9x Ender Monocle [4.8k coins]) Cheap Armors for Intel: Aurora or crystal with Wise Reforge, holding staff of the volcano for +150 intel, heroic jerry-chine gun. High enchanting / alch levels extremely easy and cheap to get")
    Talisman("Exquisite Ring of Love", "Classy Ring of Love", Rarity.EPIC, 310000, "Refined Ring of Love & 1 emerald blade")
    Talisman("Lucky Hoof", None, Rarity.UNCOMMON, 400000, "obtained via rare drop from Nightmares, when fishing during the spooky festival")
    Talisman("Scarf's Studies", None, Rarity.RARE, 410000, "obtained randomly in rewards chest by completing catacombs f2 w/ a score of B or higher")
    Talisman("Titanium Talisman", None, Rarity.UNCOMMON, 436000, "obtained via making 2 refined titanium in The Forge")
    Talisman("Personal Compactor 5000", "Personal Compactor 4000", Rarity.RARE, 436000, "redstone collection 11, craft w/ 14 ench redstone blocks & Personal Compactor 4000")
    Talisman("Personal Deletor 4000", None, Rarity.UNCOMMON, 450000, "iron collection 9, craft w/ 112 ench iron ingot & 1ench redstone block & 1ench lava bucket")
    Talisman("Personal Deletor 5000", "Personal Deletor 4000", Rarity.RARE, 272000, "iron collection 10, craft w/ 224 ench iron ingot & Personal Deletor 4000")
    Talisman("BeastMaster Crest (Uncommon)", "BeastMaster Crest (Common)", Rarity.UNCOMMON, 459000, "craft w/ 80 ancient claws & 8 griffin feathers & Common BeastMaster Crest")
    Talisman("Bat Artifact", "Bat Ring", Rarity.LEGENDARY, 480000, "bought w/ 1 bat ring & 64 purple candy at the spooky shop")
    Talisman("Personal Deletor 6000", "Personal Deletor 5000", Rarity.EPIC, 543000, "iron collection 11, craft w/ 448 ench iron ingot & Personal Deletor 5000")
    Talisman("Red Claw Ring", "Red Claw Talisman", Rarity.RARE, 563000, "wolf slayer 5, craft w/ Red Claw Talisman & 32 ench leather & 8 golden teeth")
    Talisman("Green Jerry Talisman", None, Rarity.UNCOMMON, 650000, "obtained via rare drop from Jerry Boxes")
    Talisman("Intimidation Artifact", "Intimidation Ring", Rarity.RARE, 750000, "bought w/ Intimidation Ring & 100 purple candy in the spooky shop")
    Talisman("Ring of Power", "Talisman of Power", Rarity.UNCOMMON, 845000, "gemstone 6, craft w/ 7 fine ruby gemstone & gemstone mixture & Talisman of Power")
    Talisman("Personal Compactor 6000", "Personal Compactor 5000", Rarity.EPIC, 872000, "redstone collection 13, craft w/ 28 ench redstone blocks & PersonalCompactor 5000")
    Talisman("Handy Blood Chalice", None, Rarity.COMMON, 1100000, "enderman slayer 5, rare drop from tier IV voidgloom seraph")
    Talisman("Wolf Talisman", None, Rarity.COMMON, 1200000, "rare drop from old wolves at the castle) (cannot be BIN’D on AH, not worth buying")
    Talisman("Wolf Ring", "Wolf Talisman", Rarity.RARE, 70000, "craft w/ Wolf talisman & Weak Wolf Catalyst & 14 ench bone [obtained by killing wolves @ spirit cave]")
    Talisman("Titanium Ring", "Titanium Talisman", Rarity.RARE, 1300000, "obtained via making 6 refined titanium & Titanium Talisman in The Forge")
    Talisman("Devour Ring", None, Rarity.RARE, 1400000, "zombie slayer 5, craft w/ 39 rev viscera & 8 ench raw salmon & 2 ench raw chicken")
    Talisman("Personal Deletor 7000", "Personal Deletor 6000", Rarity.LEGENDARY, 1400000, "iron collection 12, craft w/ 7 ench iron blocks & Personal Deletor 6000")
    Talisman("Jungle Amulet", None, Rarity.UNCOMMON, 1500000, "purchased from Odawa in the Crystal Hollows for 4 Jungle Hearts & 500 Sludge Juice")
    Talisman("Zombie Artifact", "Zombie Ring", Rarity.RARE, 1700000, "zombie slayer 7, craft w/ zombie ring & 48 rev viscera & 32 ench iron & 16 ench diamonds")
    Talisman("Personal Compactor 7000", "Personal Compactor 6000", Rarity.LEGENDARY, 1800000, "redstone collection 14, craft w/ 54 ench redstone block & Personal Compactor 6000")
    Talisman("BeastMaster Crest (Rare)", "BeastMaster Crest (Uncommon)", Rarity.RARE, 1800000, "craft w/ 256 ancient claws & 32 griffin feathers & Uncommon BeastMaster Crest")
    Talisman("Bat Person Ring", "Bat Person Talisman", Rarity.UNCOMMON, 1800000, "craft w/ Bat Person Talisman & 4 spooky shards & 32 ectoplasm")
    Talisman("Blood God Crest", None, Rarity.COMMON, 1900000, "obtained via the Pig Shop, which is available every skyblock anniversary [June 10th]")
    Talisman("Scarf's Thesis", None, Rarity.EPIC, 1900000, "craft w/ 4 Scarf’s Studies")
    Talisman("Master Skull Tier 1", None, Rarity.COMMON, -1, "250k from M1 Obsidian Chest")
    Talisman("Master Skull Tier 2", "Master Skull Tier 1", Rarity.COMMON, -1, "500k from M2 Obsidian Chest, craft w/ 4 Master Skull Tier 1")
    Talisman("Master Skull Tier 3", "Master Skull Tier 2", Rarity.UNCOMMON, 2000000, "2M from M3-M5 Obsidian Chest, craft w/ 4 Master Skull Tier 2")
    Talisman("Tarantula Talisman", None, Rarity.EPIC, 2000000, "tarantula slayer 6, drop from Tarantula Broodfather boss")
    Talisman("Speed Artifact", "Speed Ring", Rarity.RARE, 2400000, "sugar collection 8, craft w/ 48 ench sugarcane & speed ring")
    Talisman("Titanium Artifact", "Titanium Ring", Rarity.EPIC, 2600000, "obtained via making 12 refined titanium & Titanium Ring in The Forge")
    Talisman("Treasure Ring", "Treasure Talisman", Rarity.EPIC, 2800000, "craft w/ 8 Treasure Talismans")
    Talisman("Hunter Talisman", None, Rarity.UNCOMMON, 3300000, "wolf slayer 7, craft w/ 32 ench rotten flesh & 64 golden tooth")
    Talisman("Red Claw Artifact", "Red Claw Ring", Rarity.EPIC, 3400000, "wolf slayer 5, craft w/ Red Claw Ring & Red Claw Egg & 128 ench leather & 54 golden teeth")
    Talisman("Blue Jerry Talisman", "Green Jerry Talisman", Rarity.RARE, 3700000, "craft w/ 5 Green Jerry Talismans")
    Talisman("Razer-Sharp Shark Tooth Necklace", "Sharp Shark Tooth Necklace", Rarity.LEGENDARY, 3700000, "craft w/ Sharp Shark Tooth Necklace & 4 great white shark teeth")
    Talisman("Spider Artifact", "Spider Ring", Rarity.EPIC, 3800000, "tarantula slayer 7, craft w/ Spider Ring & 32 ench emerald & 32 Tarantula Silk")
    Talisman("Titanium Relic", "Titanium Artifact", Rarity.LEGENDARY, 4400000, "obtained via making 20 refined titanium & Titanium Artifact in The Forge")
    Talisman("Pulse Ring (Uncommon)", None, Rarity.UNCOMMON, 5000000, "craft w/ 256 Orb of Energy from Lava Fishing")
    Talisman("Bits Talisman", None, Rarity.RARE, 5800000, "purchased for 15k bits in the community center shop")
    Talisman("Campfire God Badge", "Campfire Scion Badge", Rarity.NONE, 3800000, "Campfire Scion Badge & 1000 ench jungle logs [mastiff armor set, mana flux power orb, silky power (9x luxurious spool @724k) to survive trial]")
    Talisman("Master Skull Tier 4", "Master Skull Tier 3", Rarity.UNCOMMON, 6000000, "8M from M5-M7 Bedrock / Obsidian Chests, craft w/ 4 Master Skull Tier 3")
    Talisman("BeastMaster Crest (Epic)", "BeastMaster Crest (Rare)", Rarity.EPIC, 7100000, "craft w/ 4 ench ancient claws & 128 griffin feathers & Rare BeastMaster Crest")
    Talisman("Bat Person Artifact", "Bat Person Ring", Rarity.RARE, 7100000, "craft w/ Bat Person Artifact & 16 spooky shards & 128 ectoplasm")
    Talisman("Eternal Hoof", "Lucky Hoof", Rarity.RARE, 7500000, "craft with Lucky Hoof & 8 soul fragments")
    Talisman("Candy Relic", "Candy Artifact", Rarity.LEGENDARY, 7700000, "bought w/ Candy Artifact & 1024 purple candy @ fear mongerer NPC")
    Talisman("Scarf's Grimoire", "Scarf's Thesis", Rarity.LEGENDARY, 8200000, "craft w/ 4 Scarf’s Thesis")
    Talisman("Auto Recombobulator", None, Rarity.LEGENDARY, 9100000, "obtained via Bedrock chest as a reward for completing the catacombs floor 7")
    Talisman("Survivor Cube", None, Rarity.RARE, 10000000, "get automatically at tarantula slayer 7")
    Talisman("New Year Cake Bag (full)", "New Year Cake Bag (empty)", Rarity.UNCOMMON, 10800000, "54 unique cakes @200k each")
    Talisman("Potato Talisman", None, Rarity.COMMON, 11000000, "rare drop from Shiny Pig during SkyBlock’s anniversary event [June 10]")
    Talisman("Hunter Ring", "Hunter Talisman", Rarity.NONE, 13700000, "wolf slayer 7, craft w/ Hunter Talisman & 265 golden teeth & 1 grizzly bait")
    Talisman("BeastMaster Crest (Legendary)", "BeastMaster Crest (Epic)", Rarity.LEGENDARY, 14300000, "craft w/ 32 ench ancient claws & 256 griffin feathers & Epic BeastMaster Crest")
    Talisman("Bait Ring", None, Rarity.RARE, 15000000, "Ink Sac collection 8, craft w/ 288 ench ink sacs")
    Talisman("Spider Atrocity", "Bait Ring", Rarity.EPIC, 8000000, "craft w/ 128 ench ink sac & 128 spiked bait & Bait Ring")
    Talisman("Recombobulator on Legendary Talismans", None, Rarity.LEG_RECOMB, 5600000, "by this point using a recomb on any legendary talisman you already have would give more mp than buying a new talisman. Don’t proceed until all Legendary talismans have been recomb’ed")
    Talisman("Recombobulator on Rare and Epic Talismans", "Recombobulator on Legendary Talismans", Rarity.RARE_EPIC_RECOMB, 5600000, "by this point using a recomb on any epic or rare talisman you already have would give more mp than buying a new talisman. Don’t proceed until all talismans Rare or better have been recomb’ed")
    Talisman("Recombobulator on Uncommon Talismans", "Recombobulator on Rare and Epic Talismans", Rarity.UNCOMMON_RECOMB, 5600000, "by this point using a recomb on any uncommon talisman you already have would give more mp than buying a new talisman. Don’t proceed until all talismans Uncommon or better have been recomb’ed")
    Talisman("Recombobulator on Common Talismans", "Recombobulator on Uncommon Talismans", Rarity.COMMON_RECOMB, 5600000, "by this point using a recomb on any talisman you already have would give more mp than buying a new talisman. Don’t proceed until all talismans have been recomb’ed, and any talisman after this point should be recomb’ed right away before getting another one")
    Talisman("Pulse Ring (Rare)", "Pulse Ring (Uncommon)", Rarity.RARE, 15000000, "combine uncommon pulse ring in an anvil with Thunder in a Bottle 3 times")
    Talisman("Purple Jerry Talisman", "Blue Jerry Talisman", Rarity.EPIC, 18200000, "craft w/ 5 Blue Jerry Talismans")
    Talisman("Jacobus Register", None, Rarity.LEGENDARY, 21500000, "Obtained avia purchasing 10 additional; accessory bag slots from Jacobus")
    Talisman("Master Skull Tier 5", "Master Skull Tier 4", Rarity.RARE, 24000000, "32M from M7 Bedrock Chest, craft w/ 4 Master Skull Tier 4")
    Talisman("Invaluable Ring of Love", "Exquisite Ring of Love", Rarity.EPIC, 25000000, "Exquisite Ring of Love & 1 flower minion")
    Talisman("Legendary Ring of Love", "Invaluable Ring of Love", Rarity.LEGENDARY, 1200000, "Invaluable Ring of Love & Cheap Tuxedo, should Buy Tux from AH and resell")
    Talisman("Soulflow Pile", None, Rarity.UNCOMMON, 32000, "enderman slayer 2, craft w/ 90 Null Spheres")
    Talisman("Soulflow Battery", "Soulflow Pile", Rarity.RARE, 1000000, "enderman slayer 5, craft w/ 8 Null Ovoids & 1 Soulflow Pile")
    Talisman("Soulflow Supercell", "Soulflow Battery", Rarity.EPIC, 25100000, "enderman slayer 7, craft w/ 192 Null Ovoids & 2 Null Atom & 1 Soulflow Battery")
    Talisman("Treasure Artifact", "Treasure Ring", Rarity.LEGENDARY, 25200000, "craft w/ 9 Treasure Rings")
    Talisman("Reaper Orb", None, Rarity.LEGENDARY, 26400000, "zombie slayer 8, craft w/ 8 Reaper Scythe")
    Talisman("Catacombs Expert Ring", None, Rarity.EPIC, 29000000, "craft w/ 24 wither catalysts")
    Talisman("Shady Ring", None, Rarity.UNCOMMON, 500000, "5 DA purchases, bought from Lucius NPC")
    Talisman("Crooked Artifact", "Shady Ring", Rarity.RARE, 2000000, "10 DA purchases, bought at Lucius NPC for 2 million coins & Shady Ring")
    Talisman("Seal of the Family", "Crooked Artifact", Rarity.EPIC, 10000000, "15 DA purchases, bought at Lucius NPC for 10 million coins & crooked artifact")
    Talisman("Bingo Talisman", None, Rarity.COMMON, 33800000, "req Bingo Rank 1, can be purchased from the Bingo Shop for 100 Bingo Points")
    Talisman("Nether Artifact", None, Rarity.EPIC, 38000000, "available for purchase at the dark auction")
    Talisman("Wither Artifact", None, Rarity.EPIC, 46000000, "available for purchase at the dark auction")
    Talisman("Wither Relic", None, Rarity.LEGENDARY, 8800000, "craft w/ Wither Artifact & 8 wither catalysts")
    Talisman("Artifact of Power (empty)", None, Rarity.RARE, 22800000, "gemstone 10, craft w/ 32 Gemstone Mixture & Ring of Power")
    Talisman("Artifact of Power (max gemstones)", "Artifact of Power (empty)", Rarity.EPIC, 53900000, "placing 1 of each perfect gemstone (minus Opal) into the guantlet")
    Talisman("Burststopper Talisman", None, Rarity.RARE, 54000000, "blaze slayer 3, craft w/ 128 Molten Powder & 6 refined titanium & 4 whipped magma cream")
    Talisman("Burststopper Artifact", "Burststopper Talisman", Rarity.EPIC, 0, "blaze slayer 7, craft w/ Burststopper Talisman & 128 Molten Powder & 80 Whipped Magma Cream")
    Talisman("Ender Artifact", None, Rarity.EPIC, 80000000, "available for purchase at the dark auction, resale on AH")
    Talisman("Ender Relic", None, Rarity.LEGENDARY, 26700000, "enderman slayer 7, craft w/ Ender Artifact & Exceedingly Rare Ender Artifact Upgrader & 96 enchanted eye of ender & 128 enchanted obsidian")
    Talisman("Golden Jerry Artifact", "Purple Jerry Talisman", Rarity.LEGENDARY, 90000000, "craft w/ 5 Purple Jerry Talismans")
    Talisman("Master Skull Tier 6", "Master Skull Tier 5", Rarity.EPIC, 96000000, "craft w/ 4 Master Skull Tier 5")
    Talisman("Pulse Ring (Epic)", "Pulse Ring (Rare)", Rarity.EPIC, 100000000, "combine uncommon pulse ring in an anvil with Thunder in a Bottle 20 times")
    Talisman("Bingo Ring", "Bingo Talisman", Rarity.UNCOMMON, 144000000, "req Bingo Rank 2, can be purchased from the Bingo Shop for 150 Bingo Points")
    Talisman("Hegemony Artifact", None, Rarity.LEG_HEGEMONY, 300000000, "obtained via the “darker auction”, which makes it only available w/ Scorpuis mayor")
    Talisman("Bingo Artifact", "Bingo Ring", Rarity.RARE, 284000000, "req Bingo Rank 3, can be purchased from the Bingo Shop for 150 Bingo Points")
    Talisman("Master Skull Tier 7", "Master Skull Tier 6", Rarity.LEGENDARY, 384000000, "craft w/ 4 Master Skull Tier 6")
    Talisman("Pulse Ring (Legendary)", "Pulse Ring (Epic)", Rarity.LEGENDARY, 500000000, "combine uncommon pulse ring in an anvil with Thunder in a Bottle 100 times")
    Talisman("name", None, Rarity.NONE, 0, "description")


if __name__ == '__main__':
    inittalismans()

    # sort talismans by from least coins per mp to most
    from functools import cmp_to_key
    talismans = sorted(talismans, key=cmp_to_key(compare))

    # shove up talisman upgrades which are less expensive than previous iteration
    # (requiring that you get the previous upgrade first)
    # TODO fix when talisman and upgrade is same cost (feather artifact, cheetah talisman,
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
        talisman.printme(counter)
        counter += 1

    print("FIXED")
    counter = 1
    for talisman in finaltalismans:
        talisman.printme(counter)
        counter += 1

    # calculatebudget(500000)