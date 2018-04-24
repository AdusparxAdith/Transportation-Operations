import random
# GIVEN
ship_speed= 30



PDanger=random.uniform(0,100)

# if(PDanger<20):
#     print("Clear weather.",PDanger)
# else:
#     print("Encountered storm.",PDanger)

if(PDanger>=79 and PDanger<100):
    print("It's a Clear Weather. Full Sails!")
elif(PDanger>=58 and PDanger<79):
    print("It's raining! Sailing Smoothly.")
    danger_level=random.uniform(20,40)
    FDuration=random.uniform(0,100)
elif(PDanger>=38 and PDanger<58):
    print("Encountered Storm!! It's thundering. Gotta get back into my cabin!")
    danger_level=random.uniform(40,60)
    FDuration=random.uniform(0,90)
elif(PDanger>=20 and PDanger<38):
    print("Brace Yourselves for High Tides!!")
    danger_level=random.uniform(60,80)
    FDuration=random.uniform(0,80)
elif(PDanger>=8 and PDanger<20):
    print("Moving towards a Cyclone. Take down the sails!!")
    danger_level=random.uniform(80,100)
    FDuration=random.uniform(0,75)
else:
    print("Mother of God, it's a Hurricane!!")
    danger_level=random.uniform(100,110)
    FDuration=random.uniform(0,70)

duration=random.uniform(0,5)
duration=(duration * FDuration) /100

#
#
# danger_level=105
# duration=4.5
# FDuration=67.8
#
# duration= (duration * FDuration)/100
#
Danger= (danger_level * duration)/15
speed= ship_speed - Danger

print("Speed ",speed)
print("Danger: ",Danger)

# Danger_Factor()
