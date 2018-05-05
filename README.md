# Transportation-Operations

SAFFIR-SIMPSONS SCALE:

--------------------------------------------------------------------------------------------------------------
Category	Wind Speed	Minimum Surface Pressure	Storm Surge	|	Probability (~14.285%)
--------------------------------------------------------------------------------------------------------------
 -		30-48			1015-1030		0-2		|	18% (0-18)
 0		48-65			1000-1015		2-3		|	17% (18-35)
(Profittable)_________________________________________________________________________________________________
 1		65-82			980-1000		3-6		|	16% (35-51)
 2		82-95			965-980			6-9		|	15% (51-66)
 3		95-113			945-965			9-13		|	14% (66-80)
 4		113-135			920-945			13-19		|	12% (80-92)
 5		135-150			900-920			19-23		|	8%  (92-100)



FORMULA:

S = s' - (wind/weight)*(storm/pressure)

where,
	weight is in Tonnage (2 digits),
	pressure is in Bar (value * 10^-3)


SHIP DICTIONARY:

ships = { "Tanker" : 15.0	#DWT 200
	"cargo": 20.0,		#DWT 120 
	"Passenger Ship": 30.0,	#DWT 80
	"Frigate": 35.0,	#DWT 60
	"Ferry": 40.0		#DWT 50
	"High Speed Craft": 50	#DWT 40
}

