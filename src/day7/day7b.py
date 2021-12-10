def solve(input):
    inputFile = open(input, 'r')
    inputs = list(map(int, inputFile.readline().split(",")))

    highest = max(inputs)

    bestOption = None
    bestMoveCount = 0

    # test each possible location
    for position in range(1, highest+1):
        fuelConsumption = 0
        for crab in inputs:
            distance = abs(position - crab)
            for fuelBurn in range(1, distance+1):
                fuelConsumption += fuelBurn

        if bestOption == None or fuelConsumption < bestMoveCount:
            bestOption = position
            bestMoveCount = fuelConsumption

    print(bestOption)
    print(bestMoveCount)


if __name__ == "__main__":
    solve("Inputs\\7.txt")
