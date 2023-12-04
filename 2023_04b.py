file = open("input_2023_04a.txt")

Sum = 0

CardIndex = 0
CardCount = [1]

for line in file:
    line = line[0:-1]  # remove annoying \n at end of each line

    Cards = line.split(": ")[1]

    Winning = Cards.split("|")[0]
    OwnNumbers = Cards.split("|")[1]

    WinningSet = set(Winning.split())
    OwnNumbersSet = set(OwnNumbers.split())

    for i in range(0, CardCount[CardIndex]):
        tail = 0
        for number in OwnNumbersSet:
            if number in WinningSet:
                tail += 1
                if len(CardCount) < CardIndex + tail + 1:
                    CardCount.append(1)
                else:
                    CardCount[CardIndex+tail] += 1

    CardIndex += 1
    if len(CardCount) < CardIndex + 1:
        CardCount.append(1)
    else:
        CardCount[CardIndex] += 1

for count in CardCount:
    Sum = Sum + count

Sum -= 1

print("Total cards: " + str(Sum))

file.close
