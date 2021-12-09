import re

def solve(input : str):
    reader = open(input, 'r')
    matrix = []
    limit = 1000
    for i in range(limit):
        row = []
        matrix.append(row)        
        for j in range(limit):
            row.append(0)

    #parse the coordinates into a matrix and whilst doing it, add the cell count   
    for line in reader:
        m = re.search('(\w+),(\w+)\s*->\s*(\w+),(\w+)\s*', line)
        startX = int(m.group(1))
        startY = int(m.group(2))
        endX = int(m.group(3))
        endY = int(m.group(4))     

        if startX > endX:
            xRange = range(startX,endX-1,-1)
        else:
            xRange = range(startX, endX+1, 1)

        if startY > endY:
            yRange = range(startY, endY-1, -1)
        else:
            yRange = range(startY, endY+1, 1)
     

        #horizontal line
        if startX != endX and startY == endY:                            
            for x in xRange:
                matrix[startY][x] += 1

        #vertical line
        if startY != endY and startX == endX:            
            for y in yRange:
                matrix[y][startX] += 1
        
        #diagonal line
        if startY != endY and startX != endX:
            for x, y in zip(xRange, yRange):
              matrix[y][x] += 1

    result = 0

    for row in matrix:
        line = ""
        for cell in row:            
            line += str(cell) + " "
            if cell > 1:
                result +=1
        #print (line)

                
    print(result)

if __name__ == "__main__":
    #main(sys.argv[1:])
    solve("Inputs\\5.txt")