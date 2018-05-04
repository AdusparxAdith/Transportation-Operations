import Misc

ships = { "Tanker" : 15.0,	#DWT 200
	"Cargo" : 20.0,		#DWT 120
	"Passenger Ship" : 30.0,	#DWT 80
	"Frigate" : 35.0,	#DWT 60
	"Ferry" : 40.0,		#DWT 50
	"High Speed Craft" : 50.0	#DWT 40
}

# 1 Nautical Mile (nm) = 1.852 Km
# 1 Knot= 1.852 km/hr

distance = float(input("What is the distance between the source and your destination? "))

print (ships)
ship = input("\nWhich ship would you like to use? ")
ship_speed=ships.get(ship)

# for i in ships:
if(ship not in ships):
    print("Invalid option.")
    exit(0)

# Selecting weights of  ships
print("Select the weight of the ship: ")

def weights():
    # Have to make the error clauses too
    if(ship=="Tanker"):
        print("~120-200")
    if(ship=="Cargo"):
        print("~80-120")
    if(ship=="Passenger Ship"):
        print("~60-80")
    if(ship=="Frigate"):
        print("~50-60")
    if(ship=="Ferry"):
        print("~45-50")
    if(ship=="High Speed Craft"):
        print("~40-45")

    weight=float(input())
    return weight


Misc.Simulation(weights(),ship_speed,distance)
