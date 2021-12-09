import functools

def solve(input : str):

    firstSpawn = 9
    secondSpawn = 7
    daysExamined = 256
    reader = open(input, 'r')
    fishyBirthdays = list(map(lambda x: 0, range(0,daysExamined+1)))
    netFish = 0
    #seed the very first set of birthdays, count the generation 1 fish
    for fishSpawnDay in map(int,reader.readline().split(",")):
        netFish +=1 
        fishSpawnDay +=1 #account for the fact 0 is actually a non spawn day
        fishyBirthdays[fishSpawnDay] += 1
        #project all spawns from gen1 fish
        nextSpawnDay = fishSpawnDay+ secondSpawn
        while (nextSpawnDay <= daysExamined):
            fishyBirthdays[nextSpawnDay] +=1
            nextSpawnDay += secondSpawn

    #calculate the reproductions across the daysExamined days, count fihs as they spawn
    for day in range (1, daysExamined+1):
        #add up the fish born today
        fishCountedToday = fishyBirthdays[day]
        netFish += fishCountedToday
        #then project their offspring
        if day + firstSpawn > daysExamined:
            continue
        firstProgenyBday = day + firstSpawn               
        fishyBirthdays[firstProgenyBday] += fishCountedToday
        nextSpawnDay = firstProgenyBday + secondSpawn
        while (nextSpawnDay <= daysExamined):
                    fishyBirthdays[nextSpawnDay] += fishCountedToday
                    nextSpawnDay += secondSpawn

    print (netFish)  

if __name__ == "__main__":
    #main(sys.argv[1:])
    solve("Inputs\\6.txt")



