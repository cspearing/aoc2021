def solve(input):
    inputFile = open(input, 'r')
    inputs = list(map(int, inputFile.readline().split(",")))

    highest = max(inputs)

    bestOption = None
    bestFuelConsumption = 0

    # test each possible location
    for i in range(1, highest+1):
        fuelConsumption = 0
        for crab in inputs:
            fuelConsumption += abs(i - crab)

        if bestOption == None or fuelConsumption < bestFuelConsumption:
            bestOption = i
            bestFuelConsumption = fuelConsumption

    print(bestOption)
    print(bestFuelConsumption)


if __name__ == "__main__":
    solve("Inputs\\7.txt")
