def AppendToList(list, i, j):
    for k in range(-1,2):
        for l in range(-1,2):
            if [i+k,j+l] not in list:
                list.append([i+k,j+l])

Engine = []
MarkingSet = set()
MarkedCoordinates = []

file = open("input_2023_03a.txt")

for line in file:
    line = line[0:-1]  # remove annoying \n at end of each line
    Engine.append(line)

file.close

for EngineLine in Engine:                                                   # Find out what are the markings.
    for i in range(0,len(EngineLine)):
        if EngineLine[i] != "." and EngineLine[i].isnumeric() == False:     # Everything is a marking which is not a '.' or a number
            MarkingSet.add(EngineLine[i])                                   # Add it to the marking set
print(MarkingSet)

for i in range(0,len(Engine)):
    for j in range(0,len(Engine[i])):
        if Engine[i][j] in MarkingSet:
            AppendToList(MarkedCoordinates, i, j)                           # All coordinates which are valid are added to the list 
                                                                            # All nine coordinates aroung the Marking is added (see AppendToList function)
# print(MarkedCoordinates)

Number = 0
Valid = False
Sum = 0
for i in range(0,len(Engine)):
    for j in range(0,len(Engine[i])):
        if Engine[i][j].isnumeric():
            Number = Number * 10 + int(Engine[i][j])
            Valid = Valid or ([i,j] in MarkedCoordinates)
        else:
            if Valid:
                Sum = Sum + Number
            Number = 0
            Valid = False

print("Sum: " + str(Sum))

