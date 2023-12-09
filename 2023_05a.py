file = open("input_2023_05a.txt")

seeds = [194657215, 187012821, 1093203236, 6077151, 44187305, 148722449, 2959577030, 152281079, 3400626717, 198691716, 1333399202, 287624830, 2657325069, 35258407, 1913289352, 410917164, 1005856673, 850939, 839895010, 162018909]

mapped = []

for i in range(0, len(seeds)):
    mapped.append(False)

for line in file:
    line = line[0:-1]  # remove annoying \n at end of each line

    if line == '':
        for i in range(0, len(mapped)):
            mapped[i] = False
    elif line[0].isnumeric() == True:
        destin = int(line.split()[0])
        source = int(line.split()[1])
        rangelength = int(line.split()[2])
        for i in range(0, len(seeds)):
            if seeds[i] in range(source, source+rangelength) and mapped[i] == False:
                seeds[i] = destin + seeds[i] - source
                mapped[i] = True
                
seeds.sort()

print("Locations: " + str(seeds))

file.close
