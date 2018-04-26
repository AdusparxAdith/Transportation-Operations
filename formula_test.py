import random

class Calamity:

# Create constructor for CALAMITY object, taking parameters:
# ship_speed,PDanger

# ship_speed

# PDanger=random.uniform(0,99)

# Inside the constructor, the if-else clause begins:
    if(PDanger>=79 and PDanger<100):
        print("It's a Clear Weather. Full Sails!")
        danger_level=random.uniform(0,20)
        duration=random.uniform(0,3.5)
    elif(PDanger>=58 and PDanger<79):
        print("It's raining! Sailing Smoothly.")
        danger_level=random.uniform(20,40)
        duration=random.uniform(1,3.5)
    elif(PDanger>=38 and PDanger<58):
        print("Encountered Storm!! It's thundering. Gotta get back into my cabin!")
        danger_level=random.uniform(40,60)
        duration=random.uniform(2,3.5)
    elif(PDanger>=20 and PDanger<38):
        print("Brace Yourselves for High Tides!!")
        danger_level=random.uniform(60,80)
        duration=random.uniform(3.5,5)
    elif(PDanger>=8 and PDanger<20):
        print("Moving towards a Cyclone. Take down the sails!!")
        danger_level=random.uniform(80,100)
        duration=random.uniform(4,5)
    else:
        print("Mother of God, it's a Hurricane!!")
        danger_level=random.uniform(100,120)
        duration=random.uniform(4,5)

    # funciton for calculating PDanger and speed
    #
    if(PDanger<79): #if not a clear Weather
        Danger= (danger_level * duration)/10
        speed= ship_speed - Danger
    else: #if it is a clear weather, ship should accelerate
        profit= (danger_level * duration)/10
        speed= ship_speed + profit

    print("Danger Level: ", danger_level)
    print("Duration: ",duration)

    if(PDanger<79): #Clear weather not considered a Danger
        print("Danger: ",Danger)
        
    if(speed>0):
        print("Speed ",speed)
    else:
        print("Halt")
