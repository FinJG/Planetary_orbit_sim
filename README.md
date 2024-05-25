### run "pip install -r requirements.txt" in the console to install all of this projects dependencies

# Welcome to my planetary orbit sim!!

this is fairly bare-bones atm, but its fun to play around with 

# Controls

- `R` — restarts the simulation
  
- `SPACE` — pauses and plays the simulation

- `[` and `]` — cycles through and highlights the planets 'trails' 

- `ENTER` — selects the currently highlighted planet, the selected planet's trail will now always be visible, until unselected 

- `W` and `S` — will fastforward / rewind the trial of the selected planets while the simulation is paused
 
- hold `Z` — while fastforwarding or rewinding the simultaion to slow down the (fastforwarding / rewinding) speed
- hold `X` — while fastforwarding or rewinding the simultaion to speed up the (fastforwarding / rewinding) speed

# Setting up a simulation 

the default simulation creates a planet with 1_000_000_000 mass in the center of the screen,
and then creates 10 planets with random position, mass and initial velocity.

this essentially creates a sort of self-forming solar system.


currently, the only way to change the simulation is to manually change the code in the "new_game" function, found in the "settings.py" folder.

also, this program sort of works like a cellular automata (idk if it counts as one) in the sense that, when you run the program, you will always get 
the same result every time, assuming the starting conditions dont change. 

so i recomend playing around with different settings and see what results you get 

i hope you enjoy ;)
