file = open("input_2023_04a.txt")

Sum = 0

for line in file:
    line = line[0:-1]  # remove annoying \n at end of each line

    Cards = line.split(": ")[1]

    Winning = Cards.split("|")[0]
    OwnNumbers = Cards.split("|")[1]

    WinningSet = Winning.split()
    OwnNumbersSet = OwnNumbers.split()

    Score = 0
    for number in OwnNumbersSet:
        if number in WinningSet:
            if Score == 0:
                Score = 1
            else:
                Score = Score * 2
    
    Sum = Sum + Score


print("Total Score: " + str(Sum))

file.close
