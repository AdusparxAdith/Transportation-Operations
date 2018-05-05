import random

def Condition_Generator(distance):
    if(distance > 2000):
        distance_section = int(distance / 500)
        distance_interval = []
        while(distance % 500 == 0 and len(distance_interval) <= distance_section):
            distance_interval.append(500)
        distance_interval.append(distance%500)
        distance = distance-(distance%500)
        Condition_Generator(distance)
    else:
        distance_section = 4
        distance_interval = distance/4

    return(distance_section)

# def Simulation(ship_speed,distance):d 
#     for i in len(distance_section):
#         PDanger=rand.uniform(0,100)
#         C=Calamity(ship_speed,PDanger)
#
# distance_section=[]     # 500  500  500  500 500 500 500 430
# len(distance_section)
#
#     occurances = random.randrange(0,distance_section+1)
#     return(occurances)
#
# Simulation(400)
