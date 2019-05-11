import random, sys, argparse

#create argument parser and parse arguments from user
parser = argparse.ArgumentParser(description="Assign to each of P players, C civs.")
parser.add_argument("numPlayers", default=1, metavar="P", type=int, nargs="?", help="# of players")
parser.add_argument("numCivs", default=3, metavar="C", type=int, nargs="?", help="# of civs")
parser.add_argument("-args", "--showArgs", 
dest="showArgs", default=False, action="store_true", help="display arguments")
parser.add_argument("-r", "--showRulers", 
dest="showRulers", default=False, action="store_true", help="display ruler")
parser.add_argument("-b", "--base", 
dest="base", default=False, action="store_true", help="use only base game civs")
parser.add_argument("-gk", "--GodsKings", 
dest="gk", default=False, action="store_true", help="use only Gods & Kings expansion civs")
parser.add_argument("-bnw", "--BraveNewWorld", 
dest="bnw", default=False, action="store_true", help="use only Brave New World expansion civs")
parser.add_argument("-dlc", "--downloadable", 
dest="dlc", default=False, action="store_true", help="use only DLC civs")
parser.add_argument("-ex", "--excludeCivs", 
type=str, nargs="+", help="exclude civs from selection")
parser.add_argument("-vb", "--VeniceBonus", 
dest="veniceBonus", default=False, action="store_true", help="Venice awards bonus civ")
args = parser.parse_args()

#logic for determining which civ sets to include and whether to give Venice a bonus civ
if(not(args.base or args.gk or args.bnw or args.dlc)):
    #if none of the civ set selectors, then include all by default
    #else only include civs explicitly asked for
    args.base = True
    args.gk = True
    args.bnw = True
    args.dlc = True
if(not args.bnw): args.veniceBonus = False
if(args.showArgs): 
    print(args)

#create list to distribute civs to players
civList = []
if(args.base): civList += open("civs/BaseGame.txt").read().splitlines()
if(args.gk): civList += open("civs/GodsKings.txt").read().splitlines()
if(args.bnw): civList += open("civs/BraveNewWorld.txt").read().splitlines()
if(args.dlc): civList += open("civs/DLC.txt").read().splitlines()
civList = set(civList)
civList = list(civList)

#civ removal algorithm
if(args.excludeCivs):
    removedCivs = [] #holds civs removed from selection
    couldntFind = [] #holds civs unable to be removed
    for toRemove in args.excludeCivs:
        found = False
        for i in range(len(civList)):
            if(civList[i].split("|")[0] == toRemove):
                civList.pop(i)
                removedCivs.append(toRemove)
                found = True
                break
        if(not found): couldntFind.append(toRemove)
    if(removedCivs): print("\n" + ", ".join(removedCivs) + " removed from selection.")
    if(couldntFind): print("\n" + ", ".join(couldntFind) + " unable to be removed from selection.")

#ensure requested number of civs doesn't exceed number of civs
civsRequested = (args.numPlayers * args.numCivs)
if(args.veniceBonus): civsRequested += 1
if(len(civList) < civsRequested):
    sys.exit("\nError: Too many players/civs; try decreasing the number of civs per player.\n")

#function to grab civ from civList
def getCiv():
    i = random.randint(0,len(civList)-1)
    civ = civList.pop(i).split("|")
    print(civ[0], end='')
    if(args.showRulers): print(" (" + civ[1] + ")", end='')
    if (args.veniceBonus and civ[0] == "Venice"): return True
    return False

#run civ selection algorithm
print()
for p in range(args.numPlayers):
    extra = False
    print("Player " + str(p+1) + " choose from: ", end='')
    for i in range(args.numCivs):
        if (getCiv()): 
            extra = True
        if (i < (args.numCivs - 1)):
            print(", ", end='')
    if extra:
        print(", ", end='')
        getCiv()
    print(";")
print()