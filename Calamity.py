class Calamity:

    def __init__(self, danger_level, duration):
        self.danger_level=danger_level
        self.duration=duration

    def Calamity_Type(self):
        if(self.danger_level>5 and self.danger_level<10 ):
            self.calamity_type="Rain"
        elif(self.danger_level>10 and self.danger_level<15 ):
            self.calamity_type="Lightning"
        elif(self.danger_level>15 and self.danger_level<20 ):
            self.calamity_type="High Tides"
        elif(self.danger_level>20 and self.danger_level<25 ):
            self.calamity_type="Cyclone"
        elif(self.danger_level>25 and self.danger_level<30 ):
            self.calamity_type="Hurricane"
        else:
            self.calamity_type="Unidentified"

    def Danger_Factor(self):






C=Calamity(6,10)

def main():
    C.Calamity_Type()
    print(C.calamity_type)

main()
