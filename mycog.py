import discord
import threading
import json
import random
import re
import time
import sqlite3
import datetime
from random import randint
from timeit import Timer
from discord.ext import commands
'''
LumScape 0.1.0 Beta

Current bugs:
When pay timer is done it does not reset after using the pay command.

ChangeLog:
0.1.0
Reworked the droptable mechanic
0.0.9
reworked combat to include many more factors
0.0.8
dev kit location added
0.0.7
expanded the fishing skill
0.0.6
expanded the smithing skill
0.0.5
dev kit additem
0.0.4
Added lots of new items
0.0.3
Changed the way multiline messages are displayed
0.0.2
Fixed item name input fields.
Added traveling
Added mining
Addes fishing
0.0.1
Fixed a bug where trading only gave resources and didn't take any.
'''

Account = []
Location = [[0]]
CombatMode = [1]
SaveTimer = [1]
LoadingError = [1]
Loaded = 0
Saved = 0
Constitution = [1]
ItemName = ["Apple"]
ItemAmount = [0]
ItemExamine = ["1"]
ItemPrice = [0]
Experience = [[0]]

Equipment = [[0]]
LocationName = [["d"]]

LocationTree = [[1]]
LocationMine= [[1]]
LocationMonster = [[1]]
LocationFish = [[0]]

LocationTrees = [[1]]
LocationMines = [[1]]
LocationMonsters = [[1]]
LocationFishs = [[0]]

MonsterName = ["Rat"]
MonsterConstitution = [50]
MonsterDefaultConstitution = [50]
MonsterAccuracy = [[100, 0, 0]]
MonsterAffinities = [[90, 55, 45, 65]]
MonsterWeakness = ["Earth spell"]
MonsterCombatExperience = [24.9]
MonsterConstitutionExperience = [8.2]
MonsterDamage = [[4, 0, 0]]
MonsterArmour = [100]
MonsterDrop = [[0]]

NPC = ["General Store"]
NPCStock = [[25]]
restarted = 0
LocationFire = [0]

