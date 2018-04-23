distance = input("What is the distance between the source and your destination? ")

ships= {"cargo": 40,
        "crude": 35,
        "tanker": 30,
        "ultramax": 25,
        "ferry": 20
        }

for index in ships:
    print("\n",index,ships[index])

ship = input("\n\nWhich ship would you like to use? ")
