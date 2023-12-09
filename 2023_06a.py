time = list()
distance = list()

def GetWinAttempts(mytime, dist):
    attempts = 0
    for j in range(0,mytime):
        if (j*(mytime-j) > dist):
            attempts += 1
    return attempts

file = open("input_2023_06a.txt")

for line in file:
    tokens = line.split()
    if tokens[0] == "Time:":
        for i in range(1, len(tokens)):
            time.append(int(tokens[i]))
    if tokens[0] == "Distance:":
        for i in range(1, len(tokens)):
            distance.append(int(tokens[i]))

file.close

sum = 1

for i in range(0, len(time)):
    Winnable = GetWinAttempts(time[i], distance[i])
    sum = sum * Winnable


print("Good Attempts: " + str(sum))

