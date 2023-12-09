file = open("input_2023_07a.txt")

deals = []

def GenerateSubstitutes(hand):
    CardList = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    hands = set()
    found = False
    for i, card in enumerate(hand):
        if card == "J":
            found = True
            for letter in CardList:
                newhand = hand[:i] + letter + hand[i + 1:]
                hands.update(GenerateSubstitutes(newhand))
    if not found:
        hands.add(hand)
        #print(str(hands), end='\r')
    return hands

def CalculateRank(hand):
    # five: 600000h
    # four: 500000h
    # full house: 400000h
    # drill: 300000h
    # two pair: 200000h
    # one pair: 100000h
    CardCount = {"A":0, "K":0, "Q":0, "J":0, "T":0, "9":0, "8":0, "7":0, "6":0, "5":0, "4":0, "3":0, "2":0}
    CardValue = {"A":0xD, "K":0xC, "Q":0xB, "T":0x9, "9":0x8, "8":0x7, "7":0x6, "6":0x5, "5":0x4, "4":0x3, "3":0x2, "2":0x1, "J":0x0}
    
    substitutes = list(GenerateSubstitutes(hand))

    maximalrank = 0
    for substhand in substitutes:
        rank = 0
        for key in CardCount.keys():
            CardCount[key] = 0
        print(substhand, end='\r')
        for i, card in enumerate(hand):
            rank += CardValue[card] * (0x1 << (4*(5-i-1)))
        for i, card in enumerate(substhand):
            CardCount[card] += 1
        for key in CardCount.keys() :
            if CardCount[key] == 5:
                rank += 0x600000
            if CardCount[key] == 4:
                rank += 0x500000
            if CardCount[key] == 3:
                rank += 0x300000
            if CardCount[key] == 2:
                rank += 0x100000
        if rank > maximalrank:
            maximalrank = rank
            print()
    return maximalrank

for line in file:
    tokens = line.split()
    deal = [tokens[0], tokens[1], 0]  # deal is a list where sublist[0] is hand, sublist[1] is bet, and sublist[2] is rank (not yet calculated)
    deals.append(deal)                   # deals is a list of these sublists
file.close

# establish ranks
for deal in deals:
    print(deal)
    deal[2] = CalculateRank(deal[0])

# Sort cards based on rank
deals.sort(key = lambda x : x[2])

# Calculate full winnings
sum = 0
for i, deal in enumerate(deals):
    sum = sum + (i+1)*int(deal[1])

print("Full winnings: " + str(sum))
