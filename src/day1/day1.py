from aoc import helpers
from day1.WindowManager import WindowManager

def day1a(fileIn):
    inputs = open(fileIn, 'r')
    lines = helpers.read_all_int_lines(inputs)
    result = -1
    lastNumber = -1
    for currentNumber in lines:
        if currentNumber > lastNumber:
            result+=1
        lastNumber = currentNumber
    print("Result: " + str(result))

def day1b(fileIn):
    inputs = open(fileIn, 'r')
    lines = helpers.read_all_int_lines(inputs)
    windowMgr = WindowManager(3)
    for line in lines:
        windowMgr.add(line)
    #have rolling windows
    #3 places in each window
    #once full compare to previous window
    #only need three windows
    #need to count one window at a time
    #need a window pointer or structure
    
    result = -1
    lastNumber = -1    
    for currentWindow in windowMgr.getWindows():
        currentNumber = currentWindow.total()
        if currentNumber > lastNumber:
            result+=1
        lastNumber = currentNumber
        
    print("Result: " + str(result))