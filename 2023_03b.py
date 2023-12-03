def AppendToList(myDict, i, j):
    global Gear
    templist = []
    for k in range(-1,2):
        for l in range(-1,2):
            templist.append([i+k,j+l])
    myDict[Gear] = templist
    Gear = Gear + 1

Gear = 0
Engine = []
MarkingSet = {"*"}
MarkedCoordinates = dict()

file = open("input_2023_03a.txt")

for line in file:
    line = line[0:-1]  # remove annoying \n at end of each line
    Engine.append(line)

file.close

for i in range(0,len(Engine)):
    for j in range(0,len(Engine[i])):
        if Engine[i][j] in MarkingSet:
            AppendToList(MarkedCoordinates, i, j)                           # All coordinates which are valid are added to the list 
                                                                            # All nine coordinates around the Marking is added (see AppendToList function)
# print(MarkedCoordinates)

Number = 0
Valid = False
GearUpdate = 0
Sum = 0
GearRatios = dict()
for i in range(0,len(Engine)):
    for j in range(0,len(Engine[i])):
        if Engine[i][j].isnumeric():
            Number = Number * 10 + int(Engine[i][j])
            # Valid = Valid or ([i,j] in MarkedCoordinates)
            for k in MarkedCoordinates:
                if [i,j] in MarkedCoordinates[k]:
                    GearUpdate = k
                    Valid = True
        else:
            if Valid:
                if GearUpdate not in GearRatios:
                    GearRatios[GearUpdate] = 0
                if GearRatios[GearUpdate] == 0:
                    GearRatios[GearUpdate] = Number
                else:
                    GearRatios[GearUpdate] = GearRatios[GearUpdate] * Number
                    Sum = Sum + GearRatios[GearUpdate]
            Number = 0
            Valid = False

print("Sum: " + str(Sum))

