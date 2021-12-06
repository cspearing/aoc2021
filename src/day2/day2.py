from aoc import helpers

class Submarine:
    def __init__(self) -> None:
        self.horizontal = 0
        self.vertical = 0

    def performCommand(self,command):
        operation = command[0]
        value = int(command[1].rstrip())
        match operation:
            case "forward":
                self.horizontal += value
            case "up":
                self.vertical -= value
            case "down":
                self.vertical += value
    
    def getPosition(self):
        return (self.horizontal, self.vertical)


def day2a(fileIn):
    inputs = open(fileIn, 'r')
    lines = inputs.readlines()
    sub = Submarine()
    commands = map(parseLine, lines)
    for command in commands:
        sub.performCommand(command)
    coords = sub.getPosition()
    result = coords[0] * coords[1]
    print(result)


def parseLine(line):
    parts = str.split(line.rstrip())
    return parts


