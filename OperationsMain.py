ships= {
    "cargo": 20,
    "crude": 25,
    "tanker": 30,
    "ultramax": 35,
    "ferry": 40
}

distance = float(input("What is the distance between the source and your destination? "))

# Call misc.py

# for index in ships:
#         print("\n",index,ships[index])

ship = input("\nWhich ship would you like to use? ")

ship_speed=ships.get(ship)

for i in len(distance_section):
    PDanger=rand.uniform(0,100)
    C=Calamity(ship_speed,PDanger)
