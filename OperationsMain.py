distance = input("What is the distance between the source and your destination? ")

ships= {"cargo": 20,
        "crude": 25,
        "tanker": 30,
        "ultramax": 35,
        "ferry": 40
        }

for index in ships:
    print("\n",index,ships[index])

ship = input("\n\nWhich ship would you like to use? ")
