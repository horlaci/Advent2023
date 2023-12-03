file = open("input_2023_01a.txt")

tens = 0
ones = 0
sum = 0

for line in file:
    line = line[0:-1]  # remove annoying \n at end of each line
    for i in range(0, len(line)):
        tens = 0
        if line[i].isnumeric():
            tens = int(line[i])
            break
        elif line[i:i+3] == "one":
            tens = 1
            break
        elif line[i:i+3] == "two":
            tens = 2
            break
        elif line[i:i+5] == "three":
            tens = 3
            break
        elif line[i:i+4] == "four":
            tens = 4
            break
        elif line[i:i+4] == "five":
            tens = 5
            break
        elif line[i:i+3] == "six":
            tens = 6
            break
        elif line[i:i+5] == "seven":
            tens = 7
            break
        elif line[i:i+5] == "eight":
            tens = 8
            break
        elif line[i:i+4] == "nine":
            tens = 9
            break
    
    for i in range(len(line)-1, -1, -1):
        ones = 0
        if line[i].isnumeric():
            ones = int(line[i])
            break
        elif line[i:i+3] == "one":
            ones = 1
            break
        elif line[i:i+3] == "two":
            ones = 2
            break
        elif line[i:i+5] == "three":
            ones = 3
            break
        elif line[i:i+4] == "four":
            ones = 4
            break
        elif line[i:i+4] == "five":
            ones = 5
            break
        elif line[i:i+3] == "six":
            ones = 6
            break
        elif line[i:i+5] == "seven":
            ones = 7
            break
        elif line[i:i+5] == "eight":
            ones = 8
            break
        elif line[i:i+4] == "nine":
            ones = 9
            break
    
    sum = sum + tens * 10 + ones

print(sum)

file.close
