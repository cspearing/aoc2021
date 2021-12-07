from os import X_OK



matrix  = []

def day3a(fileIn):
    gammaRate = ""
    epsilonRate = ""

    #parse the lines into a 2d matrix
    inputs = open(fileIn, 'r')
    lines = inputs.readlines()
    lineCount = len(lines)
    initialiseMatrix(len(lines[0].rstrip()))
    for line in lines:
        parseToMatrix(line)
    #calculate the most frequent bit
    for column in matrix:
        positiveBits = column.count(1)
        negativeBits = lineCount - positiveBits
        #build a binary number up 
        if positiveBits > negativeBits:
            gammaRate = gammaRate + "1"
            epsilonRate = epsilonRate + "0"
        else:
            gammaRate = gammaRate + "0"
            epsilonRate = epsilonRate + "1"
    #multiply the two
    print ("Gamma Rate: " + gammaRate)
    print ("Epsilon Rate: " + epsilonRate)
    gammaRateVal = int(gammaRate, 2)
    epsilonRateVal = int(epsilonRate, 2)
    power = gammaRateVal * epsilonRateVal
    print(power)

def initialiseMatrix(columnCount):
    for column in range(0, columnCount):
        matrix.append([])


def parseToMatrix(line):
    bitCount = 0
    for char in line.rstrip():
        matrix[bitCount].append(int(char))
        bitCount += 1
    

