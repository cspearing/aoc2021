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

        #horizontal line
        if startX != endX and startY == endY:
            if startX > endX:
                x = endX
                endX = startX
                startX = x
                
            for x in range(startX,endX+1):
                matrix[startY][x] += 1

        #vertical line
        if startY != endY and startX == endX:
            if startY > endY:
                y = endY
                endY = startY
                startY = y
            for y in range(startY,endY+1):
                matrix[y][startX] += 1
        
    result = 0

    for row in matrix:
        for cell in row:            
            if cell > 1:
                result +=1

                
    print(result)

if __name__ == "__main__":
    #main(sys.argv[1:])
    solve("Inputs\\5.txt")