import functools



matrix  = []

def solve(fileIn):
    #parse the lines into a 2d matrix
    inputs = open(fileIn, 'r')
    lines = inputs.readlines()
    lineCount = len(lines)    
    matrix = list(map(lambda line: list(line.rstrip()), lines))
    

    #find the most popular number.
    oxygenRating = recursiveMatrixFilter(matrix, 0, lineCount, True)
    scrubberRating = recursiveMatrixFilter(matrix, 0, lineCount, False)

    #multiply the two    
    oxy = functools.reduce(lambda x,y: x+y, oxygenRating[0])
    scrub = functools.reduce(lambda x,y: x+y, scrubberRating[0])
    print ("Oxygen Rate: " + oxy)
    print ("Scrub Rate: " + scrub)
    oxygenRatingVal = int(oxy, 2)
    scrubberRatingVal = int(scrub, 2)
    lifeSupport = oxygenRatingVal * scrubberRatingVal
    print(lifeSupport)

def recursiveMatrixFilter(localMatrix, columnIndex, lineCount, wantMostNotLeast):
    #find the most popular value in the columns
    value = findMostPopularValue(localMatrix, columnIndex, wantMostNotLeast)
    #filter out the rows that don't have the correct column value
    
    newMatrix = list(filter(lambda c: c[columnIndex] == value, localMatrix))
    if (len(newMatrix) > 1):
        return recursiveMatrixFilter(newMatrix, columnIndex+1, lineCount, wantMostNotLeast)
    else:
        return newMatrix

    

def findMostPopularValue(matrix, columnIndex, wantMostNotLeast):
    positiveBits = 0
    negativeBits = 0

    for row in matrix:
        if row[columnIndex] == "1":
            positiveBits +=1
        else:
            negativeBits +=1

    #calculate the most frequent bit
    if wantMostNotLeast:
        if positiveBits >= negativeBits :
            return "1"
        else:
            return "0"
    else:
        if negativeBits <= positiveBits:
            return "0"
        else:
            return "1"



