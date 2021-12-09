import functools

class Fish:
    def __init__(self,age) -> None:
        self.age = age

def solve(input : str):
    reader = open(input, 'r')
    fishes = list(map(Fish,map(int,reader.readline().split(","))))

    for day in range(80):
        print (day)
        for i in range(tick(fishes)):            
            fishes.append(Fish(8))
 
    print ("for " + str(len(fishes)))


def tick(fishes: list[Fish]):
    fishToAdd = 0
    for fish in fishes:
        if fish.age == 0:            
            fishToAdd +=1
            fish.age = 6
        else:
            fish.age -= 1
    return fishToAdd

if __name__ == "__main__":
    #main(sys.argv[1:])
    solve("Inputs\\6.txt")



