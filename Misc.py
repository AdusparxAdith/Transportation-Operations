import random
import formula_test3

simulated_interval=[]

def Condition_Generator(distance):
    dist_interval=[]

    if(distance>2000):
        while(True):
            dist_interval.append(500.0)
            distance=distance-500
            if(distance<500):
                dist_interval.append(distance)
                break
    else:
        dist_interval=[distance/4] *4
    return dist_interval

def Simulation(weight,ship_speed,distance):
    # Give time Interval
    simulated_interval=Condition_Generator(distance)
    print("Interval: ",simulated_interval)
    #
    # for i in simulated_interval:
    #     simulated_interval[i]*= 1.852
    #
    # print("Interval in km: ",simulated_interval)
    Resultant_Time=0

    for i in range(0,len(simulated_interval)):
        PDanger=random.uniform(0,100)
        C=formula_test3.Calamity(weight,ship_speed,PDanger)

        speed=C.Speed()


        if(speed>0):
            speed = round(speed, 2)
            print("Sailing at the speed of ",speed," knots")
            time=simulated_interval[i]/speed
            print("Time: ",time)
            Resultant_Time += time
        else:
            time=(random.uniform(3.5,5))
            print("Halting for ",time)
            Resultant_Time += time
            i=i-1
            continue

    def Time(Resultant_Time):
          Days = Resultant_Time/ 24
          hours = Days - int(Days)
          hours *= 24

          minutes = hours - int(hours)
          minutes *= 60

          seconds = minutes - int(minutes)
          seconds *= 60

          print(int(Days),"day(s)",int(hours),"hours",int(minutes),"minutes",int(seconds),"seconds")

    Time(Resultant_Time)

    # print("Hours: ",Resultant_Time)
