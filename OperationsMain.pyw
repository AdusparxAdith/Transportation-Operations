from Mediator import Simulation
from tkinter import *
from tkinter import ttk,Frame,Entry, Tk

root = Tk()

mainFrame = ttk.Frame(root)
mainFrame.pack()
secondFrame = ttk.Frame(root)
secondFrame.pack()

mainFrame.config(relief = RIDGE)
secondFrame.config(relief = RIDGE)

Widget_Label = ttk.Label(secondFrame)
Widget_Label.pack()

ShipSpeed = StringVar()
Speed = DoubleVar()

Title = ttk.Label(mainFrame, text="Select your ship: ").pack()

def weights():
    # Have to make the error clauses too
	mainFrame.pack_forget()

	SpeedLabel = ttk.Label(secondFrame)
	SpeedLabel.pack()

	Speed = float(ShipSpeed.get())

	if(Speed == 15.0):
		Type_Of_Ship = ship1.cget('text')
		Widget_Label.config(text="You've chosen a Tanker(15 Knots)")
		SpeedLabel.config(text="Enter weight between 120 and 200")

	if(Speed == 20.0):
		Type_Of_Ship = ship2.cget('text')
		Widget_Label.config(text="You've chosen a Cargo(20 Knots)")
		SpeedLabel.config(text="Enter weight between 80 and 120")

	if(Speed == 30.0):
		Type_Of_Ship = ship3.cget('text')
		Widget_Label.config(text="You've chosen a Passenger Ship(30 Knots)")
		SpeedLabel.config(text="Enter weight between 60 and 80")

	if(Speed == 35.0):
		Type_Of_Ship = ship4.cget('text')
		Widget_Label.config(text="You've chosen a Frigate(35 Knots)")
		SpeedLabel.config(text="Enter weight between 50 and 60")

	if(Speed == 40.0):
		Type_Of_Ship = ship5.cget('text')
		Widget_Label.config(text="You've chosen a Ferry(40 Knots)")
		SpeedLabel.config(text="Enter weight between 45 and 50")

	if(Speed == 50.0):
		Type_Of_Ship = ship6.cget('text')
		Widget_Label.config(text="You've chosen a High Speed Craft(50 Knots)")
		SpeedLabel.config(text="Enter weight between 40 and 45")

	Weight_entry = ttk.Entry(secondFrame, width = 30)
	Weight_entry.pack()

	Distance_Label = ttk.Label(secondFrame,text = "Enter Distance between source and destination: ").pack()

	Distance_entry = ttk.Entry(secondFrame, width = 30)
	Distance_entry.pack()


	submit = ttk.Button(secondFrame,text="Submit", command = lambda: Simulation(float(Weight_entry.get()),Speed,float(Distance_entry.get()))).pack()

ship1 = ttk.Radiobutton(mainFrame, text = "Tanker", variable = ShipSpeed , value = '15.0',command=weights)
ship1.pack()
ship2 = ttk.Radiobutton(mainFrame, text = "Cargo", variable = ShipSpeed, value = '20.0',command=weights)
ship2.pack()
ship3 = ttk.Radiobutton(mainFrame, text = "Passenger Ship",  variable = ShipSpeed, value = '30.0',command=weights)
ship3.pack()
ship4 = ttk.Radiobutton(mainFrame, text = "Frigate",  variable = ShipSpeed, value = '35.0',command=weights)
ship4.pack()
ship5 = ttk.Radiobutton(mainFrame, text = "Ferry",  variable = ShipSpeed, value = '40.0',command=weights)
ship5.pack()
ship6 = ttk.Radiobutton(mainFrame, text = "High Speed Craft",  variable = ShipSpeed, value = '50.0',command=weights)
ship6.pack()

Display_Speed = ttk.Label(mainFrame,textvariable = ShipSpeed)
Display_Speed.pack()

root.mainloop()
