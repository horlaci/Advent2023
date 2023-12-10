file = open("input_2023_08a.txt")

contents = file.readlines()
file.close

instructions = contents[0].strip()
nodes = {}

for i, node in enumerate(contents[2:]):
    line = node.strip()
    map = line.split(" = ")
    mapstart = map[0]
    mapleft = map[1].strip("()").split(", ")[0]
    mapright = map[1].strip("()").split(", ")[1]
    nodes[mapstart] = {"L": mapleft, "R": mapright}

element = "AAA"
sum = 0
found = False
while not found:
    for i, inst in enumerate( instructions ):
        element = nodes[element][inst]
        if element == "ZZZ":
            found = True
            break
    sum += i+1

print("steps: " + str(sum))
