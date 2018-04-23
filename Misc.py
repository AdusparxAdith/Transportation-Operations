import random

def Simulation(distance):
    print(Condition_Generator(distance))







def Condition_Generator(distance):
    if(distance > 2000):
        distance_section = int(distance / 500)
    else:
        distance_section = 4

    occurances = random.randrange(0,distance_section+1)
    return(occurances)



Simulation(400)
