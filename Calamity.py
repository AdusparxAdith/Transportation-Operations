class Calamity:
    
    def __init__(self, danger_level, duration):
        self.danger_level=danger_level
        self.duration=duration

    def Calamity_Type(self):
        if(self.danger_level>5):
            self.calamity_type="Rain"


C=Calamity(6,10)

def main():
    C.Calamity_Type()
    print(C.calamity_type)

main()
