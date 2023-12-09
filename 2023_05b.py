seeds = []

file = open("input_2023_05a.txt")

filecontent = file.readlines()

file.close

mapped = []
SeedMapped = []
TargetMapped = []
SeedIndex = 0

for line in filecontent:

    tokens = line.split()

    if tokens != []:
        if tokens[0]=="seeds:":
            for i in range(1, len(tokens), 2):
                seeds.append(range(int(tokens[i]), int(tokens[i])+int(tokens[i+1])))
                SeedMapped.append(False)
                #seeds.append(list((int(tokens[i]),int(tokens[i])+int(tokens[i+1]-1))))
        elif tokens[0].isnumeric():
            # We are in a mapping region
            Dest = int(tokens[0])
            Source = int(tokens[1])
            RangeLength = int(tokens[2])
            MapRange = range(Source, Source+RangeLength)

            SeedIndex = 0
            while SeedIndex < len(seeds):
                if SeedMapped[SeedIndex] == False:
                    SeedRange = seeds[SeedIndex]
                    Intersection = range(max(MapRange.start, SeedRange.start), min(MapRange.stop, SeedRange.stop)+1)
                    if Intersection:
                        mapped.append(range(Intersection.start+Dest-Source, Intersection.stop+Dest-Source))
                        TargetMapped.append(False)

                        Lowerdiff = range(SeedRange.start, min(SeedRange.stop, MapRange.start)+1)
                        if Lowerdiff:
                            seeds.append(Lowerdiff)
                            SeedMapped.append(False)

                        Upperdiff = range(max(SeedRange.start, MapRange.stop), SeedRange.stop+1)
                        if Upperdiff:
                            seeds.append(Upperdiff)
                            SeedMapped.append(False)
                        SeedMapped[SeedIndex] = True

                print(len(mapped),end='\r')
                SeedIndex += 1
                
        else:
            # Start of new mapping area, take over results to origin

            print()
            print(tokens[0])
            if mapped:
                for SeedIndex in range(0, len(seeds)):
                    if SeedMapped[SeedIndex] == False:
                        mapped.append(seeds[SeedIndex])
                        TargetMapped.append(False)

                seeds = mapped
                mapped = []
                SeedMapped = TargetMapped

Location = seeds[0].start
for NewLocation in seeds:
    if NewLocation.start < Location:
        Location = NewLocation.start

print("Locations: " + str(Location))

