import random
import Core
from tkinter import *
from tkinter import ttk

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
    root = Tk()

    frame = ttk.Frame(root,relief = RIDGE)
    frame.pack()
    Resultframe = ttk.Frame(root)
    Resultframe.pack()

    ResultantTime_Label = ttk.Label(Resultframe)
    ResultantTime_Label.pack()

    simulated_interval=Condition_Generator(distance)
    Resultant_Time=0

    Labels =[]
    Labels1 = []
    Labels2 = []

    for i in range(0,len(simulated_interval)):
        PDanger=random.uniform(0,100)
        C=Core.Calamity(weight,ship_speed,PDanger)


        speed=C.Speed()


        if(speed>0):
            speed = round(speed, 2)
            # print(C.Calamity_Message)
            Labels.append(Label(frame,text= C.Calamity_Message))
            Labels[i].pack()

            # print("Sailing at the speed of ",speed," knots")
            Labels1.append(Label(frame,text= "Sailing at the speed of "+str(speed)))
            Labels1[i].pack()

            time=simulated_interval[i]/speed
            # print("Time: ",round(time, 2))
            Labels2.append(Label(frame,text= "Time taken is: "+str(round(time, 2))))
            Labels2[i].pack()

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

          # print(int(Days),"day(s)",int(hours),"hours",int(minutes),"minutes",int(seconds),"seconds")
          ResultantTime_Label.config(text=(int(Days),"day(s)",int(hours),"hours",int(minutes),"minutes",int(seconds),"seconds"))

    Time(Resultant_Time)

    root.mainloop()
