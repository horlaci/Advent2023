file = open("input_2023_01a.txt")

tens = 0
ones = 0
sum = 0

for line in file:
    line = line[0:-1]  # remove annoying \n at end of each line
    for i in range(0, len(line)): # start search from left, 
        tens = 0
        if line[i].isnumeric(): # if numeric found, save it and stop search
            tens = int(line[i])
            break
    for j in range(len(line)-1, -1, -1): # start search from right
        ones = 0
        if line[j].isnumeric():  # if numeric found, save it and stop search
            ones = int(line[j])
            break
    
    sum = sum + tens * 10 + ones

print(sum)

file.close
