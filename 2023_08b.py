def FindGreatestDivider(a, b):
    while a != b and a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return max(a,b)

file = open("input_2023_08a.txt")
contents = file.readlines()
file.close

instructions = contents[0].strip()
nodes = {}
elements = []
found = False

for i, node in enumerate(contents[2:]):
    line = node.strip()
    map = line.split(" = ")
    mapstart = map[0]
    mapleft = map[1].strip("()").split(", ")[0]
    mapright = map[1].strip("()").split(", ")[1]
    nodes[mapstart] = {"L": mapleft, "R": mapright}

for key in nodes.keys():
    if key[-1] == "A":
        elements.append([key, 0, 0]) # elements : [starting map, steps, found]

sum = 0

while not found:
    for i, inst in enumerate( instructions ):
        for j, element in enumerate(elements):
            if element[2] == False: # not found yet
                elements[j][0] = nodes[element[0]][inst]
                elements[j][1] += 1 # steps
                if elements[j][0][-1] == "Z":
                    elements[j][2] = True # found
        found = True
        for element in elements:
            if element[2] == False:
                found = False
                break
        if found:
            break

print(elements)

for i, element in enumerate(elements[1:],1):
    elements[i][1] = (elements[i-1][1] * elements[i][1] / FindGreatestDivider(elements[i-1][1], elements[i][1]))

print(elements)

print("steps: " + str(sum))
