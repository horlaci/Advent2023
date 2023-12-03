file = open("input_2023_02a.txt")

Sum = 0

for line in file:
    line = line[0:-1]  # remove annoying \n at end of each line

    Game = line.split(": ")  # Game[0] is game id, Game[1] are the drawings
    Gamenumber = int(Game[0].split()[1]) # extract integer game number
    
    GamePossible = True

    for Drawing in Game[1].split("; "):     # go through all drawing by splitting Game[1] (aka drawings)
        Cubes = {"red": 0, "green": 0, "blue": 0} # temporary dictionary for holding the color drawn
        for Color in Drawing.split(", "):       # Go through all colors
            Cubes[Color.split()[1]] = int(Color.split()[0])  # Update number of colors drawn in dictionary
        if (Cubes["red"] > 12) or (Cubes["green"] > 13) or (Cubes["blue"] > 14): # Game possible?
            GamePossible = False

    if GamePossible:
        Sum = Sum + Gamenumber

print("Összes: " + str(Sum))

file.close
