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
    nodes[mapstart] = {"L": mapleft, "R": mapright}  # This is the Dictionary of Dictionaries we want to have (nodes)

for key in nodes.keys(): # establish starting points, list of starting points will be named "elements"
    if key[-1] == "A":
        elements.append([key, 0, 0]) # elements : [starting map, steps, found]

while not found:                                            # "found" means every element reached an end point
    for i, inst in enumerate( instructions ):               # go through all the instruction (L or R)
        for j, element in enumerate(elements):              # go thourgh all the elements with the same instruction
            if element[2] == False:                         # don't go further if endoint for this element is already found
                elements[j][0] = nodes[element[0]][inst]    # THIS IS THE MAIN STEP. Lookup next node in nodes dictionary
                elements[j][1] += 1                         # count steps
                if elements[j][0][-1] == "Z":
                    elements[j][2] = True                   # mark element if found end node

        found = True                                        # this part ensures that we exit the for loop once all elements reached the end.
        for element in elements:
            if element[2] == False:
                found = False
                break
        if found:
            break

print(elements)

# all elements reached the end node separately. Let's calculate the least common multiple of the individual steps.
for i, element in enumerate(elements[1:],1):
    elements[i][1] = (elements[i-1][1] * elements[i][1] / FindGreatestDivider(elements[i-1][1], elements[i][1]))

print(elements)

print("steps: " + str(elements[-1][1]))