def Save():
    global SaveTimer
    global Account
    global Location
    global LoadingError
    global Loaded
    global Saved
    global Constitution
    global ItemName
    global ItemAmount
    global ItemExamine
    global ItemPrice
    global Experience
    global CombatMode
    global Equipment
    global LocationName
    
    global LocationTrees
    global LocationMines
    global LocationMonsters
    global LocationFishs
    global LocationTree
    global LocationMine
    global LocationMonster
    global LocationFish

    global NPC
    global NPCStock

    global MonsterName
    global MonsterConstitution
    global MonsterDefaultConstitution
    global MonsterAccuracy
    global MonsterAffinities
    global MonsterWeakness
    global MonsterCombatExperience
    global MonsterConstitutionExperience
    global MonsterDamage
    global MonsterArmour
    global MonsterLevel
    global MonsterDrop
    global LocationFire

    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\Account.txt", "w") as outfile:
        json.dump(Account, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\Location.txt", "w") as outfile:
        json.dump(Location, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\Constitution.txt", "w") as outfile:
        json.dump(Constitution, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\ItemName.txt", "w") as outfile:
        json.dump(ItemName, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\ItemAmount.txt", "w") as outfile:
        json.dump(ItemAmount, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\ItemExamine.txt", "w") as outfile:
        json.dump(ItemExamine, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\ItemPrice.txt", "w") as outfile:
        json.dump(ItemPrice, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\Experience.txt", "w") as outfile:
        json.dump(Experience, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\CombatMode.txt", "w") as outfile:
        json.dump(CombatMode, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\Equipment.txt", "w") as outfile:
        json.dump(Equipment, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\LocationName.txt", "w") as outfile:
        json.dump(LocationName, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\LocationTree.txt", "w") as outfile:
        json.dump(LocationTree, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\LocationMine.txt", "w") as outfile:
        json.dump(LocationMine, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\LocationMonster.txt", "w") as outfile:
        json.dump(LocationMonster, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\LocationFish.txt", "w") as outfile:
        json.dump(LocationFish, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\LocationTrees.txt", "w") as outfile:
        json.dump(LocationTrees, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\LocationMines.txt", "w") as outfile:
        json.dump(LocationMines, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\LocationMonsters.txt", "w") as outfile:
        json.dump(LocationMonsters, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\LocationFishs.txt", "w") as outfile:
        json.dump(LocationFishs, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\NPC.txt", "w") as outfile:
        json.dump(NPC, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\NPCStock.txt", "w") as outfile:
        json.dump(NPCStock, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\MonsterName.txt", "w") as outfile:
        json.dump(MonsterName, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\MonsterConstitution.txt", "w") as outfile:
        json.dump(MonsterConstitution, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\MonsterDefaultConstitution.txt", "w") as outfile:
        json.dump(MonsterDefaultConstitution, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\MonsterAccuracy.txt", "w") as outfile:
        json.dump(MonsterAccuracy, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\MonsterAffinities.txt", "w") as outfile:
        json.dump(MonsterAffinities, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\MonsterWeakness.txt", "w") as outfile:
        json.dump(MonsterWeakness, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\MonsterCombatExperience.txt", "w") as outfile:
        json.dump(MonsterCombatExperience, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\MonsterConstitutionExperience.txt", "w") as outfile:
        json.dump(MonsterConstitutionExperience, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\MonsterDamage.txt", "w") as outfile:
        json.dump(MonsterDamage, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\MonsterArmour.txt", "w") as outfile:
        json.dump(MonsterArmour, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\MonsterLevel.txt", "w") as outfile:
        json.dump(MonsterLevel, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\MonsterDrop.txt", "w") as outfile:
        json.dump(MonsterDrop, outfile)
        outfile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\LocationFire.txt", "w") as outfile:
        json.dump(LocationFire, outfile)
        outfile.close()

def Load():
    global SaveTimer
    global Account
    global Location
    global LoadingError
    global Loaded
    global Saved
    global Constitution
    global ItemName
    global ItemAmount
    global ItemExamine
    global ItemPrice
    global Experience
    global CombatMode
    global Equipment
    global LocationName

    global LocationTree
    global LocationMine
    global LocationMonster
    global LocationFish
    
    global LocationTrees
    global LocationMines
    global LocationMonsters
    global LocationFishs

    global NPC
    global NPCStock

    global MonsterName
    global MonsterConstitution
    global MonsterDefaultConstitution
    global MonsterAccuracy
    global MonsterAffinities
    global MonsterWeakness
    global MonsterCombatExperience
    global MonsterConstitutionExperience
    global MonsterDamage
    global MonsterArmour
    global MonsterLevel
    global MonsterDrop
    global LocationFire
    print("Do we even run this")

    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\Account.txt", "r") as infile:
    #     Account = json.load(infile)
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\Location.txt", "r") as infile:
    #     Location = json.load(infile)
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\Constitution.txt", "r") as infile:
        Constitution = json.load(infile)
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\ItemName.txt", "r") as infile:
    #     ItemName = json.load(infile)
    #     infile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\ItemAmount.txt", "r") as infile:
        ItemAmount = json.load(infile)
        infile.close()
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\ItemExamine.txt", "r") as infile:
    #     ItemExamine = json.load(infile)
    #     infile.close()
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\ItemPrice.txt", "r") as infile:
    #     ItemPrice = json.load(infile)
    #     infile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\Experience.txt", "r") as infile:
        Experience = json.load(infile)
        infile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\CombatMode.txt", "r") as infile:
        CombatMode = json.load(infile)
        infile.close()
    with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\Equipment.txt", "r") as infile:
        Equipment = json.load(infile)
        infile.close()
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\LocationName.txt", "r") as infile:
    #     LocationName = json.load(infile)
    #     infile.close()
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\LocationTree.txt", "r") as infile:
    #     LocationTree = json.load(infile)
    #     infile.close()
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\LocationMine.txt", "r") as infile:
    #     LocationMine = json.load(infile)
    #     infile.close()
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\LocationMonster.txt", "r") as infile:
    #     LocationMonster = json.load(infile)
    #     infile.close()
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\LocationFish.txt", "r") as infile:
    #     LocationFish = json.load(infile)
    #     infile.close()
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\LocationTrees.txt", "r") as infile:
    #     LocationTrees = json.load(infile)
    #     infile.close()
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\LocationMines.txt", "r") as infile:
    #     LocationMines = json.load(infile)
    #     infile.close()
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\LocationMonsters.txt", "r") as infile:
    #     LocationMonsters = json.load(infile)
    #     infile.close()
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\LocationFishs.txt", "r") as infile:
    #     LocationFishs = json.load(infile)
    #     infile.close()
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\NPC.txt", "r") as infile:
    #     NPC = json.load(infile)
    #     infile.close()
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\NPCStock.txt", "r") as infile:
    #     NPCStock = json.load(infile)
    #     infile.close()
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\MonsterName.txt", "r") as infile:
    #     MonsterName = json.load(infile)
    #     infile.close()
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\MonsterConstitution.txt", "r") as infile:
    #     MonsterConstitution = json.load(infile)
    #     infile.close()
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\MonsterDefaultConstitution.txt", "r") as infile:
    #     MonsterDefaultConstitution = json.load(infile)
    #     infile.close()
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\MonsterAccuracy.txt", "r") as infile:
    #     MonsterAccuracy = json.load(infile)
    #     infile.close()
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\MonsterAffinities.txt", "r") as infile:
    #     MonsterAffinities = json.load(infile)
    #     infile.close()
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\MonsterWeakness.txt", "r") as infile:
    #     MonsterWeakness = json.load(infile)
    #     infile.close()
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\MonsterCombatExperience.txt", "r") as infile:
    #     MonsterCombatExperience = json.load(infile)
    #     infile.close()
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\MonsterConstitutionExperience.txt", "r") as infile:
    #     MonsterConstitutionExperience = json.load(infile)
    #     infile.close()
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\MonsterDamage.txt", "r") as infile:
    #     MonsterDamage = json.load(infile)
    #     infile.close()
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\MonsterArmour.txt", "r") as infile:
    #     MonsterArmour = json.load(infile)
    #     infile.close()
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\MonsterLevel.txt", "r") as infile:
    #     MonsterLevel = json.load(infile)
    #     infile.close()
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\MonsterDrop.txt", "r") as infile:
    #     MonsterDrop = json.load(infile)
    #     infile.close()
    # with open("C:\\Users\\Administrator\\Desktop\\Red-DiscordBot\\data\\Mycogs\\LocationFire.txt", "r") as infile:
    #     LocationFire = json.load(infile)
    #     infile.close()
    restarted = 1
    BasicStock()

conn = sqlite3.connect('LumScape.db')
f = conn.cursor()

def write_to_db():
    global Account
    global Location

    global MonsterName
    global MonsterConstitution

    global LocationName
    global LocationTree
    global LocationMine
    global LocationMonster
    global LocationFish
    global LocationFire

    global NPCStock

    name = ""

    life = 0

    tree = []
    treeoak = []
    treewillow = []
    trees = 0
    treesoak = 0
    treeswillow = 0
    minecopper = []
    minetin = []
    mineclay = []
    minescopper = []
    minestin = []
    minesclay = []
    chicken = []
    chickens = 0
    rat = []
    rats = 0
    duck = []
    ducks = 0
    spider = []
    spiders = 0
    cowcalf = []
    cowcalfs = 0
    seagull = []
    seagulls = 0
    giantspider = []
    giantspiders = 0
    goblin = []
    goblins = 0
    man = []
    mans = 0
    ram = []
    rams = 0
    woman = []
    womans = 0
    cow = []
    cows = 0
    imp = []
    imps = 0
    shrimp = []
    shrimps = 0
    crayfish = []
    crayfishs = 0
    sardine = []
    sardines = 0
    fire = []
    fires = 0

    for a in range(len(MonsterConstitution)-1):
        name = MonsterName[a]
        life = MonsterConstitution[a]
        f.execute("UPDATE monster SET life = :life WHERE name = :name", {'life': life, 'name': name})
    conn.commit()

    ###########################################################################################################################

    for a in range(len(LocationTree)):
        print(LocationTree[a])
        tree += [LocationTree[a][0]]
        treeoak += [LocationTree[a][1]]
        treewillow += [LocationTree[a][2]]
    for a in range(len(tree)-1):
        name = LocationName[a]
        trees = tree[a]
        f.execute("UPDATE location SET tree0 = :tree WHERE name = :name", {'tree': trees, 'name': name})
    conn.commit()
    for a in range(len(treeoak)-1):
        name = LocationName[a]
        treesoak = treeoak[a]
        f.execute("UPDATE location SET tree1 = :tree WHERE name = :name", {'tree': treesoak, 'name': name})
    conn.commit()
    for a in range(len(treewillow)-1):
        name = LocationName[a]
        treeswillow = treewillow[a]
        f.execute("UPDATE location SET tree2 = :tree WHERE name = :name", {'tree': treeswillow, 'name': name})
    conn.commit()

    for a in range(len(LocationMine)):
        minecopper += [LocationMine[a][0]]
        minetin += [LocationMine[a][1]]
        mineclay += [LocationMine[a][2]]
    for a in range(len(minecopper)-1):
        name = LocationName[a]
        minescopper = minecopper[a]
        f.execute("UPDATE location SET mine0 = :mine WHERE name = :name", {'mine': minescopper, 'name': name})
    conn.commit()
    for a in range(len(minetin)-1):
        name = LocationName[a]
        minestin = minetin[a]
        f.execute("UPDATE location SET mine1 = :mine WHERE name = :name", {'mine': minestin, 'name': name})
    conn.commit()
    for a in range(len(mineclay)-1):
        name = LocationName[a]
        minesclay = mineclay[a]
        f.execute("UPDATE location SET mine2 = :mine WHERE name = :name", {'mine': minesclay, 'name': name})
    conn.commit()

    for a in range(len(LocationMonster)):
        chicken += [LocationMonster[a][0]]
        rat += [LocationMonster[a][1]]
        duck += [LocationMonster[a][2]]
        spider += [LocationMonster[a][3]]
        cowcalf += [LocationMonster[a][4]]
        seagull += [LocationMonster[a][5]]
        giantspider += [LocationMonster[a][6]]
        goblin += [LocationMonster[a][7]]
        man += [LocationMonster[a][8]]
        ram += [LocationMonster[a][9]]
        woman += [LocationMonster[a][10]]
        cow += [LocationMonster[a][11]]
        imp += [LocationMonster[a][12]]
    for a in range(len(chicken)-1):
        name = LocationName[a]
        chickens = chicken[a]
        f.execute("UPDATE location SET monster0 = :monster WHERE name = :name", {'monster': chickens, 'name': name})
    conn.commit()
    for a in range(len(rat)-1):
        name = LocationName[a]
        rats = rat[a]
        f.execute("UPDATE location SET monster1 = :monster WHERE name = :name", {'monster': rats, 'name': name})
    conn.commit()
    for a in range(len(duck)-1):
        name = LocationName[a]
        ducks = duck[a]
        f.execute("UPDATE location SET monster2 = :monster WHERE name = :name", {'monster': ducks, 'name': name})
    conn.commit()
    for a in range(len(spider)-1):
        name = LocationName[a]
        spiders = spider[a]
        f.execute("UPDATE location SET monster3 = :monster WHERE name = :name", {'monster': spiders, 'name': name})
    conn.commit()
    for a in range(len(cowcalf)-1):
        name = LocationName[a]
        cowcalfs = cowcalf[a]
        f.execute("UPDATE location SET monster4 = :monster WHERE name = :name", {'monster': cowcalfs, 'name': name})
    conn.commit()
    for a in range(len(seagull)-1):
        name = LocationName[a]
        seagulls = seagull[a]
        f.execute("UPDATE location SET monster5 = :monster WHERE name = :name", {'monster': seagulls, 'name': name})
    conn.commit()
    for a in range(len(giantspider)-1):
        name = LocationName[a]
        giantspiders = giantspider[a]
        f.execute("UPDATE location SET monster6 = :monster WHERE name = :name", {'monster': giantspiders, 'name': name})
    conn.commit()
    for a in range(len(goblin)-1):
        name = LocationName[a]
        goblins = goblin[a]
        f.execute("UPDATE location SET monster7 = :monster WHERE name = :name", {'monster': goblins, 'name': name})
    conn.commit()
    for a in range(len(man)-1):
        name = LocationName[a]
        mans = man[a]
        f.execute("UPDATE location SET monster8 = :monster WHERE name = :name", {'monster': mans, 'name': name})
    conn.commit()
    for a in range(len(ram)-1):
        name = LocationName[a]
        rams = ram[a]
        f.execute("UPDATE location SET monster9 = :monster WHERE name = :name", {'monster': rams, 'name': name})
    conn.commit()
    for a in range(len(woman)-1):
        name = LocationName[a]
        womans = woman[a]
        f.execute("UPDATE location SET monster10 = :monster WHERE name = :name", {'monster': womans, 'name': name})
    conn.commit()
    for a in range(len(cow)-1):
        name = LocationName[a]
        cows = cow[a]
        f.execute("UPDATE location SET monster11 = :monster WHERE name = :name", {'monster': cows, 'name': name})
    conn.commit()
    for a in range(len(imp)-1):
        name = LocationName[a]
        imps = imp[a]
        f.execute("UPDATE location SET monster12 = :monster WHERE name = :name", {'monster': imps, 'name': name})
    conn.commit()

    for a in range(len(LocationFish)):
        crayfish += [LocationFish[a][0]]
        shrimp += [LocationFish[a][1]]
        sardine += [LocationFish[a][2]]
    for a in range(len(crayfish)-1):
        name = LocationName[a]
        crayfishs = crayfish[a]
        f.execute("UPDATE location SET fish0 = :fish WHERE name = :name", {'fish': crayfishs, 'name': name})
    conn.commit()
    for a in range(len(shrimp)-1):
        name = LocationName[a]
        shrimps = shrimp[a]
        f.execute("UPDATE location SET fish1 = :fish WHERE name = :name", {'fish': shrimps, 'name': name})
    conn.commit()
    for a in range(len(sardine)-1):
        name = LocationName[a]
        sardines = sardine[a]
        f.execute("UPDATE location SET fish2 = :fish WHERE name = :name", {'fish': sardines, 'name': name})
    conn.commit()

    for a in range(len(LocationFire)-1):
        name = MonsterName[a]
        fires = LocationFire[a]
        f.execute("UPDATE location SET fire = :fire WHERE name = :name", {'fire': fires, 'name': name})
    conn.commit()


def read_from_db():
    global Account
    global Location

    global LocationName
    global LocationTree
    global LocationTrees
    global LocationMine
    global LocationMines
    global LocationMonster
    global LocationMonsters
    global LocationFish
    global LocationFishs
    global LocationFire

    global ItemName
    global ItemAmount
    global ItemExamine
    global ItemPrice

    global MonsterName
    global MonsterDamage
    global MonsterAccuracy
    global MonsterArmour
    global MonsterLevel
    global MonsterAffinities
    global MonsterWeakness
    global MonsterConstitution
    global MonsterDefaultConstitution
    global MonsterConstitutionExperience
    global MonsterCombatExperience
    global MonsterDrop

    global NPC
    global NPCStock

    Account = []

    Location = []

    ###########################################################################################

    LocationName = []

    LocationTree = [[]]
    tree = []
    treeoak = []
    treewillow = []

    LocationTrees = [[]]
    trees = []
    treesoak = []
    treeswillow = []

    LocationMine = []
    minecopper = []
    minetin = []
    mineclay = []

    LocationMines = []
    minescopper = []
    minestin = []
    minesclay = []

    LocationMonster = []
    monsterchicken = []
    monsterrat = []
    monsterduck = []
    monsterspider = []
    monstercowcalf = []
    monsterseagull = []
    monstergiantspider = []
    monstergoblin = []
    monsterman = []
    monsterram = []
    monsterwoman = []
    monstercow = []
    monsterimp = []

    LocationMonsters = []
    monsterschicken = []
    monstersrat = []
    monstersduck = []
    monstersspider = []
    monsterscowcalf = []
    monstersseagull = []
    monstersgiantspider = []
    monstersgoblin = []
    monstersman = []
    monstersram = []
    monsterswoman = []
    monsterscow = []
    monstersimp = []

    LocationFish = []
    fishcrayfish = []
    fishshrimp = []
    fishsardine = []

    LocationFishs = []
    fishscrayfish = []
    fishsshrimp = []
    fishssardine = []

    LocationFire = []

    ##########################################

    ItemName = []

    ItemAmount = []

    ItemExamine = []

    ItemPrice = []

    ##########################################

    MonsterName = []

    MonsterDamage = [[]]
    meleedamage = []
    rangeddamage = []
    magicdamage = []

    MonsterAccuracy = [[]]
    meleeaccuracy = []
    rangedaccuracy = []
    magicaccuracy = []

    MonsterArmour = []

    MonsterLevel = []

    MonsterAffinities = [[]]
    weakness = []
    melee = []
    ranged = []
    magic = []

    MonsterWeakness = [[]]
    weaknessname = []

    MonsterConstitution = []

    MonsterDefaultConstitution = []

    MonsterConstitutionExperience = []

    MonsterCombatExperience = []

    MonsterDrop = []
    coins  = []
    bread  = []
    cheese  = []
    bronzeaxe  = []
    bronzepickaxe  = []
    copperore  = []
    tinore  = []
    bronzebar  = []
    rawshrimp  = []
    logs  = []
    bronzedagger  = []
    hammer  = []
    smallfishingnet  = []
    crayfishcage  = []
    fishingrod  = []
    fishingbait  = []
    rawcrayfish  = []
    rawsardine  = []
    clay  = []
    runeessence  = []
    ironpickaxe  = []
    ironaxe  = []
    oaklogs  = []
    willowlogs  = []
    bronzemace  = []
    bronzehelm  = []
    bronzesword  = []
    bronzescimitar  = []
    bones  = []
    rawchicken  = []
    feather  = []
    rawbeef  = []
    cowhide  = []
    wheat  = []
    emptypot  = []
    potofflour  = []
    jug  = []
    jugofwater  = []
    breaddough  = []
    cabbage  = []
    goblinmail  = []
    beer  = []
    beerglass  = []
    tinderbox  = []
    crayfish  = []
    sardine  = []
    cookedchicken  = []
    cookedmeat  = []
    shrimps  = []
    ncoins  = []
    nbread  = []
    ncheese  = []
    nbronzeaxe  = []
    nbronzepickaxe  = []
    ncopperore  = []
    ntinore  = []
    nbronzebar  = []
    nrawshrimp  = []
    nlogs  = []
    nbronzedagger  = []
    nhammer  = []
    nsmallfishingnet  = []
    ncrayfishcage  = []
    nfishingrod  = []
    nfishingbait  = []
    nrawcrayfish  = []
    nrawsardine  = []
    nclay  = []
    nruneessence  = []
    nironpickaxe  = []
    nironaxe  = []
    noaklogs  = []
    nwillowlogs  = []
    nbronzemace  = []
    nbronzehelm  = []
    nbronzesword  = []
    nbronzescimitar  = []
    nbones  = []
    nrawchicken  = []
    nfeather  = []
    nrawbeef  = []
    ncowhide  = []
    nwheat  = []
    nemptypot  = []
    npotofflour  = []
    njug  = []
    njugofwater  = []
    nbreaddough  = []
    ncabbage  = []
    ngoblinmail  = []
    nbeer  = []
    nbeerglass  = []
    ntinderbox  = []
    ncrayfish  = []
    nsardine  = []
    ncookedchicken  = []
    ncookedmeat  = []
    nshrimps  = []
    xcoins  = []
    xbread  = []
    xcheese  = []
    xbronzeaxe  = []
    xbronzepickaxe  = []
    xcopperore  = []
    xtinore  = []
    xbronzebar  = []
    xrawshrimp  = []
    xlogs  = []
    xbronzedagger  = []
    xhammer  = []
    xsmallfishingnet  = []
    xcrayfishcage  = []
    xfishingrod  = []
    xfishingbait  = []
    xrawcrayfish  = []
    xrawsardine  = []
    xclay  = []
    xruneessence  = []
    xironpickaxe  = []
    xironaxe  = []
    xoaklogs  = []
    xwillowlogs  = []
    xbronzemace  = []
    xbronzehelm  = []
    xbronzesword  = []
    xbronzescimitar  = []
    xbones  = []
    xrawchicken  = []
    xfeather  = []
    xrawbeef  = []
    xcowhide  = []
    xwheat  = []
    xemptypot  = []
    xpotofflour  = []
    xjug  = []
    xjugofwater  = []
    xbreaddough  = []
    xcabbage  = []
    xgoblinmail  = []
    xbeer  = []
    xbeerglass  = []
    xtinderbox  = []
    xcrayfish  = []
    xsardine  = []
    xcookedchicken  = []
    xcookedmeat  = []
    xshrimps  = []

    #################################################

    NPC = []
    
    NPCStock = [[]]
    scoins  = []
    sbread  = []
    scheese  = []
    sbronzeaxe  = []
    sbronzepickaxe  = []
    scopperore  = []
    stinore  = []
    sbronzebar  = []
    srawshrimp  = []
    slogs  = []
    sbronzedagger  = []
    shammer  = []
    ssmallfishingnet  = []
    scrayfishcage  = []
    sfishingrod  = []
    sfishingbait  = []
    srawcrayfish  = []
    srawsardine  = []
    sclay  = []
    sruneessence  = []
    sironpickaxe  = []
    sironaxe  = []
    soaklogs  = []
    swillowlogs  = []
    sbronzemace  = []
    sbronzehelm  = []
    sbronzesword  = []
    sbronzescimitar  = []
    sbones  = []
    srawchicken  = []
    sfeather  = []
    srawbeef  = []
    scowhide  = []
    swheat  = []
    semptypot  = []
    spotofflour  = []
    sjug  = []
    sjugofwater  = []
    sbreaddough  = []
    scabbage  = []
    sgoblinmail  = []
    sbeer  = []
    sbeerglass  = []
    stinderbox  = []
    scrayfish  = []
    ssardine  = []
    scookedchicken  = []
    scookedmeat  = []
    sshrimps  = []

    f.execute("SELECT accounts FROM user")
    for row in f.fetchall():
        Account += row

    f.execute("SELECT locations FROM user")
    for row in f.fetchall():
        Location += row

    ###########################################################################################

    f.execute("SELECT name FROM location")
    for row in f.fetchall():
        LocationName += row

    f.execute("SELECT tree0 FROM location")
    for row in f.fetchall():
        tree += row
    f.execute("SELECT tree1 FROM location")
    for row in f.fetchall():
        treeoak += row
    f.execute("SELECT tree2 FROM location")
    for row in f.fetchall():
        treewillow += row
    for a in range(len(tree)-1):
        LocationTree += [[]]
        LocationTree[a] += []
    for a in range(len(LocationTree)):
        LocationTree[a]+= [int(tree[a])]
        LocationTree[a]+= [int(treeoak[a])]
        LocationTree[a]+= [int(treewillow[a])]

    f.execute("SELECT trees0 FROM location")
    for row in f.fetchall():
        trees += row
    f.execute("SELECT trees1 FROM location")
    for row in f.fetchall():
        treesoak += row
    f.execute("SELECT trees2 FROM location")
    for row in f.fetchall():
        treeswillow += row
    for a in range(len(trees)-1):
        LocationTrees += [[]]
        LocationTrees += []
    for a in range(len(LocationTrees)):
        LocationTrees[a]+= [int(trees[a])]
        LocationTrees[a]+= [int(treesoak[a])]
        LocationTrees[a]+= [int(treeswillow[a])]

    f.execute("SELECT mine0 FROM location")
    for row in f.fetchall():
        minecopper += row
    f.execute("SELECT mine1 FROM location")
    for row in f.fetchall():
        minetin += row
    f.execute("SELECT mine2 FROM location")
    for row in f.fetchall():
        mineclay += row
    for a in range(len(minecopper)-1):
        LocationMine += [[]]
        LocationMine[a] += []
    for a in range(len(LocationMine)):
        LocationMine[a]+= [int(minecopper[a])]
        LocationMine[a]+= [int(minetin[a])]
        LocationMine[a]+= [int(mineclay[a])]

    f.execute("SELECT mines0 FROM location")
    for row in f.fetchall():
        minescopper += row
    f.execute("SELECT mines1 FROM location")
    for row in f.fetchall():
        minestin += row
    f.execute("SELECT mines2 FROM location")
    for row in f.fetchall():
        minesclay += row
    for a in range(len(minescopper)-1):
        LocationMines += [[]]
        LocationMines[a] += []
    for a in range(len(LocationMines)):
        LocationMines[a]+= [int(minescopper[a])]
        LocationMines[a]+= [int(minestin[a])]
        LocationMines[a]+= [int(minesclay[a])]

    f.execute("SELECT monster0 FROM location")
    for row in f.fetchall():
        monsterchicken += row
    f.execute("SELECT monster1 FROM location")
    for row in f.fetchall():
        monsterrat += row
    f.execute("SELECT monster2 FROM location")
    for row in f.fetchall():
        monsterduck += row
    f.execute("SELECT monster3 FROM location")
    for row in f.fetchall():
        monsterspider += row
    f.execute("SELECT monster4 FROM location")
    for row in f.fetchall():
        monstercowcalf += row
    f.execute("SELECT monster5 FROM location")
    for row in f.fetchall():
        monsterseagull += row
    f.execute("SELECT monster6 FROM location")
    for row in f.fetchall():
        monstergiantspider += row
    f.execute("SELECT monster7 FROM location")
    for row in f.fetchall():
        monstergoblin += row
    f.execute("SELECT monster8 FROM location")
    for row in f.fetchall():
        monsterman += row
    f.execute("SELECT monster9 FROM location")
    for row in f.fetchall():
        monsterram += row
    f.execute("SELECT monster10 FROM location")
    for row in f.fetchall():
        monsterwoman += row
    f.execute("SELECT monster11 FROM location")
    for row in f.fetchall():
        monstercow += row
    f.execute("SELECT monster12 FROM location")
    for row in f.fetchall():
        monsterimp += row
    for a in range(len(monsterchicken)-1):
        LocationMonster += [[]]
        LocationMonster += []
    for a in range(len(LocationMonster)):
        LocationMonster[a]+= [int(monsterchicken[a])]
        LocationMonster[a]+= [int(monsterrat[a])]
        LocationMonster[a]+= [int(monsterduck[a])]
        LocationMonster[a]+= [int(monsterspider[a])]
        LocationMonster[a]+= [int(monstercowcalf[a])]
        LocationMonster[a]+= [int(monsterseagull[a])]
        LocationMonster[a]+= [int(monstergiantspider[a])]
        LocationMonster[a]+= [int(monstergoblin[a])]
        LocationMonster[a]+= [int(monsterman[a])]
        LocationMonster[a]+= [int(monsterram[a])]
        LocationMonster[a]+= [int(monsterwoman[a])]
        LocationMonster[a]+= [int(monstercow[a])]
        LocationMonster[a]+= [int(monsterimp[a])]

    f.execute("SELECT monsters0 FROM location")
    for row in f.fetchall():
        monsterschicken += row
    f.execute("SELECT monsters1 FROM location")
    for row in f.fetchall():
        monstersrat += row
    f.execute("SELECT monsters2 FROM location")
    for row in f.fetchall():
        monstersduck += row
    f.execute("SELECT monsters3 FROM location")
    for row in f.fetchall():
        monstersspider += row
    f.execute("SELECT monsters4 FROM location")
    for row in f.fetchall():
        monsterscowcalf += row
    f.execute("SELECT monsters5 FROM location")
    for row in f.fetchall():
        monstersseagull += row
    f.execute("SELECT monsters6 FROM location")
    for row in f.fetchall():
        monstersgiantspider += row
    f.execute("SELECT monsters7 FROM location")
    for row in f.fetchall():
        monstersgoblin += row
    f.execute("SELECT monsters8 FROM location")
    for row in f.fetchall():
        monstersman += row
    f.execute("SELECT monsters9 FROM location")
    for row in f.fetchall():
        monstersram += row
    f.execute("SELECT monsters10 FROM location")
    for row in f.fetchall():
        monsterswoman += row
    f.execute("SELECT monsters11 FROM location")
    for row in f.fetchall():
        monsterscow += row
    f.execute("SELECT monsters12 FROM location")
    for row in f.fetchall():
        monstersimp += row
    for a in range(len(monsterschicken)-1):
        LocationMonsters += [[]]
        LocationMonsters[a] += []
    for a in range(len(LocationMonsters)):
        LocationMonsters[a]+= [int(monsterschicken[a])]
        LocationMonsters[a]+= [int(monstersrat[a])]
        LocationMonsters[a]+= [int(monstersduck[a])]
        LocationMonsters[a]+= [int(monstersspider[a])]
        LocationMonsters[a]+= [int(monsterscowcalf[a])]
        LocationMonsters[a]+= [int(monstersseagull[a])]
        LocationMonsters[a]+= [int(monstersgiantspider[a])]
        LocationMonsters[a]+= [int(monstersgoblin[a])]
        LocationMonsters[a]+= [int(monstersman[a])]
        LocationMonsters[a]+= [int(monstersram[a])]
        LocationMonsters[a]+= [int(monsterswoman[a])]
        LocationMonsters[a]+= [int(monsterscow[a])]
        LocationMonsters[a]+= [int(monstersimp[a])]

    f.execute("SELECT fish0 FROM location")
    for row in f.fetchall():
        fishcrayfish += row
    f.execute("SELECT fish1 FROM location")
    for row in f.fetchall():
        fishshrimp += row
    f.execute("SELECT fish2 FROM location")
    for row in f.fetchall():
        fishsardine += row
    for a in range(len(fishcrayfish)-1):
        LocationFish += [[]]
        LocationFish[a] += []
    for a in range(len(LocationFish)):
        LocationFish[a]+= [int(fishcrayfish[a])]
        LocationFish[a]+= [int(fishshrimp[a])]
        LocationFish[a]+= [int(fishsardine[a])]

    f.execute("SELECT fishs0 FROM location")
    for row in f.fetchall():
        fishscrayfish += row
    f.execute("SELECT fishs1 FROM location")
    for row in f.fetchall():
        fishsshrimp += row
    f.execute("SELECT fishs2 FROM location")
    for row in f.fetchall():
        fishssardine += row
    for a in range(len(fishscrayfish)-1):
        LocationFishs += [[]]
        LocationFishs += []
    for a in range(len(LocationFishs)):
        LocationFishs[a]+= [int(fishscrayfish[a])]
        LocationFishs[a]+= [int(fishsshrimp[a])]
        LocationFishs[a]+= [int(fishssardine[a])]

    f.execute("SELECT fire FROM location")
    for row in f.fetchall():
        LocationFire += row

    ###################################################

    f.execute("SELECT name FROM item")
    for row in f.fetchall():
        ItemName += row

    f.execute("SELECT examine FROM item")
    for row in f.fetchall():
        ItemExamine += row

    f.execute("SELECT price FROM item")
    for row in f.fetchall():
        ItemPrice += row

    ####################################################

    f.execute("SELECT name FROM monster")
    for row in f.fetchall():
        MonsterName += row

    f.execute("SELECT meleedamage FROM monster")
    for row in f.fetchall():
        meleedamage += row
    f.execute("SELECT rangeddamage FROM monster")
    for row in f.fetchall():
        rangeddamage += row
    f.execute("SELECT magicdamage FROM monster")
    for row in f.fetchall():
        magicdamage += row
    for a in range(len(meleedamage)-1):
        MonsterDamage += [[]]
        MonsterDamage[a] += []
    for a in range(len(MonsterDamage)):
        MonsterDamage[a]+= [int(meleedamage[a])]
        MonsterDamage[a]+= [int(rangeddamage[a])]
        MonsterDamage[a]+= [int(magicdamage[a])]

    f.execute("SELECT meleeaccuracy FROM monster")
    for row in f.fetchall():
        meleeaccuracy += row
    f.execute("SELECT rangedaccuracy FROM monster")
    for row in f.fetchall():
        rangedaccuracy += row
    f.execute("SELECT magicaccuracy FROM monster")
    for row in f.fetchall():
        magicaccuracy += row
    for a in range(len(meleeaccuracy)-1):
        MonsterAccuracy += [[]]
        MonsterAccuracy[a] += []
    for a in range(len(MonsterAccuracy)):
        MonsterAccuracy[a]+= [int(meleeaccuracy[a])]
        MonsterAccuracy[a]+= [int(rangedaccuracy[a])]
        MonsterAccuracy[a]+= [int(magicaccuracy[a])]

    f.execute("SELECT armour FROM monster")
    for row in f.fetchall():
        MonsterArmour += row

    f.execute("SELECT level FROM monster")
    for row in f.fetchall():
        MonsterLevel += row

    f.execute("SELECT weakness FROM monster")
    for row in f.fetchall():
        weakness += row
    f.execute("SELECT melee FROM monster")
    for row in f.fetchall():
        melee += row
    f.execute("SELECT ranged FROM monster")
    for row in f.fetchall():
        ranged += row
    f.execute("SELECT magic FROM monster")
    for row in f.fetchall():
        magic += row
    for a in range(len(weakness)-1):
        MonsterAffinities += [[]]
        MonsterAffinities[a] += []
    for a in range(len(MonsterAffinities)):
        MonsterAffinities[a]+= [int(weakness[a])]
        MonsterAffinities[a]+= [int(melee[a])]
        MonsterAffinities[a]+= [int(ranged[a])]
        MonsterAffinities[a]+= [int(magic[a])]

    f.execute("SELECT weaknessname FROM monster")
    for row in f.fetchall():
        MonsterWeakness += row

    f.execute("SELECT life FROM monster")
    for row in f.fetchall():
        MonsterConstitution += row

    f.execute("SELECT constitution FROM monster")
    for row in f.fetchall():
        MonsterDefaultConstitution += row

    f.execute("SELECT constitutionexperience FROM monster")
    for row in f.fetchall():
        MonsterConstitutionExperience += row

    f.execute("SELECT combatexperience FROM monster")
    for row in f.fetchall():
        MonsterCombatExperience += row

    f.execute("SELECT coins FROM monster")
    for row in f.fetchall():
        coins += row
    f.execute("SELECT bread FROM monster")
    for row in f.fetchall():
        bread += row
    f.execute("SELECT cheese FROM monster")
    for row in f.fetchall():
        cheese += row
    f.execute("SELECT bronzeaxe FROM monster")
    for row in f.fetchall():
        bronzeaxe += row
    f.execute("SELECT bronzepickaxe FROM monster")
    for row in f.fetchall():
        bronzepickaxe += row
    f.execute("SELECT copperore FROM monster")
    for row in f.fetchall():
        copperore += row
    f.execute("SELECT tinore FROM monster")
    for row in f.fetchall():
        tinore += row
    f.execute("SELECT bronzebar FROM monster")
    for row in f.fetchall():
        bronzebar += row
    f.execute("SELECT rawshrimp FROM monster")
    for row in f.fetchall():
        rawshrimp += row
    f.execute("SELECT logs FROM monster")
    for row in f.fetchall():
        logs += row
    f.execute("SELECT bronzedagger FROM monster")
    for row in f.fetchall():
        bronzedagger += row
    f.execute("SELECT hammer FROM monster")
    for row in f.fetchall():
        hammer += row
    f.execute("SELECT smallfishingnet FROM monster")
    for row in f.fetchall():
        smallfishingnet += row
    f.execute("SELECT crayfishcage FROM monster")
    for row in f.fetchall():
        crayfishcage += row
    f.execute("SELECT fishingrod FROM monster")
    for row in f.fetchall():
        fishingrod += row
    f.execute("SELECT fishingbait FROM monster")
    for row in f.fetchall():
        fishingbait += row
    f.execute("SELECT rawcrayfish FROM monster")
    for row in f.fetchall():
        rawcrayfish += row
    f.execute("SELECT rawsardine FROM monster")
    for row in f.fetchall():
        rawsardine += row
    f.execute("SELECT clay FROM monster")
    for row in f.fetchall():
        clay += row
    f.execute("SELECT runeessence FROM monster")
    for row in f.fetchall():
        runeessence += row
    f.execute("SELECT ironpickaxe FROM monster")
    for row in f.fetchall():
        ironpickaxe += row
    f.execute("SELECT ironaxe FROM monster")
    for row in f.fetchall():
        ironaxe += row
    f.execute("SELECT oaklogs FROM monster")
    for row in f.fetchall():
        oaklogs += row
    f.execute("SELECT willowlogs FROM monster")
    for row in f.fetchall():
        willowlogs += row
    f.execute("SELECT bronzemace FROM monster")
    for row in f.fetchall():
        bronzemace += row
    f.execute("SELECT bronzehelm FROM monster")
    for row in f.fetchall():
        bronzehelm += row
    f.execute("SELECT bronzesword FROM monster")
    for row in f.fetchall():
        bronzesword += row
    f.execute("SELECT bronzescimitar FROM monster")
    for row in f.fetchall():
        bronzescimitar += row
    f.execute("SELECT bones FROM monster")
    for row in f.fetchall():
        bones += row
    f.execute("SELECT rawchicken FROM monster")
    for row in f.fetchall():
        rawchicken += row
    f.execute("SELECT feather FROM monster")
    for row in f.fetchall():
        feather += row
    f.execute("SELECT rawbeef FROM monster")
    for row in f.fetchall():
        rawbeef += row
    f.execute("SELECT cowhide FROM monster")
    for row in f.fetchall():
        cowhide += row
    f.execute("SELECT wheat FROM monster")
    for row in f.fetchall():
        wheat += row
    f.execute("SELECT emptypot FROM monster")
    for row in f.fetchall():
        emptypot += row
    f.execute("SELECT potofflour FROM monster")
    for row in f.fetchall():
        potofflour += row
    f.execute("SELECT jug FROM monster")
    for row in f.fetchall():
        jug += row
    f.execute("SELECT jugofwater FROM monster")
    for row in f.fetchall():
        jugofwater += row
    f.execute("SELECT breaddough FROM monster")
    for row in f.fetchall():
        breaddough += row
    f.execute("SELECT cabbage FROM monster")
    for row in f.fetchall():
        cabbage += row
    f.execute("SELECT goblinmail FROM monster")
    for row in f.fetchall():
        goblinmail += row
    f.execute("SELECT beer FROM monster")
    for row in f.fetchall():
        beer += row
    f.execute("SELECT beerglass FROM monster")
    for row in f.fetchall():
        beerglass += row
    f.execute("SELECT tinderbox FROM monster")
    for row in f.fetchall():
        tinderbox += row
    f.execute("SELECT crayfish FROM monster")
    for row in f.fetchall():
        crayfish += row
    f.execute("SELECT sardine FROM monster")
    for row in f.fetchall():
        sardine += row
    f.execute("SELECT cookedchicken FROM monster")
    for row in f.fetchall():
        cookedchicken += row
    f.execute("SELECT cookedmeat FROM monster")
    for row in f.fetchall():
        cookedmeat += row
    f.execute("SELECT shrimps FROM monster")
    for row in f.fetchall():
        shrimps += row
    f.execute("SELECT ncoins FROM monster")
    for row in f.fetchall():
        ncoins += row
    f.execute("SELECT nbread FROM monster")
    for row in f.fetchall():
        nbread += row
    f.execute("SELECT ncheese FROM monster")
    for row in f.fetchall():
        ncheese += row
    f.execute("SELECT nbronzeaxe FROM monster")
    for row in f.fetchall():
        nbronzeaxe += row
    f.execute("SELECT nbronzepickaxe FROM monster")
    for row in f.fetchall():
        nbronzepickaxe += row
    f.execute("SELECT ncopperore FROM monster")
    for row in f.fetchall():
        ncopperore += row
    f.execute("SELECT ntinore FROM monster")
    for row in f.fetchall():
        ntinore += row
    f.execute("SELECT nbronzebar FROM monster")
    for row in f.fetchall():
        nbronzebar += row
    f.execute("SELECT nrawshrimp FROM monster")
    for row in f.fetchall():
        nrawshrimp += row
    f.execute("SELECT nlogs FROM monster")
    for row in f.fetchall():
        nlogs += row
    f.execute("SELECT nbronzedagger FROM monster")
    for row in f.fetchall():
        nbronzedagger += row
    f.execute("SELECT nhammer FROM monster")
    for row in f.fetchall():
        nhammer += row
    f.execute("SELECT nsmallfishingnet FROM monster")
    for row in f.fetchall():
        nsmallfishingnet += row
    f.execute("SELECT ncrayfishcage FROM monster")
    for row in f.fetchall():
        ncrayfishcage += row
    f.execute("SELECT nfishingrod FROM monster")
    for row in f.fetchall():
        nfishingrod += row
    f.execute("SELECT nfishingbait FROM monster")
    for row in f.fetchall():
        nfishingbait += row
    f.execute("SELECT nrawcrayfish FROM monster")
    for row in f.fetchall():
        nrawcrayfish += row
    f.execute("SELECT nrawsardine FROM monster")
    for row in f.fetchall():
        nrawsardine += row
    f.execute("SELECT nclay FROM monster")
    for row in f.fetchall():
        nclay += row
    f.execute("SELECT nruneessence FROM monster")
    for row in f.fetchall():
        nruneessence += row
    f.execute("SELECT nironpickaxe FROM monster")
    for row in f.fetchall():
        nironpickaxe += row
    f.execute("SELECT nironaxe FROM monster")
    for row in f.fetchall():
        nironaxe += row
    f.execute("SELECT noaklogs FROM monster")
    for row in f.fetchall():
        noaklogs += row
    f.execute("SELECT nwillowlogs FROM monster")
    for row in f.fetchall():
        nwillowlogs += row
    f.execute("SELECT nbronzemace FROM monster")
    for row in f.fetchall():
        nbronzemace += row
    f.execute("SELECT nbronzehelm FROM monster")
    for row in f.fetchall():
        nbronzehelm += row
    f.execute("SELECT nbronzesword FROM monster")
    for row in f.fetchall():
        nbronzesword += row
    f.execute("SELECT nbronzescimitar FROM monster")
    for row in f.fetchall():
        nbronzescimitar += row
    f.execute("SELECT nbones FROM monster")
    for row in f.fetchall():
        nbones += row
    f.execute("SELECT nrawchicken FROM monster")
    for row in f.fetchall():
        nrawchicken += row
    f.execute("SELECT nfeather FROM monster")
    for row in f.fetchall():
        nfeather += row
    f.execute("SELECT nrawbeef FROM monster")
    for row in f.fetchall():
        nrawbeef += row
    f.execute("SELECT ncowhide FROM monster")
    for row in f.fetchall():
        ncowhide += row
    f.execute("SELECT nwheat FROM monster")
    for row in f.fetchall():
        nwheat += row
    f.execute("SELECT nemptypot FROM monster")
    for row in f.fetchall():
        nemptypot += row
    f.execute("SELECT npotofflour FROM monster")
    for row in f.fetchall():
        npotofflour += row
    f.execute("SELECT njug FROM monster")
    for row in f.fetchall():
        njug += row
    f.execute("SELECT njugofwater FROM monster")
    for row in f.fetchall():
        njugofwater += row
    f.execute("SELECT nbreaddough FROM monster")
    for row in f.fetchall():
        nbreaddough += row
    f.execute("SELECT ncabbage FROM monster")
    for row in f.fetchall():
        ncabbage += row
    f.execute("SELECT ngoblinmail FROM monster")
    for row in f.fetchall():
        ngoblinmail += row
    f.execute("SELECT nbeer FROM monster")
    for row in f.fetchall():
        nbeer += row
    f.execute("SELECT nbeerglass FROM monster")
    for row in f.fetchall():
        nbeerglass += row
    f.execute("SELECT ntinderbox FROM monster")
    for row in f.fetchall():
        ntinderbox += row
    f.execute("SELECT ncrayfish FROM monster")
    for row in f.fetchall():
        ncrayfish += row
    f.execute("SELECT nsardine FROM monster")
    for row in f.fetchall():
        nsardine += row
    f.execute("SELECT ncookedchicken FROM monster")
    for row in f.fetchall():
        ncookedchicken += row
    f.execute("SELECT ncookedmeat FROM monster")
    for row in f.fetchall():
        ncookedmeat += row
    f.execute("SELECT nshrimps FROM monster")
    for row in f.fetchall():
        nshrimps += row
    f.execute("SELECT xcoins FROM monster")
    for row in f.fetchall():
        xcoins += row
    f.execute("SELECT xbread FROM monster")
    for row in f.fetchall():
        xbread += row
    f.execute("SELECT xcheese FROM monster")
    for row in f.fetchall():
        xcheese += row
    f.execute("SELECT xbronzeaxe FROM monster")
    for row in f.fetchall():
        xbronzeaxe += row
    f.execute("SELECT xbronzepickaxe FROM monster")
    for row in f.fetchall():
        xbronzepickaxe += row
    f.execute("SELECT xcopperore FROM monster")
    for row in f.fetchall():
        xcopperore += row
    f.execute("SELECT xtinore FROM monster")
    for row in f.fetchall():
        xtinore += row
    f.execute("SELECT xbronzebar FROM monster")
    for row in f.fetchall():
        xbronzebar += row
    f.execute("SELECT xrawshrimp FROM monster")
    for row in f.fetchall():
        xrawshrimp += row
    f.execute("SELECT xlogs FROM monster")
    for row in f.fetchall():
        xlogs += row
    f.execute("SELECT xbronzedagger FROM monster")
    for row in f.fetchall():
        xbronzedagger += row
    f.execute("SELECT xhammer FROM monster")
    for row in f.fetchall():
        xhammer += row
    f.execute("SELECT xsmallfishingnet FROM monster")
    for row in f.fetchall():
        xsmallfishingnet += row
    f.execute("SELECT xcrayfishcage FROM monster")
    for row in f.fetchall():
        xcrayfishcage += row
    f.execute("SELECT xfishingrod FROM monster")
    for row in f.fetchall():
        xfishingrod += row
    f.execute("SELECT xfishingbait FROM monster")
    for row in f.fetchall():
        xfishingbait += row
    f.execute("SELECT xrawcrayfish FROM monster")
    for row in f.fetchall():
        xrawcrayfish += row
    f.execute("SELECT xrawsardine FROM monster")
    for row in f.fetchall():
        xrawsardine += row
    f.execute("SELECT xclay FROM monster")
    for row in f.fetchall():
        xclay += row
    f.execute("SELECT xruneessence FROM monster")
    for row in f.fetchall():
        xruneessence += row
    f.execute("SELECT xironpickaxe FROM monster")
    for row in f.fetchall():
        xironpickaxe += row
    f.execute("SELECT xironaxe FROM monster")
    for row in f.fetchall():
        xironaxe += row
    f.execute("SELECT xoaklogs FROM monster")
    for row in f.fetchall():
        xoaklogs += row
    f.execute("SELECT xwillowlogs FROM monster")
    for row in f.fetchall():
        xwillowlogs += row
    f.execute("SELECT xbronzemace FROM monster")
    for row in f.fetchall():
        xbronzemace += row
    f.execute("SELECT xbronzehelm FROM monster")
    for row in f.fetchall():
        xbronzehelm += row
    f.execute("SELECT xbronzesword FROM monster")
    for row in f.fetchall():
        xbronzesword += row
    f.execute("SELECT xbronzescimitar FROM monster")
    for row in f.fetchall():
        xbronzescimitar += row
    f.execute("SELECT xbones FROM monster")
    for row in f.fetchall():
        xbones += row
    f.execute("SELECT xrawchicken FROM monster")
    for row in f.fetchall():
        xrawchicken += row
    f.execute("SELECT xfeather FROM monster")
    for row in f.fetchall():
        xfeather += row
    f.execute("SELECT xrawbeef FROM monster")
    for row in f.fetchall():
        xrawbeef += row
    f.execute("SELECT xcowhide FROM monster")
    for row in f.fetchall():
        xcowhide += row
    f.execute("SELECT xwheat FROM monster")
    for row in f.fetchall():
        xwheat += row
    f.execute("SELECT xemptypot FROM monster")
    for row in f.fetchall():
        xemptypot += row
    f.execute("SELECT xpotofflour FROM monster")
    for row in f.fetchall():
        xpotofflour += row
    f.execute("SELECT xjug FROM monster")
    for row in f.fetchall():
        xjug += row
    f.execute("SELECT xjugofwater FROM monster")
    for row in f.fetchall():
        xjugofwater += row
    f.execute("SELECT xbreaddough FROM monster")
    for row in f.fetchall():
        xbreaddough += row
    f.execute("SELECT xcabbage FROM monster")
    for row in f.fetchall():
        xcabbage += row
    f.execute("SELECT xgoblinmail FROM monster")
    for row in f.fetchall():
        xgoblinmail += row
    f.execute("SELECT xbeer FROM monster")
    for row in f.fetchall():
        xbeer += row
    f.execute("SELECT xbeerglass FROM monster")
    for row in f.fetchall():
        xbeerglass += row
    f.execute("SELECT xtinderbox FROM monster")
    for row in f.fetchall():
        xtinderbox += row
    f.execute("SELECT xcrayfish FROM monster")
    for row in f.fetchall():
        xcrayfish += row
    f.execute("SELECT xsardine FROM monster")
    for row in f.fetchall():
        xsardine += row
    f.execute("SELECT xcookedchicken FROM monster")
    for row in f.fetchall():
        xcookedchicken += row
    f.execute("SELECT xcookedmeat FROM monster")
    for row in f.fetchall():
        xcookedmeat += row
    f.execute("SELECT xshrimps FROM monster")
    for row in f.fetchall():
        xshrimps += row
    for a in range(len(coins)):
        MonsterDrop += [[[]]]
        for b in range(48):
            MonsterDrop[a] += [[]]
    for a in range(len(coins)):
        MonsterDrop[a][0]+= [int(coins[a])]
        MonsterDrop[a][0]+= [int(ncoins[a])]
        MonsterDrop[a][0]+= [int(xcoins[a])]
        MonsterDrop[a][1]+= [int(bread[a])]
        MonsterDrop[a][1]+= [int(nbread[a])]
        MonsterDrop[a][1]+= [int(xbread[a])]
        MonsterDrop[a][2]+= [int(cheese[a])]
        MonsterDrop[a][2]+= [int(ncheese[a])]
        MonsterDrop[a][2]+= [int(xcheese[a])]
        MonsterDrop[a][3]+= [int(bronzeaxe[a])]
        MonsterDrop[a][3]+= [int(nbronzeaxe[a])]
        MonsterDrop[a][3]+= [int(xbronzeaxe[a])]
        MonsterDrop[a][4]+= [int(bronzepickaxe[a])]
        MonsterDrop[a][4]+= [int(nbronzepickaxe[a])]
        MonsterDrop[a][4]+= [int(xbronzepickaxe[a])]
        MonsterDrop[a][5]+= [int(copperore[a])]
        MonsterDrop[a][5]+= [int(ncopperore[a])]
        MonsterDrop[a][5]+= [int(xcopperore[a])]
        MonsterDrop[a][6]+= [int(tinore[a])]
        MonsterDrop[a][6]+= [int(ntinore[a])]
        MonsterDrop[a][6]+= [int(xtinore[a])]
        MonsterDrop[a][7]+= [int(bronzebar[a])]
        MonsterDrop[a][7]+= [int(nbronzebar[a])]
        MonsterDrop[a][7]+= [int(xbronzebar[a])]
        MonsterDrop[a][8]+= [int(rawshrimp[a])]
        MonsterDrop[a][8]+= [int(nrawshrimp[a])]
        MonsterDrop[a][8]+= [int(xrawshrimp[a])]
        MonsterDrop[a][9]+= [int(logs[a])]
        MonsterDrop[a][9]+= [int(nlogs[a])]
        MonsterDrop[a][9]+= [int(xlogs[a])]
        MonsterDrop[a][10]+= [int(bronzedagger[a])]
        MonsterDrop[a][10]+= [int(nbronzedagger[a])]
        MonsterDrop[a][10]+= [int(xbronzedagger[a])]
        MonsterDrop[a][11]+= [int(hammer[a])]
        MonsterDrop[a][11]+= [int(nhammer[a])]
        MonsterDrop[a][11]+= [int(xhammer[a])]
        MonsterDrop[a][12]+= [int(smallfishingnet[a])]
        MonsterDrop[a][12]+= [int(nsmallfishingnet[a])]
        MonsterDrop[a][12]+= [int(xsmallfishingnet[a])]
        MonsterDrop[a][13]+= [int(crayfishcage[a])]
        MonsterDrop[a][13]+= [int(ncrayfishcage[a])]
        MonsterDrop[a][13]+= [int(xcrayfishcage[a])]
        MonsterDrop[a][14]+= [int(fishingrod[a])]
        MonsterDrop[a][14]+= [int(nfishingrod[a])]
        MonsterDrop[a][14]+= [int(xfishingrod[a])]
        MonsterDrop[a][15]+= [int(fishingbait[a])]
        MonsterDrop[a][15]+= [int(nfishingbait[a])]
        MonsterDrop[a][15]+= [int(xfishingbait[a])]
        MonsterDrop[a][16]+= [int(rawcrayfish[a])]
        MonsterDrop[a][16]+= [int(nrawcrayfish[a])]
        MonsterDrop[a][16]+= [int(xrawcrayfish[a])]
        MonsterDrop[a][17]+= [int(rawsardine[a])]
        MonsterDrop[a][17]+= [int(nrawsardine[a])]
        MonsterDrop[a][17]+= [int(xrawsardine[a])]
        MonsterDrop[a][18]+= [int(clay[a])]
        MonsterDrop[a][18]+= [int(nclay[a])]
        MonsterDrop[a][18]+= [int(xclay[a])]
        MonsterDrop[a][19]+= [int(runeessence[a])]
        MonsterDrop[a][19]+= [int(nruneessence[a])]
        MonsterDrop[a][19]+= [int(xruneessence[a])]
        MonsterDrop[a][20]+= [int(ironpickaxe[a])]
        MonsterDrop[a][20]+= [int(nironpickaxe[a])]
        MonsterDrop[a][20]+= [int(xironpickaxe[a])]
        MonsterDrop[a][21]+= [int(ironaxe[a])]
        MonsterDrop[a][21]+= [int(nironaxe[a])]
        MonsterDrop[a][21]+= [int(xironaxe[a])]
        MonsterDrop[a][22]+= [int(oaklogs[a])]
        MonsterDrop[a][22]+= [int(noaklogs[a])]
        MonsterDrop[a][22]+= [int(xoaklogs[a])]
        MonsterDrop[a][23]+= [int(willowlogs[a])]
        MonsterDrop[a][23]+= [int(nwillowlogs[a])]
        MonsterDrop[a][23]+= [int(xwillowlogs[a])]
        MonsterDrop[a][24]+= [int(bronzemace[a])]
        MonsterDrop[a][24]+= [int(nbronzemace[a])]
        MonsterDrop[a][24]+= [int(xbronzemace[a])]
        MonsterDrop[a][25]+= [int(bronzehelm[a])]
        MonsterDrop[a][25]+= [int(nbronzehelm[a])]
        MonsterDrop[a][25]+= [int(xbronzehelm[a])]
        MonsterDrop[a][26]+= [int(bronzesword[a])]
        MonsterDrop[a][26]+= [int(nbronzesword[a])]
        MonsterDrop[a][26]+= [int(xbronzesword[a])]
        MonsterDrop[a][27]+= [int(bronzescimitar[a])]
        MonsterDrop[a][27]+= [int(nbronzescimitar[a])]
        MonsterDrop[a][27]+= [int(xbronzescimitar[a])]
        MonsterDrop[a][28]+= [int(bones[a])]
        MonsterDrop[a][28]+= [int(nbones[a])]
        MonsterDrop[a][28]+= [int(xbones[a])]
        MonsterDrop[a][29]+= [int(rawchicken[a])]
        MonsterDrop[a][29]+= [int(nrawchicken[a])]
        MonsterDrop[a][29]+= [int(xrawchicken[a])]
        MonsterDrop[a][30]+= [int(feather[a])]
        MonsterDrop[a][30]+= [int(nfeather[a])]
        MonsterDrop[a][30]+= [int(xfeather[a])]
        MonsterDrop[a][31]+= [int(rawbeef[a])]
        MonsterDrop[a][31]+= [int(nrawbeef[a])]
        MonsterDrop[a][31]+= [int(xrawbeef[a])]
        MonsterDrop[a][32]+= [int(cowhide[a])]
        MonsterDrop[a][32]+= [int(ncowhide[a])]
        MonsterDrop[a][32]+= [int(xcowhide[a])]
        MonsterDrop[a][33]+= [int(wheat[a])]
        MonsterDrop[a][33]+= [int(nwheat[a])]
        MonsterDrop[a][33]+= [int(xwheat[a])]
        MonsterDrop[a][34]+= [int(emptypot[a])]
        MonsterDrop[a][34]+= [int(nemptypot[a])]
        MonsterDrop[a][34]+= [int(xemptypot[a])]
        MonsterDrop[a][35]+= [int(potofflour[a])]
        MonsterDrop[a][35]+= [int(npotofflour[a])]
        MonsterDrop[a][35]+= [int(xpotofflour[a])]
        MonsterDrop[a][36]+= [int(jug[a])]
        MonsterDrop[a][36]+= [int(njug[a])]
        MonsterDrop[a][36]+= [int(xjug[a])]
        MonsterDrop[a][37]+= [int(jugofwater[a])]
        MonsterDrop[a][37]+= [int(njugofwater[a])]
        MonsterDrop[a][37]+= [int(xjugofwater[a])]
        MonsterDrop[a][38]+= [int(breaddough[a])]
        MonsterDrop[a][38]+= [int(nbreaddough[a])]
        MonsterDrop[a][38]+= [int(xbreaddough[a])]
        MonsterDrop[a][39]+= [int(cabbage[a])]
        MonsterDrop[a][39]+= [int(ncabbage[a])]
        MonsterDrop[a][39]+= [int(xcabbage[a])]
        MonsterDrop[a][40]+= [int(goblinmail[a])]
        MonsterDrop[a][40]+= [int(ngoblinmail[a])]
        MonsterDrop[a][40]+= [int(xgoblinmail[a])]
        MonsterDrop[a][41]+= [int(beer[a])]
        MonsterDrop[a][41]+= [int(nbeer[a])]
        MonsterDrop[a][41]+= [int(xbeer[a])]
        MonsterDrop[a][42]+= [int(beerglass[a])]
        MonsterDrop[a][42]+= [int(nbeerglass[a])]
        MonsterDrop[a][42]+= [int(xbeerglass[a])]
        MonsterDrop[a][43]+= [int(tinderbox[a])]
        MonsterDrop[a][43]+= [int(ntinderbox[a])]
        MonsterDrop[a][43]+= [int(xtinderbox[a])]
        MonsterDrop[a][44]+= [int(crayfish[a])]
        MonsterDrop[a][44]+= [int(ncrayfish[a])]
        MonsterDrop[a][44]+= [int(xcrayfish[a])]
        MonsterDrop[a][45]+= [int(sardine[a])]
        MonsterDrop[a][45]+= [int(nsardine[a])]
        MonsterDrop[a][45]+= [int(xsardine[a])]
        MonsterDrop[a][46]+= [int(cookedchicken[a])]
        MonsterDrop[a][46]+= [int(ncookedchicken[a])]
        MonsterDrop[a][46]+= [int(xcookedchicken[a])]
        MonsterDrop[a][47]+= [int(cookedmeat[a])]
        MonsterDrop[a][47]+= [int(ncookedmeat[a])]
        MonsterDrop[a][47]+= [int(xcookedmeat[a])]
        MonsterDrop[a][48]+= [int(shrimps[a])]
        MonsterDrop[a][48]+= [int(nshrimps[a])]
        MonsterDrop[a][48]+= [int(xshrimps[a])]

    ###########################################################################################

    f.execute("SELECT name FROM npc")
    for row in f.fetchall():
        NPC += row

    f.execute("SELECT coins FROM npc")
    for row in f.fetchall():
        scoins += row
    f.execute("SELECT bread FROM npc")
    for row in f.fetchall():
        sbread += row
    f.execute("SELECT cheese FROM npc")
    for row in f.fetchall():
        scheese += row
    f.execute("SELECT bronzeaxe FROM npc")
    for row in f.fetchall():
        sbronzeaxe += row
    f.execute("SELECT bronzepickaxe FROM npc")
    for row in f.fetchall():
        sbronzepickaxe += row
    f.execute("SELECT copperore FROM npc")
    for row in f.fetchall():
        scopperore += row
    f.execute("SELECT tinore FROM npc")
    for row in f.fetchall():
        stinore += row
    f.execute("SELECT bronzebar FROM npc")
    for row in f.fetchall():
        sbronzebar += row
    f.execute("SELECT rawshrimp FROM npc")
    for row in f.fetchall():
        srawshrimp += row
    f.execute("SELECT logs FROM npc")
    for row in f.fetchall():
        slogs += row
    f.execute("SELECT bronzedagger FROM npc")
    for row in f.fetchall():
        sbronzedagger += row
    f.execute("SELECT hammer FROM npc")
    for row in f.fetchall():
        shammer += row
    f.execute("SELECT smallfishingnet FROM npc")
    for row in f.fetchall():
        ssmallfishingnet += row
    f.execute("SELECT crayfishcage FROM npc")
    for row in f.fetchall():
        scrayfishcage += row
    f.execute("SELECT fishingrod FROM npc")
    for row in f.fetchall():
        sfishingrod += row
    f.execute("SELECT fishingbait FROM npc")
    for row in f.fetchall():
        sfishingbait += row
    f.execute("SELECT rawcrayfish FROM npc")
    for row in f.fetchall():
        srawcrayfish += row
    f.execute("SELECT rawsardine FROM npc")
    for row in f.fetchall():
        srawsardine += row
    f.execute("SELECT clay FROM npc")
    for row in f.fetchall():
        sclay += row
    f.execute("SELECT runeessence FROM npc")
    for row in f.fetchall():
        sruneessence += row
    f.execute("SELECT ironpickaxe FROM npc")
    for row in f.fetchall():
        sironpickaxe += row
    f.execute("SELECT ironaxe FROM npc")
    for row in f.fetchall():
        sironaxe += row
    f.execute("SELECT oaklogs FROM npc")
    for row in f.fetchall():
        soaklogs += row
    f.execute("SELECT willowlogs FROM npc")
    for row in f.fetchall():
        swillowlogs += row
    f.execute("SELECT bronzemace FROM npc")
    for row in f.fetchall():
        sbronzemace += row
    f.execute("SELECT bronzehelm FROM npc")
    for row in f.fetchall():
        sbronzehelm += row
    f.execute("SELECT bronzesword FROM npc")
    for row in f.fetchall():
        sbronzesword += row
    f.execute("SELECT bronzescimitar FROM npc")
    for row in f.fetchall():
        sbronzescimitar += row
    f.execute("SELECT bones FROM npc")
    for row in f.fetchall():
        sbones += row
    f.execute("SELECT rawchicken FROM npc")
    for row in f.fetchall():
        srawchicken += row
    f.execute("SELECT feather FROM npc")
    for row in f.fetchall():
        sfeather += row
    f.execute("SELECT rawbeef FROM npc")
    for row in f.fetchall():
        srawbeef += row
    f.execute("SELECT cowhide FROM npc")
    for row in f.fetchall():
        scowhide += row
    f.execute("SELECT wheat FROM npc")
    for row in f.fetchall():
        swheat += row
    f.execute("SELECT emptypot FROM npc")
    for row in f.fetchall():
        semptypot += row
    f.execute("SELECT potofflour FROM npc")
    for row in f.fetchall():
        spotofflour += row
    f.execute("SELECT jug FROM npc")
    for row in f.fetchall():
        sjug += row
    f.execute("SELECT jugofwater FROM npc")
    for row in f.fetchall():
        sjugofwater += row
    f.execute("SELECT breaddough FROM npc")
    for row in f.fetchall():
        sbreaddough += row
    f.execute("SELECT cabbage FROM npc")
    for row in f.fetchall():
        scabbage += row
    f.execute("SELECT goblinmail FROM npc")
    for row in f.fetchall():
        sgoblinmail += row
    f.execute("SELECT beer FROM npc")
    for row in f.fetchall():
        sbeer += row
    f.execute("SELECT beerglass FROM npc")
    for row in f.fetchall():
        sbeerglass += row
    f.execute("SELECT tinderbox FROM npc")
    for row in f.fetchall():
        stinderbox += row
    f.execute("SELECT crayfish FROM npc")
    for row in f.fetchall():
        scrayfish += row
    f.execute("SELECT sardine FROM npc")
    for row in f.fetchall():
        ssardine += row
    f.execute("SELECT cookedchicken FROM npc")
    for row in f.fetchall():
        scookedchicken += row
    f.execute("SELECT cookedmeat FROM npc")
    for row in f.fetchall():
        scookedmeat += row
    f.execute("SELECT shrimps FROM npc")
    for row in f.fetchall():
        sshrimps += row
    for b in range(len(NPC)-1):
        NPCStock += []
    for a in range(len(NPC)):
        NPCStock[a] += [int(scoins[a])]
        NPCStock[a] += [int(sbread[a])]
        NPCStock[a] += [int(scheese[a])]
        NPCStock[a] += [int(sbronzeaxe[a])]
        NPCStock[a] += [int(sbronzepickaxe[a])]
        NPCStock[a] += [int(scopperore[a])]
        NPCStock[a] += [int(stinore[a])]
        NPCStock[a] += [int(sbronzebar[a])]
        NPCStock[a] += [int(srawshrimp[a])]
        NPCStock[a] += [int(slogs[a])]
        NPCStock[a] += [int(sbronzedagger[a])]
        NPCStock[a] += [int(shammer[a])]
        NPCStock[a] += [int(ssmallfishingnet[a])]
        NPCStock[a] += [int(scrayfishcage[a])]
        NPCStock[a] += [int(sfishingrod[a])]
        NPCStock[a] += [int(sfishingbait[a])]
        NPCStock[a] += [int(srawcrayfish[a])]
        NPCStock[a] += [int(srawsardine[a])]
        NPCStock[a] += [int(sclay[a])]
        NPCStock[a] += [int(sruneessence[a])]
        NPCStock[a] += [int(sironpickaxe[a])]
        NPCStock[a] += [int(sironaxe[a])]
        NPCStock[a] += [int(soaklogs[a])]
        NPCStock[a] += [int(swillowlogs[a])]
        NPCStock[a] += [int(sbronzemace[a])]
        NPCStock[a] += [int(sbronzehelm[a])]
        NPCStock[a] += [int(sbronzesword[a])]
        NPCStock[a] += [int(sbronzescimitar[a])]
        NPCStock[a] += [int(sbones[a])]
        NPCStock[a] += [int(srawchicken[a])]
        NPCStock[a] += [int(sfeather[a])]
        NPCStock[a] += [int(srawbeef[a])]
        NPCStock[a] += [int(scowhide[a])]
        NPCStock[a] += [int(swheat[a])]
        NPCStock[a] += [int(semptypot[a])]
        NPCStock[a] += [int(spotofflour[a])]
        NPCStock[a] += [int(sjug[a])]
        NPCStock[a] += [int(sjugofwater[a])]
        NPCStock[a] += [int(sbreaddough[a])]
        NPCStock[a] += [int(scabbage[a])]
        NPCStock[a] += [int(sgoblinmail[a])]
        NPCStock[a] += [int(sbeer[a])]
        NPCStock[a] += [int(sbeerglass[a])]
        NPCStock[a] += [int(stinderbox[a])]
        NPCStock[a] += [int(scrayfish[a])]
        NPCStock[a] += [int(ssardine[a])]
        NPCStock[a] += [int(scookedchicken[a])]
        NPCStock[a] += [int(scookedmeat[a])]
        NPCStock[a] += [int(sshrimps[a])]
    Load()
    print("Run this then")

TreeName = ["Tree", "Oak tree", "Willow tree"]
RockName = ["Copper ore vein", "Tin ore vein", "Clay vein ore"]
FishName = ["Crayfish", "Shrimp", "Sardine"]
LevelName = ["Constitution", "Attack", "Strength", "Ranged", "Magic", "Defence", "Fishing", "Mining", "Smithing", "Woodcutting", "Firemaking", "Cooking"]
Level = [0, 83, 174, 276, 388, 512, 650, 801, 969, 1154, 1358, 1584, 1833, 2107, 2411, 2746, 3115, 3523, 3973, 4470, 5018, 5624, 6291, 7028, 7842, 8740, 9730, 10824, 12031, 13363, 14833, 16456, 18247, 20224, 22406, 24815, 27473, 30408, 33648, 37224, 41171, 45529, 50339, 55649, 61512, 57983, 75127, 83014, 91721, 101333, 111945, 123660, 136594, 150872, 166636, 184040, 203254, 224466, 247886, 273742, 302288, 333804, 368599, 407015, 449428, 496254, 547953, 605032, 668051, 737627, 814445, 899257, 992895, 1096278, 1210421, 1336443, 1475581, 1629200, 1798808, 1986068, 2192818, 2421087, 2673114, 2951373, 3258594, 3597792, 3972294, 4385776, 4842295, 5346332, 5902831, 6517253, 7195629, 7944614, 8771558, 9684577, 10692629, 11805606, 13034431]

#Constitution and (Attack, Strength, Defence, Ranged and Magic)
MonsterDropChance = [(1,0,0,0,0,0,0,0,0,0,),(1,0,0,0,0,0,0,0,0,0,),(50,0,0,0,0,0,0,0,0,0,)]
MonsterDropAmountMin = [(0,0,0,0,0,0,0,0,0,0,),(0,0,0,0,0,0,0,0,0,0,),(1,0,0,0,0,0,0,0,0,0,)]
MonsterDropAmountMax = [(0,0,0,0,0,0,0,0,0,0,),(0,0,0,0,0,0,0,0,0,0,),(24,0,0,0,0,0,0,0,0,0,)]

EquipmentSlot = ["Helm", "Platebody", "Platelegs", "Shield", "Footwear", "Gloves", "Weapon"]
Equipable = [[25],[0],[0],[0],[0],[0],[3, 4, 10, 20, 21, 24, 26, 27]]
EquipmentType = [[[0, 4, 20, 21, 24], [0, 3, 21, 27], [0, 10, 26]], [[0], [0], [0]], [[0], [0], [0], [0]]]
EquipmentTypes = [["Crush weapon", "Slash weapon", "Stab weapon"], ["Arrows", "Bolts", "Thrown"], ["Air spell", "Earth spell", "Water spell", "Fire spell"]]
WeaponDamage = [[0],[0],[0],[0],[0],[0],[30, 29, 48, 74, 61, 48, 61, 48]]
WeaponAccuracy = [[0],[0],[0],[0],[0],[0],[110, 110, 150, 202, 202, 150, 150, 150]]
WeaponSpeed = [[0],[0],[0],[0],[0],[0],[0.7837, 0.6443, 1, 0.6443, 0.7837, 1, 0.7837, 1]]

Rock = "stone"

sender = "LIVINGDEADSOULS#7539"
receiver = "LIVINGDEADSOULS#7539"

Sitems = "coins"
Samounts = "0"

Bitems = "coins"
Bamounts = "0"

payTime = 0
mineTime = 1
fishTime = 1
cutTime = 1
smeltTime = 1
prospectTime = 1
lightTime = 1
burnTime = 1
cookTime = 1

SaveTest = 0

using = 0

def BasicStock():
    
    global ItemAmount
    global ItemName
    global Experience
    global Level
    global LevelName
    global NPC
    global NPCStock

    global LocationName
    global LocationTree
    global LocationMine
    global LocationMonster
    global LocationFish
    
    global LocationTrees
    global LocationMines
    global LocationMonsters
    global LocationFishs

    global Constitution
    
    l = 0
    i = 0
    while i < len(Constitution):
        while Experience[0][i] >= Level[l]:
            l += 1
        else:
            if Constitution[i] < l * 100:
                Constitution[i] += l*1.5
        i += 1

    a = 0
    i = 0
    while i < len(NPC) and NPC[i] != "General Store":
        i += 1
    else:
        if len(NPC) >= i:
            a = 0
            while a < len(ItemName) and ItemName[a] != "Cheese":
                a += 1
            else:
                if NPCStock[i][a] < 100:
                    NPCStock[i][a] += 1
            a = 0
            while a < len(ItemName) and ItemName[a] != "Bread":
                a += 1
            else:
                if NPCStock[i][a] < 100:
                    NPCStock[i][a] += 1
            a = 0
            while a < len(ItemName) and ItemName[a] != "Bronze axe":
                a += 1
            else:
                if NPCStock[i][a] < 1:
                    NPCStock[i][a] += 1
            a = 0
            while a < len(ItemName) and ItemName[a] != "Bronze pickaxe":
                a += 1
            else:
                if NPCStock[i][a] < 1:
                    NPCStock[i][a] += 1
            a = 0
            while a < len(ItemName) and ItemName[a] != "Hammer":
                a += 1
            else:
                if NPCStock[i][a] < 10:
                    NPCStock[i][a] += 1
            a = 0
            while a < len(ItemName) and ItemName[a] != "Iron pickaxe":
                a += 1
            else:
                if NPCStock[i][a] < 1:
                    NPCStock[i][a] += 1
            a = 0
            while a < len(ItemName) and ItemName[a] != "Iron axe":
                a += 1
            else:
                if NPCStock[i][a] < 1:
                    NPCStock[i][a] += 1
            a = 0
            while a < len(ItemName) and ItemName[a] != "Fishing rod":
                a += 1
            else:
                if NPCStock[i][a] < 1:
                   NPCStock[i][a] += 1
            a = 0
            while a < len(ItemName) and ItemName[a] != "Tinderbox":
                a += 1
            else:
                if NPCStock[i][a] < 1:
                   NPCStock[i][a] += 1
            a = 0
            while a < len(ItemName) and ItemName[a] != "Small fishing net":
                a += 1
            else:
                if NPCStock[i][a] < 1:
                   NPCStock[i][a] += 1
            a = 0
            while a < len(ItemName) and ItemName[a] != "Crayfish cage":
                a += 1
            else:
                if NPCStock[i][a] < 1:
                   NPCStock[i][a] += 1
            a = 0
            while a < len(ItemName) and ItemName[a] != "Fishing bait":
                a += 1
            else:
                if NPCStock[i][a] < 100:
                   NPCStock[i][a] += 1
            a = 0
            while a < len(ItemName) and ItemName[a] != "Empty pot":
                a += 1
            else:
                if NPCStock[i][a] < 1:
                   NPCStock[i][a] += 1
            a = 0
            while a < len(ItemName) and ItemName[a] != "Jug":
                a += 1
            else:
                if NPCStock[i][a] < 1:
                   NPCStock[i][a] += 1
    a = 0 
    b = 0
    while a < len(LocationTree):
        while b < len(LocationTree[a]) and LocationTree[a][b] < LocationTrees[a][b]:
            LocationTree[a][b] += 1
            b+= 1
        a += 1
    a = 0
    b = 0
    while a < len(LocationMine):
        while b < len(LocationMine[a]) and LocationMine[a][b] < LocationMines[a][b]:
            LocationMine[a][b] += 1
            b+= 1
        a += 1
    a = 0
    b = 0
    while a < len(LocationMonster):
        while b < len(LocationMonster[a]) and LocationMonster[a][b] < LocationMonsters[a][b]:
            LocationMonster[a][b] += 1
            b+= 1
        a += 1
    a = 0
    b = 0
    while a < len(LocationFish):
        while b < len(LocationFish[a]) and LocationFish[a][b] < LocationFishs[a][b]:
            LocationFish[a][b] += 1
            b+= 1
        a += 1
    Save()
    write_to_db()
    BasicTimer = threading.Timer(90.0, BasicStock)
    BasicTimer.start()

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def register(self, ctx,):
        
        global Account
        global Location
        global ItemName
        global ItemAmount
        global ItemPrice
        global ItemExamine
        global Equipment
        global CombatMode
        global LevelName
        global Constitution
        global LocationName
        
        author = ctx.message.author
        User = str(author)
        if str(author) in Account:
            await self.bot.say(str(author)+" account already exists")
        else:
            Constitution += [1000]
            Account += [User]
            Location += [0]
            CombatMode += [0]
            a = 0
            while a < len(Equipment):
                Equipment[a] += [0]
                a += 1
            a = 1
            Experience[0] += [1154]
            while a < len(LevelName):
                Experience[a] += [0]
                a += 1
            ItemAmount[0] += [25]
            a = 1
            while a < len(ItemAmount):
                ItemAmount[a] += [0]
                a += 1
            Information = """
Commands, Function
==========================================
register, to register an account
spot, to spot your surroundings
travel, to travel around Lumbridge
skills, to view your skills
bag, to view your inventory
examine, to examine items
trade, trade with other players
accept, to accept an incoming trade request
shop, to view the general store
buy, to buy from the general store
sell, to sell to the general store
pay, to get payed
attack, to attack targets
fish, to fish
prospect, to examine the contents of rocks
mine, to mine rocks
smelt, to smelt ore into bars
forge, to forge bars into item
cut, to cut down trees"""
            await self.bot.say(Information)
        Save()
            
    @commands.command(pass_context=True, no_pm=True)
    async def examine(self, ctx, *, item: str):
        """examine items"""
        global ItemName
        global ItemExamine
        i = 0
        while item.lower() != ItemName[i].lower() and i < len(ItemName):
            i += 1
        else:
            if i >= len(ItemName):
                await self.bot.say("That doesn't exist")
            else:
                await self.bot.say(ItemExamine[i])
        Save()

    @commands.command(pass_context=True, no_pm=True)
    async def use(self, ctx, *, item: str):
        """To use items on other items, objects or beings"""
        global Account
        global Location
        global LocationName
        global ItemName
        global ItemAmount
        global Using

        author = ctx.message.author

        i = 0
        LOC = 0
        ITE = 0
        if str(author) in Account:
            while str(author) != Account[i]:
                i += 1
            else:
                if str(author) == Account[i]:
                    while LOC < len(LocationName)-1 and Location[LOC][i] < 1:
                        LOC += 1
                    else:
                        if Location[LOC][i] > 0:
                            while ITE < len(ItemName)-1 and item.lower() != str(ItemName[ITE]).lower():
                                ITE += 1
                            else:
                                if str(ItemName[ITE]).lower() == item.lower():
                                    if ItemAmount[ITE][i] > 0:
                                        Using = ITE
                                    else:
                                        await self.bot.say("You don't have any "+item+".")
                                else:
                                    await self.bot.say(item+" doesn't exist.")
                        else:
                            await self.bot.say("Where are you?")
                else:
                    await self.bot.say("Who are you?")
        else:
            await self.bots.say("You're not registered.")
        Save()
    @commands.command(pass_context=True, no_pm=True)
    async def use(self, ctx, *, item: str):
        """To use items on other items, objects or beings"""
        global Account
        global Location
        global LocationName
        global ItemName
        global ItemAmount
        global Using

        author = ctx.message.author

        i = 0
        LOC = 0
        ITE = 0
        if str(author) in Account:
            while str(author) != Account[i]:
                i += 1
            else:
                if str(author) == Account[i]:
                    while LOC < len(LocationName)-1 and Location[LOC][i] < 1:
                        LOC += 1
                    else:
                        if Location[LOC][i] > 0:
                            while ITE < len(ItemName)-1 and item.lower() != str(ItemName[ITE]).lower():
                                ITE += 1
                            else:
                                if str(ItemName[ITE]).lower() == item.lower():
                                    if ItemAmount[ITE][i] > 0:
                                        Using = ITE
                                    else:
                                        await self.bot.say("You don't have any "+item+".")
                                else:
                                    await self.bot.say(item+" doesn't exist.")
                        else:
                            await self.bot.say("Where are you?")
                else:
                    await self.bot.say("Who are you?")
        else:
            await self.bots.say("You're not registered.")
        Save()

    @commands.command(pass_context=True, no_pm=True)
    async def travel(self, ctx, *, place: str):
        """Lumbridge Castle, Lumbridge River, Lumbridge Forest, Lumbridge Swamp, Lumbridge Furnace, Draynor Village, Draynor Manor"""

        global Account
        global Location
        global LocationName
        
        author = ctx.message.author

        i = 0
        a = 0
        b = 0
        if str(author) in Account:
            while str(author) != Account[i]:
                i += 1
            else:
                LOC = Location[i]
                if str(author) == Account[i]:
                    while b < len(LocationName)-1 and str(LocationName[b]).lower() != place.lower():
                        b+=1
                    else:
                        if str(LocationName[b]).lower() == place.lower():
                            if b == LOC:
                                await self.bot.say("Already at "+LocationName[b]+".")
                            else:
                                Location[i] = b
                                await self.bot.say("Traveling to "+LocationName[b]+".")
                        else:
                            await self.bot.say(place+" doesn't exist.")
                else:
                    await self.bot.say("Who are you?")
        else:
            await self.bot.say("You're not registered.")     
        Save()
        
    @commands.command(pass_context=True, no_pm=True)
    async def spot(self, ctx):
        """Shows the world"""
        
        global Account
        global Location
        global LocationName
        global LocationTree
        global LocationMine
        global LocationMonster
        global NPC
        global NPCStock

        global MonsterName
        global TreeName
        global ItemName

        author = ctx.message.author
        i = 0
        a = 0

        while i < len(NPC) and NPC[i] != "General Store":
            i += 1
        else:
            if i >= len(NPC):
                a = 0
                while a < len(ItemName) and ItemName[a] != "Cheese":
                    a += 1
                else:
                    if NPCStock[a][i] < 120:
                        NPCStock[a][i] += 1
        i = 0
        LOC = 0
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        if str(author) in Account:
            while str(author) != Account[i]:
                i += 1
            else:
                LOC = int(Location[i])
                if str(author) == Account[i]:
                    Report = """While looking around """+LocationName[LOC]+""" you find the following :"""
                    Report += """\nPlayers:"""
                    while a < len(Account):
                        if Location[a] == Location[i] and a != i:
                            Report += """\n"""+str(Account[a][:-5])+""" is nearby."""
                        a += 1
                    else:
                        Report += """\nMonsters:"""
                        while b < len(MonsterName):
                            if LocationMonster[LOC][b] > 0:
                                Report += """\nThere are """+str(LocationMonster[LOC][b])+""" """+MonsterName[b]+"""(s) nearby."""
                            b += 1
                        else:
                            Report += """\nTrees:"""
                            while c < len(TreeName):
                                if LocationTree[LOC][c] > 0:
                                    Report += """\nThere are """+str(LocationTree[LOC][c])+""" """+TreeName[c]+"""(s) nearby."""
                                c += 1
                            else:
                                Report += """\nRocks:"""
                                while d < len(RockName):
                                    if LocationMine[LOC][d] > 0:
                                        Report += """\nThere are """+str(LocationMine[LOC][d])+""" """+RockName[d]+"""(s) nearby."""
                                    d += 1
                                else:
                                    Report += """\nFish:"""
                                    while e < len(FishName):
                                        if LocationFish[LOC][e] > 0:
                                            Report += """\nThere are """+str(LocationFish[LOC][e])+""" """+FishName[e]+"""(s) nearby."""
                                        e += 1
                                    else:
                                        await self.bot.say(Report)
                else:
                    await self.bot.say("Who are you?")
        else:
            await self.bot.say("message sent by: "+str(author)+". list of account he should be in: "+str(Account)+".")
            await self.bot.say("You're not registered.")
        write_to_db()
        Save()
        
        
    @commands.command(pass_context=True, no_pm=True)
    async def combat(self, ctx, CombatSetting: str):
        """Combat Mode: Attack, Strength, Ranged, Magic"""

        global CombatMode
        global Account

        i = 0
        
        author = ctx.message.author
        Combat = ["attack", "strength", "ranged", "magic", "defence"]
        
        if str(author) in Account:
            while str(author) != Account[i]:
                i += 1
            else:
                if str(author) == Account[i]:
                    a = 0
                    while a < len(Combat)-1 and CombatSetting.lower() != Combat[a].lower():
                        a += 1
                    else:
                        if a >= len(Combat):
                            await self.bot.say("That doesn't exist")
                        else:
                            if CombatSetting.lower() == Combat[a].lower():
                                CombatMode[i] = a
                                await self.bot.say(Combat[a])
                            else:
                                await self.bot.say(CombatSetting+" doesn't exist.")
                else:
                    await self.bot.say("Who are you?")
        else:
            await self.bot.say("You're not registered.")
        Save()        

    @commands.command(pass_context=True, no_pm=True)
    async def eat(self, ctx, *, Food: str):
        """You can !eat bread, cheese and rawshrimp"""
        
        global Account
        global Constitution
        global Experience
        global Level
        global LevelName

        global ItemName
        global ItemAmount

        i = 0
        author = ctx.message.author
        
        if str(author) in Account:
            while str(author) != Account[i]:
                i += 1
            else:
                if str(author) == Account[i]:
                    a = 0
                    while Food.lower() != ItemName[a].lower() and a < len(ItemName):
                        a += 1
                    else:
                        if a >= len(ItemName):
                            await self.bot.say("That doesn't exist")
                        elif Food.lower() == ItemName[a].lower():
                            if ItemName[a] in ("Bread", "Cheese", "Raw Shrimp", "Raw crayfish", "Raw sardine"):
                                CL = 0 
                                while Experience[0][i] >= Level[CL]:
                                    CL += 1
                                await self.bot.say("You eat the "+Food.lower()+".")
                                await self.bot.say("It heals some health")
                                ItemAmount[a][i] -= 1
                                Constitution[i] += 100 #import healing value and edible boolean later
                                if Constitution[i] * CL > 100 * CL: #import constitution level later
                                    Constitution[i] = 100 * CL
                            else:
                                await self.bot.say("You can't eat that.")
                        else:
                            await self.bot.say(Food+" doesn't exist.")
                else:
                    await self.bot.say("Who are you?")
        else:
            await self.bot.say("You're not registered.")
        Save()
        
    @commands.command(pass_context=True, no_pm=True)
    async def shop(self, ctx):
        """Shows the Shop and its stock"""
        author = ctx.message.author

        global Account
        global Location
        global LocationName

        global ItemName
        global ItemAmount
        global ItemPrice
        global NPCStock
        global NPC

        i = 0
        a = 0
        shop = """Welcome, to the general store """+str(author)[:-5]
        shop +="""\n======================="""
        shop +="""\n#, Item, Stock, Price"""
        shop +="""\n======================="""
        while a < len(ItemName):
            if NPCStock[0][a] >= 0:
                shop += """\n"""+str(a)+""". """+ItemName[a]+""" """+str(NPCStock[0][a])+""" $"""+str(ItemPrice[a])+"""."""
            a += 1
        
        if str(author) in Account:
            while str(author) != Account[i]:
                i += 1
            else:
                if str(author) == Account[i]:
                    LOC = Location[i]
                    if LOC == 0:
                        await self.bot.say(shop)
                    else:
                        await self.bot.say("You're not in Lumbridge Castle.")
                else:
                    await self.bot.say("Who are you?")
        else:
            await self.bot.say("You're not registered.")
        Save()
            
    @commands.command(pass_context=True, no_pm=True)
    async def pay(self, ctx):
        """Spin the wheel"""
        global payTime
        global Delay

        global Account

        global ItemAmount
        global random
        
        author = ctx.message.author
        randoms = randint(0,150)

        i = 0
        
        if str(author) in Account:
            while str(author) != Account[i]:
                i += 1
            else:
                if str(author) == Account[i]:
                    if payTime < time.time():
                        ItemAmount[0][i] += randoms
                        payTime = time.time()+300
                        await self.bot.say("You won: "+str(randoms)+".")
                    else:
                        await self.bot.say("WOAH THERE, WAY TOO SPICY")
                        await self.bot.say("You're sending commands too quickly!")
                        await self.bot.say("Wait "+str(int(round(payTime-time.time(), 0)))+" more seconds.")
                else:
                    await self.bot.say("Who are you?")
        else:
            await self.bot.say("You're not registered.")
        Save()
                
    @commands.command(pass_context=True, no_pm=True)
    async def buy(self, ctx, *, sale: str):
        """Welcome to the general store.
item + amount"""

        global Account
        global Location
        global LocationName
        global NPC
        global NPCStock

        global ItemName
        global ItemAmount
     
        author = ctx.message.author

        i = 0
        a = 0

        amount = int(str(re.findall('\d+$', sale)[0]).strip())
        item = str(sale[:-len(str(amount))]).strip()

        if str(author) in Account:
            while str(author) != Account[i]:
                i += 1
            else:
                if str(author) == Account[i]:
                    while Location[a][i] < 1:
                        a += 1
                    else:
                        if LocationName[a][0] == "Lumbridge Castle":
                            a = 0
                            while item.lower() != ItemName[a].lower() and a < len(ItemName)-1:
                                a += 1
                            else:
                                if item.lower() == ItemName[a].lower():
                                    if NPCStock[a][0] - amount >= 0:
                                        total = ItemPrice[a] * amount
                                        if ItemAmount[0][i] - total >= 0:
                                
                                            NPCStock[a][0] -= amount
                                            ItemAmount[a][i] += amount
                                            
                                            ItemAmount[0][i] -= total
                                            NPCStock[0][0] += total
                                
                                            await self.bot.say("Bought "+str(amount)+" "+ItemName[a]+" for $"+str(total))
                                        else:
                                            await self.bot.say("You don't have enough coins.")
                                    else:
                                        await self.bot.say("I'm Sorry but we don't have enough in stock right now.")
                                else:
                                    await self.bot.say(item.lower()+" doesn't exist.")
                        else:
                            await self.bot.say("You're not in Lumbridge Castle.")
                else:
                    await self.bot.say("Who are you?")
        else:
            await self.bot.say("You're not registered.")
        Save()
                        
    @commands.command(pass_context=True, no_pm=True)
    async def sell(self, ctx, *, sale: str):
        """Welcome to the general store."""

        global Account
        global Location
        global LocationName
        global NPC
        global NPCStock

        global ItemName
        global ItemAmount
        global ItemPrice
     
        author = ctx.message.author
        
        amount = int(str(re.findall('\d+$', sale)[0]).strip())
        item = str(sale[:-len(str(amount))]).strip()

        i = 0
        a = 0

        if str(author) in Account:
            while str(author) != Account[i]:
                i += 1
            else:
                if str(author) == Account[i]:
                    while Location[a][i] < 1:
                        a += 1
                    else:
                        if LocationName[a][0] == "Lumbridge Castle":
                            a = 0
                            while item.lower() != ItemName[a].lower() and a < len(ItemName)-1:
                                a += 1
                            else:
                                if a >= len(ItemName):
                                    await self.bot.say("That doesn't exist")
                                elif item.lower() == ItemName[a].lower():
                                    if ItemAmount[a][i] - amount >= 0:
                                        total = round(ItemPrice[a] * 0.3 * amount)
                                
                                        NPCStock[a][0] += amount
                                        ItemAmount[a][i] -= amount
                            
                                        NPCStock[0][0] -= total
                                        ItemAmount[0][i] += total
                            
                                        await self.bot.say("Sold "+str(amount)+" "+ItemName[a]+" for $"+str(total))
                                    else:
                                        await self.bot.say("You don't have enough "+item.lower()+".")
                                else:
                                    await self.bot.say(item.lower()+" doesn't exist.")
                        else:
                            await self.bot.say("You're not in Lumbridge Castle.")
                else:
                    await self.bot.say("Who are you?")
        else:
            await self.bot.say("You're not registered.")
        Save()
                
    @commands.command(pass_context=True, no_pm=True)
    async def bag(self, ctx):
        """To search your bag"""

        global Account

        global ItemName
        global ItemAmount

        i = 0
        
        author = ctx.message.author

        if str(author) in Account:
            while str(author) != Account[i]:
                i += 1
            else:
                if str(author) == Account[i]:
                    a = 0
                    bag = """======================="""
                    bag += """\n=BackPack==============="""
                    bag += """\n======================="""
                    while a < len(ItemAmount):
                        if ItemAmount[a][i] > 0:
                            bag += """\n"""+ItemName[a]+""": """+str(ItemAmount[a][i])+"""."""
                        a += 1
                    else:
                        await self.bot.whisper(bag)
                else:
                    await self.bot.say("Who are you?")
        else:
            await self.bot.say("You're not registered.")
        Save()
        
    @commands.command(pass_context=True, no_pm=True)
    async def equipment(self, ctx):
        """To view your equipment"""

        global Account
        global Equipment

        global ItemName
        global ItemAmount
        global Equipable

        
        EquipmentSlot = ["Helm", "Platebody", "Platelegs", "Shield", "Footwear", "Gloves", "Weapon"]

        i = 0
        
        author = ctx.message.author

        if str(author) in Account:
            while str(author) != Account[i]:
                i += 1
            else:
                if str(author) == Account[i]:
                    a = 0
                    WE = """======================="""
                    WE += """\n=Worn Equipment=========="""
                    WE += """\n======================="""
                    while a < len(EquipmentSlot):
                        if Equipment[a][i] in Equipable[a]:
                            s = 0
                            while Equipment[a][i] != Equipable[a][s]:
                                s += 1
                            else:
                                if Equipable[a][s] > 0:
                                    g = Equipable[a][s]
                                    WE += """\n"""+EquipmentSlot[a]+""": """+ItemName[g]+"""."""
                        a += 1
                    else:
                        await self.bot.whisper(WE)
                else:
                    await self.bot.say("Who are you?")
        else:
            await self.bot.say("You're not registered.")
        Save()

    @commands.command(pass_context=True, no_pm=True)
    async def equip(self, ctx, *, gear: str):
        """To equip weapons and armour"""

        global Account
        global Equipment
        global ItemAmount
        global Equipable
        global ItemName
        global EquipmentSlot

        i = 0
        
        author = ctx.message.author

        if str(author) in Account:
            while str(author) != Account[i]:
                i += 1
            else:
                if str(author) == Account[i]:
                    b = 0
                    while gear.lower() != ItemName[b].lower() and b < len(ItemName):
                        b += 1
                    else:
                        if b >= len(ItemName):
                            await self.bot.say("That doesn't exist")
                        elif gear.lower() == ItemName[b].lower():
                            if ItemAmount[b][i] > 0:
                                a = 0
                                while a < len(Equipable):
                                    if a < len(Equipable) and  b in Equipable[a]:
                                        e = 0
                                        while e < len(Equipable) and Equipable[a][e] != b:
                                            e += 1
                                        else:
                                            e += 1
                                            if Equipment[a][i] in Equipable[a]:
                                                d = Equipable[a][i]
                                                ItemAmount[d][i] += 1
                                            Equipment[a][i] = b
                                            ItemAmount[b][i] -= 1
                                            await self.bot.say("You equiped a "+ItemName[b]+".")
                                            a = 9
                                    else:
                                        a += 1
                            else:
                                await self.bot.say("You don't have a "+ItemName[b]+".")
                        else:
                            await self.bot.say(gear.lower()+" doesn't exist.")
                else:
                    await self.bot.say("Who are you?")
        else:
            await self.bot.say("You're not registered.")
        Save()
        
    @commands.command(pass_context=True, no_pm=True)
    async def skills(self, ctx):
        """To view all your level and Experience"""

        global Account
        global Experience
        global Level
        global LevelName
        i = 0
        Icon = [":heart:", ":dagger:", ":muscle:", ":shield:", ":bow_and_arrow:", ":book:", ":fishing_pole_and_fish:", ":pick:", ":hammer_pick:", ":evergreen_tree:", ":fire:", ":honey_pot:"]
        CL = 0
        AL = 0
        SL = 0
        DL = 0
        RL = 0
        ML = 0
        TotalLevel = 0
        CombatLevel = 0
        author = ctx.message.author
                            
        if str(author) in Account:
            while str(author) != Account[i]:
                i += 1
            else:
                if str(author) == Account[i]:
                    s = 0
                    skill = """======================="""
                    skill += """\n=Skills=================="""
                    skill += """\n======================="""
                    while s < len(LevelName)-1:
                        l = 0
                        while Experience[s][i] >= Level[l]:
                            l += 1
                        else:
                            m = 0
                            while Experience[s+1][i] >= Level[m]:
                                m += 1
                            else:
                                if s == 0:
                                    CL = l
                                if s-1 == 1:
                                    AL = l
                                if s == 2:
                                    SL = l
                                if s-1 == 3:
                                    DL = l
                                if s == 4:
                                    RL = l
                                if s-1 == 5:
                                    ML = l
                                TotalLevel += l
                                skill += """\n"""+Icon[s]+""" """+str(l)+""": """+str(int(round(Experience[s][i], 0)))+""" """+Icon[s+1]+""" """+str(m)+""": """+str(int(round(Experience[s+1][i], 0)))+"""."""
                        s += 2
                    else:
                        CombatLevel = (13/10 * max((AL + SL),ML*2, RL*2) + DL + CL) / 4
                        skill += """\n"""
                        skill +="""\n :crossed_swords: """+str(int(CombatLevel))+""" :bar_chart: """+str(int(TotalLevel))+"""."""
                        await self.bot.whisper(skill)
                else:
                    await self.bot.say("Who are you?")
        else:
            await self.bot.say("You're not registered.")
        Save()
            
    @commands.command(pass_context=True, no_pm=True)
    async def trade(self, ctx, user : discord.Member, Sitem: str, Samount: int, Bitem: str, Bamount: int):
        """To send a trade offer to someome else."""
        
        global Account
        global Location

        global ItemName
        global ItemAmount

        global sender
        global receiver

        global Sitems
        global Bitems

        global Samounts
        global Bamounts

        Sitems = Sitem
        Bitems = Bitem

        Samounts = Samount
        Bamounts = Bamount

        author = ctx.message.author
        
        sender = str(author)
        receiver = str(user)
        x = 0
        a = 0
        if str(author) in Account:
            while str(author) != Account[x]:
                x += 1
            else:
                if str(author) == Account[x]:
                    if str(user) in Account:
                        y = 0
                        while str(user) != Account[y]:
                            y += 1
                        else:
                            if str(user) == Account[y]:
                                LOC = 0
                                while Location[LOC][x] < 1:
                                    LOC += 1
                                else:
                                    if Location[LOC][x] == Location[LOC][y]:
                                        a = 0
                                        while Sitem.lower() != ItemName[a].lower() and a < len(ItemName):
                                            a += 1
                                        else:
                                            if a >= len(ItemName):
                                                await self.bot.say("That doesn't exist")
                                            elif Sitem.lower() == ItemName[a].lower():
                                                b = 0
                                                while Bitem.lower() != ItemName[b].lower() and b < len(ItemName):
                                                    b += 1
                                                else:
                                                    if b >= len(ItemName):
                                                        await self.bot.say("That doesn't exist")
                                                    elif Bitem.lower() == ItemName[b].lower():
                                                        if ItemAmount[a][x] - Samount >= 0:
                                                            if ItemAmount[b][y] - Bamount >= 0:
                                                                await self.bot.say(user.mention +","+sender+" Wants to trade "+Sitem+" "+str(Samount)+" for "+Bitem+" "+str(Bamount)+" type !accept or !refuse in the chat.")
                                                            else:
                                                                await self.bot.say(Account[y]+" doesn't have enough "+Bitem+"(s).")
                                                        else:
                                                            await self.bot.say(Account[x]+" doesn't have enough "+Sitem+"(s).")
                                                    else:
                                                        await self.bot.say(Bitem.lower()+" doesn't exist.")
                                            else:
                                                await self.bot.say(Sitem.lower()+" doesn't exist.")
                                    else:
                                        await self.bot.say("We can't find "+Account[y][:-5]+" in "+LocationName[LOC][0]+".")
                            else:
                                await self.bot.say("Who are they?")
                    else:
                        await self.bot.say(Account[y][:-5]+" isn't registered")
                else:
                    await self.bot.say("Who are you?")
        else:
            await self.bot.say("You're not registered")
        Save()
        
    @commands.command(pass_context=True, no_pm=True)
    async def accept(self, ctx):
        """To accept trade offers"""
        
        global Account
        global Location
        global LocationName

        global ItemName
        global ItemAmount
        
        global Bamounts
        global Samounts
        
        global Bitems
        global Sitems
        
        global sender
        global receiver
        
        author = ctx.message.author

        Sitem = Sitems
        Bitem = Bitems

        Samount = Samounts
        Bamount = Bamounts
        x = 0
        if str(author) in Account:
            while str(author) != Account[x]:
                x += 1
            else:
                if str(author) == Account[x]:
                    if str(sender) in Account:
                        y = 0
                        while str(sender) != Account[y]:
                            y += 1
                        else:
                            if str(sender) == Account[y]:
                                LOC = 0
                                while Location[LOC][x] < 1:
                                    LOC += 1
                                else:
                                    if Location[LOC][x] == Location[LOC][y]:
                                        b = 0
                                        while Sitem.lower() != ItemName[b].lower() and b < len(ItemName):
                                            b += 1
                                        else:
                                            if b >= len(ItemName):
                                                await self.bot.say("That doesn't exist")
                                            elif Sitem.lower() == ItemName[b].lower():
                                                a = 0
                                                while Bitem.lower() != ItemName[a].lower() and a < len(ItemName):
                                                    a += 1
                                                else:
                                                    if b >= len(ItemName):
                                                        await self.bot.say("That doesn't exist")
                                                    elif Bitem.lower() == ItemName[a].lower():
                                                        if ItemAmount[b][x] - Samount >= 0:
                                                            if ItemAmount[a][y] - Bamount >= 0:
                                                                ItemAmount[b][x] -= int(Samount)
                                                                ItemAmount[b][y] += int(Samount)

                                                                ItemAmount[a][y] -= int(Bamount)
                                                                ItemAmount[a][x] += int(Bamount)
                                                                await self.bot.say("Transaction Completed.")
                                                            else:
                                                                await self.bot.say(Account[y]+" doesn't have enough "+Bitem+"(s).")
                                                        else:
                                                            await self.bot.say(Account[x]+" doesn't have enough "+Sitem+"(s).")
                                                    else:
                                                        await self.bot.say(Bitem.lower()+" doesn't exist.")
                                            else:
                                                await self.bot.say(Sitem.lower()+" doesn't exist.")
                                    else:
                                        await self.bot.say("We can't find "+Account[y][:-5]+" in "+LocationName[LOC][0]+".")
                            else:
                                await self.bot.say("Who are they?")
                    else:
                        await self.bot.say(Account[y][:-5]+" isn't registered.")
                else:
                    await self.bot.say("Who are you?")
        else:
            await self.bot.say("You're not registered.")
        Save()

    @commands.command(pass_context=True, no_pm=True)
    async def attack(self, ctx, *, Target: str):
        """To attack and kill targets"""

        #Still have to add combat triangle
        #make them attack you if you don't do anything

        author = ctx.message.author
        
        global Account
        global Location
        global Constitution
        global CombatMode
        global Experience
        global Level
        global LevelName
        global Equipment
        global LocationMonster

        global MonsterName
        global MonsterConstitution
        global MonsterDefaultConstitution
        global MonsterAccuracy
        global MonsterAffinities
        global MonsterWeakness
        global MonsterCombatExperience
        global MonsterConstitutionExperience
        global MonsterDamage
        global MonsterArmour
        global MonsterLevel
        global MonsterDrop

        global MonsterDrop
        global MonsterDropChance
        global MonsterDropAmountMin
        global MonsterDropAmountMax

        global ItemName
        global ItemAmount
        global Equipable
        global EquipmentSlot
        global EquipmentTypes
        global EquipmentType
        global WeaponDamage
        global WeaponAccuracy
        global WeaponSpeed
        global MonsterArmour

        global random
        
        #Fastest: 1
        #Fast: 0.7837
        #Average:0.6443
        
        DropOn = 0

        i = 0
        y = 0
        x = 0
        h = 0
        s = 0
        p = 0
        Style = 0
        Skill = 0
        Weapon = 0
        AttackType = "Stab"
        Affinity = 0
        Melee = ["Stab weapon", "Crush weapon", "Slash weapon"]
        Ranged = ["Arrow", "Bolt", "Thrown"]
        Magic = ["Air spell", "Water spell", "Earth spell", "Fire spell"]
        if str(author) in Account:
            while str(author) != Account[i]:
                i += 1
            else:
                if str(author) == Account[i]:
                    SL = 0 
                    while Experience[1][i] >= Level[SL]:
                        SL += 1
                    AL = 0
                    while Experience[2][i] >= Level[AL]:
                        AL += 1
                    while Target.lower() != MonsterName[y].lower():
                        y += 1
                    else:
                        EQ = 0
                        if Equipment[6][i] in Equipable[6]:
                            while EQ < len(Equipable[6])-1 and Equipment[6][i] != Equipable[6][EQ]:
                                EQ += 1
                            else:
                                while Skill < len(EquipmentType) and EQ not in EquipmentType[Skill-1][Style-1]:
                                    Style = 0
                                    Skill+= 1
                                    while Style < len(EquipmentType[Skill-1]) and EQ not in EquipmentType[Skill-1][Style-1]:
                                        Style += 1
                                    else:
                                        AttackType = EquipmentTypes[Skill-1][Style-1]
                                        if MonsterWeakness[y] == EquipmentTypes[Skill-1][Style-1]:
                                            Affinity = MonsterAffinities[y][0]
                                        elif AttackType in Melee:
                                            Affinity = MonsterAffinities[y][1]
                                        elif AttackType in Ranged:
                                            Affinity = MonsterAffinities[y][2]
                                        elif AttackType in Magic:
                                            Affinity = MonsterAffinities[y][3]
                                else:
                                    Accuracy = WeaponAccuracy[6][EQ] / MonsterArmour[y] * Affinity
                                    Damage = 2.5 * SL + WeaponDamage[6][EQ] * WeaponSpeed[6][EQ]
                                    LOC = 0
                                    while Location[LOC][i] < 1:
                                        LOC += 1
                                    else:
                                        if LocationMonster[LOC][y] > 0:
                                            WE ="""You attack a nearby """+MonsterName[y]+""" with your """+ItemName[Equipment[6][i]]+""" (level: """+str(MonsterLevel[y])+""")."""
                                            Hit = randint(round(int(round(Damage)) / 5), int(round(Damage)))
                                            Chance = randint(0,100)
                                            if Chance < Accuracy:
                                                MonsterConstitution[y] -= int(round(Hit, 0))
                                                WE +="""\nYou deal """+str(int(round(Hit)))+""" damage. The """+MonsterName[y]+""" has """+str(int(MonsterConstitution[y]))+""" life points left."""
                                            else:
                                                WE +=("\nYou deal 0 damage. The "+MonsterName[y]+" has "+str(int(MonsterConstitution[y]))+" life points left.")
                                            randoms = randint(0,100)
                                            Damage = randoms / 100 * MonsterDamage[y][0]
                                            randoms = randint(0,100)
                                            if randoms < MonsterAccuracy[y][0]:
                                                Constitution[i] -= int(round(Damage, 0))
                                                WE += """\nYou receive """+str(int(round(Damage)))+""" damage. You have """+str(int(Constitution[i]))+""" life points left."""
                                            else:
                                                WE +="""\nYou receive 0 damage. You have """+str(int(Constitution[i]))+""" life points left."""
                                            await self.bot.say(WE)
                                        else:
                                            await self.bot.say("There are no "+MonsterName[y]+"(s) nearby")
                                        if Constitution[i] >= 0:
                                            if MonsterConstitution[y] <= 0:
                                                await self.bot.say("You killed a "+MonsterName[y]+" (level: "+str(MonsterLevel[y])+")")
                                                LocationMonster[LOC][y] -= 1
                                                MonsterConstitution[y] = MonsterDefaultConstitution[y]
                                                Found = 0
                                                NotFound = 0
                                                for DDrop in range(len(ItemName)-1):
                                                    if int(MonsterDrop[y][DDrop][0]) == 100:
                                                        await self.bot.say("You pick up some "+ItemName[DDrop]+".")
                                                        ItemAmount[DDrop][i] += randint(MonsterDrop[y][DDrop][1], MonsterDrop[y][DDrop][2])
                                                while Found != 1 and NotFound < len(ItemName)-1:
                                                    RD = randint(0, len(ItemName)-1)
                                                    if int(MonsterDrop[y][RD][0])*10 > int(randint(0, 1000)) and MonsterDrop[y][RD][0] != 100:
                                                        ItemAmount[RD][i] += randint(MonsterDrop[y][RD][1], MonsterDrop[y][RD][2])
                                                        await self.bot.say("You pick up some "+ItemName[RD]+"(s).")
                                                        Found = 1
                                                    else:
                                                        NotFound += 1
                                                l = 0
                                                c = 0
                                                while CombatMode[i] != c:
                                                    c += 1
                                                else:
                                                    c += 1
                                                    OLDc = 0
                                                    while Experience[c][i] >= Level[OLDc]:
                                                        OLDc += 1
                                                    else:
                                                        OLD = 0
                                                        while Experience[0][i] >= Level[OLD]:
                                                            OLD += 1
                                                        else:
                                                            Experience[c][i] += MonsterConstitutionExperience[y]
                                                            Experience[0][i] += MonsterCombatExperience[y]
                                                            SL = 0
                                                            NEWc = 0
                                                            while Experience[c][i] >= Level[NEWc]:
                                                                NEWc += 1
                                                            else:
                                                                NEW = 0
                                                                while Experience[0][i] >= Level[NEW]:
                                                                    NEW += 1
                                                                else:
                                                                    if NEWc > OLDc:
                                                                        await self.bot.say("Congratulations you just gained a level in "+LevelName[c]+".")
                                                                    if NEW > OLD:
                                                                        await self.bot.say("Congratulations you just gained a level in "+LevelName[0]+".")
                                        else:
                                            await self.bot.say("You died and lost your bag")
                                            Constitution[i] = 100
                                            Location[i] = "Lumbridge Castle"
                                            d = 0
                                            while d < len(ItemName):
                                                ItemAmount[d][i] = 0
                                                d +=1
                else:
                    await self.bot.say("Who are you?")
        else:
            await self.bot.say("You're not registered")
        Save()
        
    @commands.command(pass_context=True, no_pm=True)
    async def fish(self, ctx, *, tool: str):
        """To fish insert the tool you want to use."""

        author = ctx.message.author
        
        global Account
        global Location
        global LocationFish
        global ItemAmount
        global Experience
        
        global ItemName
        global Level
        global LevelName
        global Experience

        global fishTime
        i = 0
        Q = 0
        X = ""
        STOP = 0
        author = ctx.message.author
        if fishTime < time.time():
            if str(author) in Account:
                while str(author) != Account[i]:
                    i += 1
                else:
                    if str(author) == Account[i]:
                        b = 0
                        while b < len(ItemName) and tool.lower() != ItemName[b].lower():
                            b += 1
                        else:
                            if b >= len(ItemName):
                                await self.bot.say("That doesn't exist")
                            elif tool.lower() == ItemName[b].lower():
                                l = 0
                                while Experience[3][i] >= Level[l]:
                                    l += 1
                                else:
                                    z = 0
                                    LOC = 0
                                    while Location[LOC][i] < 1:
                                        LOC += 1
                                    else:
                                        if b == 12:
                                            E = 10
                                            O = "You cast out your net..."
                                            T = "You catch some shrimps."
                                            R = 8
                                            F = 1
                                            H = 1
                                        if b == 13:
                                            E = 10
                                            O = "You attempt to catch a crayfish"
                                            T = "You catch a crayfish"
                                            R = 16
                                            F = 1
                                            H = 0
                                        if b == 14:
                                            E = 20
                                            O = "You cast out your line..."
                                            T = "You catch a sardine."
                                            X = "You attempt to catch a fish."
                                            R = 17
                                            Q = 1
                                            F = 5
                                            H = 2
                                        if R > 1:
                                            await self.bot.say(tool)
                                            if LocationFish[LOC][H] >= Location[LOC][i]:
                                                if ItemAmount[b][i] > 0:
                                                    if b == 14:
                                                        if ItemAmount[15][i] <= 0:
                                                            STOP = 1
                                                    if STOP != 1:
                                                        if l >= F:
                                                            randoms = randint(0,100)
                                                            await self.bot.say(O)
                                                            if len(X) > 0:
                                                                await self.bot.say(X)
                                                            if 25 > randoms:
                                                                fishTime = time.time()+5
                                                            else:
                                                                ItemAmount[Q][i] -= 1
                                                                ItemAmount[R][i] += 1
                                                                OLD = 0
                                                                while Experience[6][i] >= Level[OLD]:
                                                                    OLD += 1
                                                                else:
                                                                    Experience[6][i] += E
                                                                    NEW = 0
                                                                    while Experience[6][i] >= Level[NEW]:
                                                                        NEW += 1
                                                                    else:
                                                                        if NEW > OLD:
                                                                            await self.bot.say("Congratulations, you just advanced a "+LevelName[6]+" level.")
                                                                            await self.bot.say("Your "+LevelName[6]+" level is now "+str(NEW)+".")
                                                                LocationFish[LOC][H] -= 1
                                                                await self.bot.say(T)
                                                                fishTime = 0
                                                                Delay = 5
                                                        else:
                                                            await self.bot.say("You're not a high enough level to use a "+ItemName[b]+".")
                                                    else:
                                                        await self.bot.say("You don't have enough "+ItemName[15]+".")
                                                else:
                                                    await self.bot.say("You don't have a "+ItemName[b]+".")
                                            else:
                                                await self.bot.say("You're not at a "+ItemName[b]+" fishing spot.")
                                        else:
                                            await self.bot.say(ItemName[b]+" doesn't exist.")
                            else:
                                await self.bot.say(ItemName[b]+" doesn't exist.")
                    else:
                        await self.bot.say("Who.")
            else:
                await self.bot.say("You're not registered.")
        else:
            await self.bot.say("You're tired and have to wait "+str(int(round(fishTime-time.time(), 0)))+" more seconds to fish another fish.")
        Save()
            
    
            
    @commands.command(pass_context=True, no_pm=True)
    async def mine(self, ctx, *, Rock: str):
        """To mine Rocks"""
        
        global Account
        global Location
        global LocationMine
        global Level
        global LevelName
        global Experience
        
        global ItemName
        global ItemAmount

        global Equipment
        
        global mineTime

        i = 0
        R = 0
        J = 0
        P = 0
        author = ctx.message.author

        if str(author) in Account:
            while str(author) != Account[i]:
                i += 1
            else:
                if str(author) == Account[i]:
                    while Location[P][i] < 1:
                        P += 1
                    else:
                        if Rock.lower() == str(ItemName[5]).lower():
                            R = 0
                            J = 1
                            E = 17.5
                            G = 5
                        elif Rock.lower() == ItemName[6].lower():
                            R = 1
                            J = 1
                            E = 17.5
                            G = 6
                        elif Rock.lower() == ItemName[18].lower():
                            R = 2
                            J = 1
                            E = 5
                            G = 18
                        if J >= 1:
                            if LocationMine[P][R] > 0:
                                l = 0
                                while Experience[4][i] >= Level[l]:
                                    l += 1
                                else:
                                    s = 0
                                    if Equipment[6][i] == 4 or ItemAmount[4][i] > 0:
                                        s = 4
                                        V = 1
                                    else:
                                        if Equipment[6][i] == 20 or ItemAmount[20][i] > 0:
                                            s = 20
                                            V =1 
                                    if s != 0:
                                        if mineTime < time.time():
                                            if l >= J:
                                                if l >= V:
                                                    await self.bot.say("You swing your pick at the rock.")
                                                    await self.bot.say("You manage to mine some "+Rock.lower()+".")
                                                    ItemAmount[G][i] += 1
                                                    LocationMine[P][R] -= 1
                                                    OLD = 0
                                                    while Experience[7][i] >= Level[OLD]:
                                                        OLD += 1
                                                    else:
                                                        Experience[7][i] += E
                                                        NEW = 0
                                                        while Experience[7][i] >= Level[NEW]:
                                                            NEW += 1
                                                        else:
                                                            if NEW > OLD:
                                                                await self.bot.say("Congratulations, you just advanced a "+LevelName[7]+" level.")
                                                                await self.bot.say("Your "+LevelName[7]+" level is now "+str(NEW)+".")
                                                    mineTime = time.time()+5
                                                else:
                                                    await self.bot.say("You're not a high enough level to mine with a "+ItemName[s]+".")
                                            else:
                                                await self.bot.say("You're not a high enough level to mine "+ItemName[G]+".")
                                        else:
                                            await self.bot.say("You're tired and have to wait "+str(int(round(mineTime-time.time(), 0)))+" more seconds to mine another ore.")
                                    else:
                                        await self.bot.say("You don't have a pickaxe")
                            else:
                                await self.bot.say("There are no rocks left in "+LocationName[P][0])
                        else:
                            await self.bot.say("What are you trying to mine?")
                else:
                    await self.bot.say("Who are you?")
        else:
            await self.bot.say("You're not registered")


        Save()
        
    @commands.command(pass_context=True, no_pm=True)
    async def smelt(self, ctx, *, bar: str):
        """To smelt ore into bars"""
        
        global Account
        global Location
        global Experience
        global Level
        global LevelName

        global ItemName
        global ItemAmount

        global smeltTime

        bars = ["Bronze bar"]

        i = 0
        
        author = ctx.message.author

        if str(author) in Account:
            while str(author) != Account[i]:
                i += 1
            else:
                if str(author) == Account[i]:
                    P = 0
                    while Location[P][i] < 1:
                        P += 1
                    else:
                        if LocationName[P][0] == "Lumbridge Furnace":
                            l = 0
                            while Experience[5][i] >= Level[l]:
                                l += 1
                            else:
                                if smeltTime < time.time():
                                    if l >= 1:
                                        a = 0
                                        while a <len(ItemName)-1 and bar.lower() != ItemName[a].lower():
                                            a += 1
                                        else:
                                            if bar.lower() == ItemName[a].lower():
                                                if bar.lower() in str(bars).lower():
                                                    if ItemAmount[5][i] > 0 and ItemAmount[6][i] > 0:
                                                        ItemAmount[5][i] -= 1
                                                        ItemAmount[6][i] -= 1
                                                        ItemAmount[7][i] += 1
                                                        smeltTime = time.time()+5
                                                        OLD = 0
                                                        while Experience[8][i] >= Level[OLD]:
                                                            OLD += 1
                                                        else:
                                                            Experience[8][i] += 6.2
                                                            NEW = 0
                                                            while Experience[8][i] >= Level[NEW]:
                                                                NEW += 1
                                                            else:
                                                                if NEW > OLD:
                                                                    await self.bot.say("Congratulations, you just advanced a "+LevelName[8]+" level.")
                                                                    await self.bot.say("Your "+LevelName[8]+" level is now "+str(NEW)+".")
                                                        await self.bot.say("You smelt the copper and tin in the furnace.")
                                                        await self.bot.say("You retrieve a bar of "+bar[:-3].lower()+".")
                                                        Delay == 3
                                                    else:            
                                                        await self.bot.say("You don't have enough resources.")
                                                else:
                                                    await self.bot.say(bar.lower()+" isn't a bar")
                                            else:
                                                await self.bot.say(bar.lower()+" doesn't exist")
                                    else:
                                        await self.bot.say("You're not a high enough level to smelt "+bar[:-3].lower()+"(s).")
                                else:
                                    await self.bot.say("You're tired and have to wait "+str(int(round(smeltTime-time.time(), 0)))+" more seconds to smelt another bar.")
                        else:
                            await self.bot.say("You're not at a furnace.")
                else:
                    await self.bot.say("Who the fuck are you.")
        else:
            await self.bot.say("You're not registered.")
        Save()
        
    @commands.command(pass_context=True, no_pm=True)
    async def forge(self, ctx, *, item: str):
        """To forge bars into gear"""
        
        global Account
        global Location
        global LocationName
        global Experience
        global Level
        global LevelName

        global ItemName
        global ItemAmount

        global smeltTime
        forge = ["Bronze dagger", "Bronze axe", "Bronze mace", "Bronze helm", "Bronze sword", "Bronze scimitar"]

        i = 0
        B = 7
        R = 0
        E = 0
        G = 0
        Q = 0
        author = ctx.message.author

        if str(author) in Account:
            while str(author) != Account[i]:
                i += 1
            else:
                if str(author) == Account[i]:
                    P = 0
                    while Location[P][i] < 1:
                        P += 1
                    else:
                        if LocationName[P][0] == "Lumbridge Furnace":
                            if ItemAmount[11][i] >= 1:
                                l = 0
                                while Experience[5][i] >= Level[l]:
                                    l += 1
                                else:
                                    if smeltTime < time.time():
                                        a = 0
                                        while a <len(ItemName)-1 and item.lower() != ItemName[a].lower():
                                            a += 1
                                        else:
                                            if item.lower() == ItemName[a].lower():
                                                if item.lower() in str(forge).lower():
                                                    while item.lower() != forge[Q].lower():
                                                        Q += 1
                                                    else:
                                                        if Q == 0:
                                                            B = 7
                                                            R = 10
                                                            E = 12.5
                                                            G = 1
                                                            H = 1
                                                        if Q == 1:
                                                            B = 7
                                                            R = 3
                                                            E = 12.5
                                                            G = 1
                                                            H = 1
                                                        if Q == 2:
                                                            B = 7
                                                            R = 24
                                                            E = 12.5
                                                            G = 1
                                                            H = 2
                                                        if Q == 3:
                                                            B = 7
                                                            R = 25
                                                            E = 12.5
                                                            G = 1
                                                            H = 3
                                                        if Q == 4:
                                                            B = 7
                                                            R = 26
                                                            E = 12.5
                                                            G = 1
                                                            H = 4
                                                        if Q == 5:
                                                            B = 7
                                                            R = 27
                                                            E = 25
                                                            G = 2
                                                            H = 5
                                                        if ItemAmount[B][i] >= G:
                                                            if l >= H:
                                                                ItemAmount[B][i] -= G
                                                                ItemAmount[R][i] += 1
                                                                smeltTime = time.time()+5
                                                                OLD = 0
                                                                while Experience[8][i] >= Level[OLD]:
                                                                    OLD += 1
                                                                else:
                                                                    Experience[8][i] += E
                                                                    NEW = 0
                                                                    while Experience[8][i] >= Level[NEW]:
                                                                        NEW += 1
                                                                    else:
                                                                        if NEW > OLD:
                                                                            await self.bot.say("Congratulations, you just advanced a "+LevelName[8]+" level.")
                                                                            await self.bot.say("Your "+LevelName[8]+" level is now "+str(NEW)+".")
                                                                await self.bot.say("You hammer the bronze and make a "+item.lower()+".")
                                                            else:
                                                                await self.bot.say("You're not a high enough level to forge "+item.lower()+"(s).")
                                                        else:            
                                                            await self.bot.say("You don't have enough resources.")
                                                else:
                                                    await self.bot.say("You can't make a "+item.lower()+" with smithing.")
                                            else:
                                                await self.bot.say(item.lower()+" doesn't exist")
                                    
                                    else:
                                        await self.bot.say("You're tired and have to wait "+str(int(round(smeltTime-time.time(), 0)))+" more seconds to forge another item.")
                            else:
                                await self.bot.say("You don't have a hammer to forge this bar")
                        else:
                            await self.bot.say("You're not at a furnace.")
                else:
                    await self.bot.say("Who the fuck are you.")
        else:
            await self.bot.say("You're not registered.")
        Save()

    @commands.command(pass_context=True, no_pm=True)
    async def cut(self, ctx, *, Tree: str):
        """To cut trees"""
        
        global Account
        global Location
        global LocationTree
        global TreeName
        global Equipment
        global Experience
        global Level
        global LevelName

        global ItemAmount
        global ItemName

        global cutTime
        global Delay
        
        author = ctx.message.author

        i = 0
        a = 0
        P = 0
        J = 0
        if str(author) in Account:
            while str(author) != Account[i]:
                i += 1
            else:
                if str(author) == Account[i]:
                    while Location[P][i] < 1:
                        P += 1
                    else:
                        if Tree.lower() == TreeName[a].lower():
                            R = 0
                            J = 1
                            E = 25
                            G = 9
                        a += 1
                        if Tree.lower() == TreeName[a].lower():
                            R = 1
                            J = 15
                            E = 37.5
                            G = 22
                        a += 1
                        if Tree.lower() == TreeName[a].lower():
                            R = 2
                            J = 30
                            E = 67.5
                            G = 23
                        if J >= 1:
                            if LocationTree[P][R] > 0:
                                l = 0
                                while Experience[6][i] >= Level[l]:
                                    l += 1
                                else:
                                    s = 0
                                    if Equipment[6][i] == 21 or ItemAmount[21][i] > 0:
                                        s = 21
                                        V = 1
                                    else:
                                        if Equipment[6][i] == 3 or ItemAmount[3][i] > 0:
                                            s = 3
                                            V =1 
                                    if s != 0:
                                        if cutTime < time.time():
                                            if l >= J:
                                                if l >= V:
                                                    LocationTree[P][R] -= 1
                                                    await self.bot.say("You swing your axe at the "+TreeName[R]+".")
                                                    await self.bot.say("You get some "+ItemName[G]+".")
                                                    ItemAmount[G][i] += 1
                                                    OLD = 0
                                                    while Experience[9][i] >= Level[OLD]:
                                                        OLD += 1
                                                    else:
                                                        Experience[9][i] += E
                                                        NEW = 0
                                                        while Experience[9][i] >= Level[NEW]:
                                                            NEW += 1
                                                        else:
                                                            if NEW > OLD:
                                                                await self.bot.say("Congratulations, you just advanced a "+LevelName[9]+" level.")
                                                                await self.bot.say("Your "+LevelName[9]+" level is now "+str(NEW)+".")
                                                    cutTime = time.time()+5
                                                    Delay = 6
                                                else:
                                                    await self.bot.say("You're not a high enough level to cut with a "+ItemName[s]+".")
                                            else:
                                                await self.bot.say("You're not a high enough level to cut "+TreeName[R]+"s.")
                                        else:
                                            await self.bot.say("You're tired and have to wait "+str(int(round(cutTime-time.time(), 0)))+" more seconds to cut another tree.")
                                    else:
                                        await self.bot.say("You don't have a axe")
                            else:
                                await self.bot.say("There are no trees left standing")
                        else:
                            await self.bot.say("What are you trying to cut?")
                else:
                    await self.bot.say("Who are you?")
        else:
            await self.bot.say("You're not registered")
        
        Save()
        write_to_db()

    @commands.command(pass_context=True, no_pm=True)
    async def light(self, ctx, *, Logs: str):
        '''Firemaking is the companion of Woodcutting, it gives the ability to make a fire and cook things like meat and fish on the spot'''
        global Account
        global Location
        global ItemName
        global ItemAmount
        global Experience
        global lightTime
        global Level
        global LevelName
        global Delay
        global lightTime
        global burnTime
        author = ctx.message.author

        i = 0
        P = 0
        a = 0
        l = 0
        J = 0

        if str(author) in Account:
            while str(author) != Account[i]:
                i += 1
            else:
                if str(author) == Account[i]:
                    while Location[P][i] < 1:
                        P += 1
                    else:
                        if Location[P][i] > 0:
                            if Logs.lower() == str(ItemName[9]).lower():
                                J = 1
                                E = 40
                                G = 9
                            if Logs.lower() == str(ItemName[22]).lower():
                                J = 15
                                E = 60
                                G = 22
                            if Logs.lower() == str(ItemName[23]).lower():
                                J = 30
                                E = 90
                                G = 23
                            if J >= 1:
                                while Experience[10][i] >= Level[l]:
                                    l += 1
                                else:
                                    if ItemAmount[43][i] > 0:
                                        s = 0
                                        while s < len(ItemName)-1 and Logs.lower() != str(ItemName[s]).lower():
                                            s += 1
                                        else:
                                            if Logs.lower() == str(ItemName[s]).lower():
                                                if ItemAmount[s][i] > 0:
                                                    if l >= J:
                                                        if lightTime < time.time():
                                                            ItemAmount[G][i] -= 1
                                                            Delay = 7
                                                            lightTime = time.time()+5
                                                            burnTime = int(round(time.time()+randint(75,100)))
                                                            LocationFire[P] = burnTime
                                                            await self.bot.say("The fire catches and the "+ItemName[G]+" begin to burn.")
                                                            OLD = 0
                                                            while Experience[10][i] >= Level[OLD]:
                                                                OLD += 1
                                                            else:
                                                                Experience[10][i] += E
                                                                NEW = 0
                                                                while Experience[10][i] >= Level[NEW]:
                                                                    NEW += 1
                                                                else:
                                                                    if NEW > OLD:
                                                                        await self.bot.say("Congratulations, you just advanced a "+LevelName[10]+" level.")
                                                                        await self.bot.say("Your "+LevelName[10]+" level is now "+str(NEW)+".")
                                                        else:
                                                            await self.bot.say("You're tired and have to wait "+str(int(round(lightTime-time.time(), 0)))+" more seconds to light another log.")
                                                    else:
                                                        await self.bot.say("You're not a high enough level to light"+ItemName[10]+".")
                                                else:
                                                    await self.bot.say("You don't have any "+Logs+" to burn.")
                                            else:
                                                await self.bot.say(Logs+" doesn't exist.")
                                    else:
                                        await self.bot.say("You don't have a "+ItemName[43]+".")
                            else:
                                await self.bot.say(Logs+" doesn't exist.")
                        else:
                            await self.bot.say("Where are you?")
                else:
                    await self.bot.say("Who are you?")
        else:
            await self.bot.say("You're not registered.")
        Save()
    @commands.command(pass_context=True, no_pm=True)
    async def cook(self, ctx, *, RawFood):
        '''Cooking is an artisan skill that is used to cook raw food'''
        global Account
        global Location
        global ItemName
        global ItemAmount
        global Experience
        global lightTime
        global Level
        global LevelName
        global Delay
        global burnTime
        global cookTime
        author = ctx.message.author

        i = 0
        P = 0
        a = 0
        l = 0
        J = 0
        X = 0

        if str(author) in Account:
            while str(author) != Account[i]:
                i += 1
            else:
                if str(author) == Account[i]:
                    while Location[P][i] < 1:
                        P += 1
                    else:
                        if Location[P][i] > 0:
                            if RawFood.lower() == str(ItemName[8]).lower():
                                J = 1
                                E = 30
                                G = 8
                                H = 48
                            if RawFood.lower() == str(ItemName[16]).lower():
                                J = 1
                                E = 30
                                G = 16
                                H = 44
                            if RawFood.lower() == str(ItemName[17]).lower():
                                J = 1
                                E = 40
                                G = 17
                                H = 45
                            if RawFood.lower() == str(ItemName[29]).lower():
                                J = 1
                                E = 30
                                G = 29
                                H = 46
                            if RawFood.lower() == str(ItemName[31]).lower():
                                J = 1
                                E = 30
                                G = 31
                                H = 47
                            if RawFood.lower() == str(ItemName[38]).lower():
                                J = 1
                                E = 40
                                G = 38
                                H = 1
                            if J >= 1:
                                while Experience[11][i] >= Level[l]:
                                    l += 1
                                else:
                                    if time.time() < LocationFire[P]:
                                        s = 0
                                        while s < len(ItemName)-1 and RawFood.lower() != str(ItemName[s]).lower():
                                            s += 1
                                        else:
                                            if RawFood.lower() == str(ItemName[s]).lower():
                                                if ItemAmount[s][i] > 0:
                                                    if l >= J:
                                                        if cookTime < time.time():
                                                            ItemAmount[G][i] -= 1
                                                            if randint(0, 100) > 100 - (((J+30)-l)*2):
                                                                ItemAmount[H][i] += 1
                                                                await self.bot.say("You succesfully cook some "+ItemName[H]+".")
                                                                OLD = 0
                                                                while Experience[11][i] >= Level[OLD]:
                                                                    OLD += 1
                                                                else:
                                                                    Experience[11][i] += E
                                                                    NEW = 0
                                                                    while Experience[11][i] >= Level[NEW]:
                                                                        NEW += 1
                                                                    else:
                                                                        if NEW > OLD:
                                                                            await self.bot.say("Congratulations, you just advanced a "+LevelName[11]+" level.")
                                                                            await self.bot.say("Your "+LevelName[11]+" level is now "+str(NEW)+".")
                                                            else:
                                                                await self.bot.say("You accidentally burn the "+RawFood+".")
                                                            cookTime = time.time()+5
                                                            
                                                        else:
                                                            await self.bot.say("You're tired and have to wait "+str(int(round(cookTime-time.time(), 0)))+" more seconds to cook another meal.")
                                                    else:
                                                        await self.bot.say("You're not a high enough level to cook "+ItemName[G]+".")
                                                else:
                                                    await self.bot.say("You don't have any "+RawFood+" to cook.")
                                            else:
                                                await self.bot.say(RawFood+" doesn't exist.")
                                    else:
                                        await self.bot.say("There isn't a fire nearby to cook this on.")
                            else:
                                await self.bot.say(RawFood+" doesn't exist.")
                        else:
                            await self.bot.say("Where are you?")
                else:
                    await self.bot.say("Who are you?")
        else:
            await self.bot.say("You're not registered.")
        Save()
        
    @commands.command(pass_context=True, no_pm=True)
    async def test(self, ctx):
        """for testing new features"""
        global Account
        global ItemName
        global ItemAmount
        global ItemExamine
        global ItemPrice

        author = ctx.message.author
        await self.bot.say("!yt test")

        Save()
    @commands.command(pass_context=True, no_pm=True)
    async def addItem(self, ctx, iName: str, iExamine: str, iPrice: int):
        """addItem "name stuff" "Examine stuff" 1
Development tool"""
        global Account
        
        global ItemName
        global ItemAmount
        global ItemExamine
        global ItemPrice
        global NPC
        global NPCStock

        author = ctx.message.author

        a = 0
        i = 0
        x = 0
        if str(author) == Account[0]:
            ItemName += [iName]
            ItemExamine += [iExamine]
            ItemPrice += [iPrice]
            ItemAmount += [[0]]
            NPCStock += [[0]]
            while a < len(ItemAmount)-1:
                a += 1
            else:
                while i < len(Account)-1:
                    ItemAmount[a] += [0]
                    i += 1
            for y in range(len(NPC)-1):
                NPCStock[len(NPCStock)-1] += [0]
            for x in range(len(MonsterName)-1):
                MonsterDrop[x] += [0, 0, 0]
        await self.bot.say("Added Name: "+iName+" Examine: "+iExamine+" Price: "+str(iPrice)+".")
        Save()
        
    @commands.command(pass_context=True, no_pm=True)
    async def addLocation(self, ctx, L1Name: str, L2Name: str, L3Name: str):
        global Account
        global Location
        global LocationName
        
        global MonsterName
        global TreeName
        global FishName
        global RockName

        global LocationMine
        global LocationTree
        global LocationFish
        global LocationMonster
        
        global LocationMines
        global LocationTrees
        global LocationFishs
        global LocationMonsters
        
        author = ctx.message.author
        if str(author) == Account[0]:
            if L1Name in Location:
                await self.bot.say(L1Name+" Already exists")
            else:
                Location += [[0]]
                for a in range(len(Account)-1):
                    Location[a] += [0]
                    
                LocationName += [[L1Name]]
                LocationName[len(LocationName)-1] += [L2Name]
                LocationName[len(LocationName)-1] += [L3Name]

                LocationMonster += [[0]]
                LocationMonsters += [[0]]
                
                LocationTree += [[0]]
                LocationTrees += [[0]]
                
                LocationMine += [[0]]
                LocationMines += [[0]]
                
                LocationFish += [[0]]
                LocationFishs += [[0]]
                
                for a in range(len(MonsterName)-1):
                    LocationMonster[len(LocationName)-1] += [0]
                    LocationMonsters[len(LocationName)-1] += [0]
                for a in range(len(TreeName)-1):
                    LocationTree[len(LocationName)-1] += [0]
                    LocationTrees[len(LocationName)-1] += [0]
                for a in range(len(RockName)-1):
                    LocationMine[len(LocationName)-1] += [0]
                    LocationMines[len(LocationName)-1] += [0]
                for a in range(len(FishName)-1):
                    LocationFish[len(LocationName)-1] += [0]
                    LocationFishs[len(LocationName)-1] += [0]
                    
                await self.bot.say("Added location Name1: "+L1Name+" Name2: "+L2Name+" Name3: "+L3Name+".")
        Save()
    @commands.command(pass_context=True, no_pm=True)
    async def addMonsterLocation(self, ctx, Where: str, Monster: str, Amount: int):
        global Account
        global Location
        global LocationName
        
        global MonsterName
        global LocationMonster
        global LocationMonsters
        
        author = ctx.message.author
        LOC = 0
        MON = 0
        if str(author) == Account[0]:
            if Where.lower() not in str(LocationName).lower():
                await self.bot.say(Where+" doesn't exists")
            else:
                while LOC < len(LocationName)-1 and str(LocationName[LOC][0]).lower() != Where.lower():
                    LOC += 1
                else:
                    if str(LocationName[LOC][0]).lower() == Where.lower():
                        while MON < len(MonsterName)-1 and str(MonsterName[MON]).lower() != Monster.lower():
                            MON += 1
                        else:
                            if str(MonsterName[MON]).lower() == Monster.lower():
                                LocationMonster[LOC][MON] = Amount
                                LocationMonsters[LOC][MON] = Amount
                                await self.bot.say("Added "+str(Amount)+" "+Monster+"(s) to "+Where+".")
                            else:
                                await self.bot.say(Monster+" doesn't exist.")
                    else:
                        await self.bot.say(Where+" doesn't exist.")
        else:
            await self.bot.say("You are not authorized to use this command.")
        Save()

def setup(bot):
    bot.add_cog(Mycog(bot))
    read_from_db()
    # create_table()
    # dynamic_data_entry()
    f.close
    conn.close
