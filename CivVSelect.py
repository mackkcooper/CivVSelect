import random, sys

argc = len(sys.argv)

numPlayers = 1
numCivs = 3

if (argc > 1):
    numPlayers = int(sys.argv[1])
if (argc > 2):
    numCivs = int(sys.argv[2])

civList = ["America","Arabia","Assyria","Austria","Aztecs","Babylon","Brazil","Byzantium","Carthage","Celts","China","Denmark","Netherlands","Egypt","England","Ethiopia","France","Germany","Greece","Huns","Incans","India","Indonesia","Iroquois","Japan","Maya","Mongolia","Morocco","Ottomans","Persia","Poland","Polynesia","Portugal","Rome","Russia","Shoshone","Siam","Songhai","Spain","Sweden","Venice","Zulus"]

if(len(civList) < (numPlayers * numCivs)+1):
    sys.exit("\nError: Too many players/civs; try decreasing the number of civs per player.\n")

print()
def getCiv():
    i = random.randint(0,len(civList)-1)
    civ = civList.pop(i)
    print(civ, end='')
    if (civ == "Venice"):
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