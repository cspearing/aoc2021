from day1.Window import Window

class WindowManager:

    windowSize = 0
    availableWindows = []
    itemIndex = 1

    def __init__(self, windowSize):
        self.windowSize = windowSize
        
    
    def add(self, value):
        #self.availableWindows
        #add value to all permitted windows.. based on it's index.
        for wIndex in range(self.itemIndex - self.windowSize, self.itemIndex):
            self.addToWindowAtIndex(wIndex, value)
        self.itemIndex+=1
        
    def addToWindowAtIndex(self, index, value):
        if (index < 0):
            return
        while len(self.availableWindows) < index+1:
            self.availableWindows.append(Window(self.windowSize))
        curWindow = self.availableWindows[index]
        curWindow.add(value)

    def getWindows(self):
        return self.availableWindows

    
