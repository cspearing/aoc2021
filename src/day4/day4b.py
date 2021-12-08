from typing import Match


class BingoCell:
    def __init__(self, value) -> None:
        self.__value = int(value)
        self.__match = False

    def check(self, value):
        if value == self.__value:
            self.__match = True

    @property
    def Match(self):
        return self.__match
    
    @property
    def Value(self):
        return self.__value

class BingoCard:
    def __init__(self, matrix) -> None:
        self.__matrix = []
        for row in matrix:
            cardRow = []
            for cell in row:
                cardRow.append(BingoCell(cell))
            self.__matrix.append(cardRow)
        

    def findWin(self, numberSequence):
        count = 0
        for number in numberSequence:
            self.markBingo(number)
            if self.testHorizontal():
                return count
            if self.testVertical():
                return count
            count += 1 
        return 100
        

    def markBingo(self, number):
        for row in self.__matrix:
            for cell in row:
                cell.check(number)


    def testHorizontal(self):
        for row in self.__matrix:
            success = True
            for cell in row:
                if cell.Match == False:
                    success = False
                    break
            if success:
                return True
        return False

    def testVertical(self):    
        #assume square
        for cIndex in range(0, len(self.__matrix)):
            success = True
            for rIndex in range(0, len(self.__matrix)):                
                cell = self.__matrix[rIndex][cIndex]
                if cell.Match == False:
                    success = False
                    break
            if success:
                return True
        return False

    def sumNoMatches(self):
        sum = 0
        for row in self.__matrix:
            for cell in row:
                if cell.Match == False:
                   sum += cell.Value
        return sum
 
def solve(fileIn):
    #read the first line as inputs
    inputs = open(fileIn, 'r')
    numberSequence = list(map(int, inputs.readline().split(",")))

    #read off the blank line
    inputs.readline()

    #read the 5 x 5 grids into matrixes, within wrappers
    bingoCards = []
    currentCard = []
    for line in inputs:
        if line.isspace():
            bingoCards.append(BingoCard(currentCard))
            currentCard = []
        else:
            currentCard.append(line.split())         
    bingoCards.append(BingoCard(currentCard))

    #arbitrary high value
    best = 0
    
    #for each matrix, calculate after how many inputs it would be solved
    bestCard = None
    for bingoCard in bingoCards:
        winPoint = bingoCard.findWin(numberSequence)
        if winPoint > best:
            best = winPoint
            bestCard = bingoCard
    
    #bestcard caches the one with the lowest solution score

    #calculate the result of the unmatched items multiplied by the best result
    print(bestCard.sumNoMatches() * numberSequence[best])

  
if __name__ == "__main__":
    #main(sys.argv[1:])
    solve("Inputs\\4.txt")