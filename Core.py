import random
from tkinter import *
from tkinter import ttk,Frame,Entry, Tk

class Calamity:

    def __init__(self,weight,ship_speed,PDanger):
        self.weight=weight
        self.ship_speed=ship_speed
        self.PDanger=PDanger
        if(PDanger>=0 and PDanger<18):
            self.Calamity_Message = "\nIt's a Clear Weather. Full Sails!"
            self.wind_speed=random.uniform(30,48)
            self.sur_pressure=random.uniform(1015,1030)
            self.storm_surge=random.uniform(0,2)
        elif(PDanger>=18 and PDanger<35):
            self.Calamity_Message ="\nIt's raining! Sailing Smoothly."
            self.wind_speed=random.uniform(48,65)
            self.sur_pressure=random.uniform(1000,1015)
            self.storm_surge=random.uniform(2,3)
        elif(PDanger>=35 and PDanger<51):
            self.Calamity_Message = "\nEncountered Storm!! It's thundering. Getting back into my cabin!"
            self.wind_speed=random.uniform(65,82)
            self.sur_pressure=random.uniform(980,1000)
            self.storm_surge=random.uniform(3,6)
        elif(PDanger>=51 and PDanger<66):
            self.Calamity_Message ="\nBrace Yourselves for High Tides!!"
            self.wind_speed=random.uniform(82,95)
            self.sur_pressure=random.uniform(965,980)
            self.storm_surge=random.uniform(6,9)
        elif(PDanger>=66 and PDanger<80):
            self.Calamity_Message ="\nMoving towards a Cyclone. Take down the sails!!"
            self.wind_speed=random.uniform(95,113)
            self.sur_pressure=random.uniform(945,965)
            self.storm_surge=random.uniform(9,13)
        elif(PDanger>=80 and PDanger<92):
            self.Calamity_Message ="\nMoving towards a Cyclone. Take down the sails!!"
            self.wind_speed=random.uniform(113,135)
            self.sur_pressure=random.uniform(920,945)
            self.storm_surge=random.uniform(13,19)
        else:
            self.Calamity_Message ="\nMother of God, it's a Hurricane!!"
            self.wind_speed=random.uniform(135,150)
            self.sur_pressure=random.uniform(900,920)
            self.storm_surge=random.uniform(19,23)

    def Speed(self):
        if(self.PDanger>35): # if a calamity is encountered
            self.speed= self.ship_speed - (self.wind_speed/self.weight)*(self.storm_surge*1000/self.sur_pressure)

            if(self.speed>0):
                return(self.speed)
            else:
                self.ship_halt=True
                return(self.ship_halt)
        else: # if Clear Weather
            self.speed= self.ship_speed + (self.wind_speed/self.weight)*(self.storm_surge*1000/self.sur_pressure)
            return(self.speed)
