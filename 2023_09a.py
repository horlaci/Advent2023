file = open("input_2023_09a.txt")
contents = file.readlines()
file.close

for line in contents:
    Series = line.strip().split()
    Deri = []
    for i, number in enumerate(Series):
        Deri.append(Series[i+1]-number)
        

print("steps: " + str(elements[-1][1]))
