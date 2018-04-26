PYTHON PROJECT:
SHIP DEPARTURE AND ARRIVAL:   		

--------------------------------------------------------------  
Calamity	danger_level	Duration	Prob_Danger
--------------------------------------------------------------
  -		0-20		0-3.5  		100-79 (21%)
Rain		20-40		1-3.5		79-58  (21%)
Lightning	40-60		2-3.5		58-38  (20%)
High Tides	60-80		3.5-5		38-20  (18%)
Cyclone		80-100		4-5		20-8   (12%)
Hurricane	100-120		4-5		8-0    (8%)


City A					City B
 |_________________ dist _________________|

Average:
If,	dist= 15,000 km
	speed, s= 25 knots
	        = 55.5 km/hr
	time, t= 270.27 hrs
		= 11.25 days

	And, please don't forget Adith xD:
	 time= dist/speed
--------------------------------

Class:
Create Calamity Class

class Calamity:
	/* Attributes same as the calamity table
	with 2 major factors:
	"danger_level" and "duration".
	They are generated randomly later on. */
--------------------------------

Dictionary:
Creating a dictionary of ships and their speed in knots.
Aaand, yes, we shall name the type of ship according to the speed.

ships{}=
{"ship1": 40
 "ship2": 35
 "ship3": 30
 "ship4": 25
 "ship5": 20
}
--------------------------------

Variables:

Dynamic:
	speed,
	danger (this is the final factor of danger),
	departure_time,
	boolean halt (ship shall not move until storm passes)

Constant:
	total_dist

Result:
	time,
	arrival_time

We need a 'dist' list.
dist=[]

Find the 'speed', add to 'time':
	time += dist[i]/speed
----------------------------------

CONDITIONS:

1.  if(total_dist<=2000 km):
	/* divide total_dist into 4 quarters.
	 for all i's: dist[i]=500 */

2.  if(total_dist>2000km):
	/*
	n=len(dist)
	for(i=0;sum(dist)<=total_dist;i++) :
		dist[i]=500
	dist(n-1)=total_dist-sum(dist)
	*/

3. 'Ship_Speed' is the function to calculate and return ship 'speed' for every division.
	'Danger_Factor' is the function to calculate and return 'danger' factor.

4. We calculate the 'speed' in every dist[i], and immediately sum it to the 'time'.
	For the first division, we shall add the 'time' to 'departure_time'.

5. If we encounter a strom in a dist[i], and has a very high 'danger' factor, ship will 'halt'(halt=true).
	So 'speed' is equal to zero.

6. We call the 'Ship_Speed' function again after the 'duration' of calamity, bcoz only then can the ship move lol.
	/*
	danger=Danger_Factor(danger_level, duration)
	if(danger> 'somevalue'):
		halt=true
	while(!halt):
		speed=Ship_Speed(ships.get("ship_name", danger))
		time+=dist[i]/speed
	*/

7. ship_speed=ships.get("ship_name")
