import random, sys, argparse

#ARGUMENT PARSING
argc = len(sys.argv)

numPlayers = 1
numCivs = 3

if (argc > 1):
    numPlayers = int(sys.argv[1])
if (argc > 2):
    numCivs = int(sys.argv[2])

gk = False
bnw = False
dlc = True
noVenice = True
noKorea = True

#creates list to distribute civs to players
civList = open("civs/BaseGame.txt").read().splitlines()
if(gk):
    civList += open("civs/GodsKings.txt").read().splitlines()
if(bnw):
    civList += open("civs/BraveNewWorld.txt").read().splitlines()
if(dlc):
    civList += open("civs/DLC.txt").read().splitlines()
civList = set(civList)
if(noVenice):
    civList -= set(["Venice (Enrico Dandolo)"])
if(noKorea):
    civList -= set(["Korea (Sejong)"])
civList = list(civList)

#ensures requested number of civs doesn't exceed number of civs
civsRequested = (numPlayers * numCivs) + 1
if(noVenice): #Venice counts as "bonus" civ
    civsRequested -= 1
if(len(civList) < civsRequested):
    sys.exit("\nError: Too many players/civs; try decreasing the number of civs per player.\n")

print()
def getCiv():
    i = random.randint(0,len(civList)-1)
    civ = civList.pop(i)
    print(civ, end='')
    if (civ == "Venice (Enrico Dandolo)"):
        return True
    return False

for p in range(numPlayers):
    extra = False
    print("Player " + str(p+1) + " choose from: ", end='')
    for i in range(numCivs):
        if (getCiv()): 
            extra = True
        if (i < (numCivs - 1)):
            print(", ", end='')
    if extra:
        print(", ", end='')
        getCiv()
    print(";")
print()