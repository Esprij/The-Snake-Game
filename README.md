# The-Snake-Game
Atari's Snake Game recreated using Python's Turtle module &amp; some advanced methods.


## Technologies/Libraries & Modules used:
<li>Turtle</li>
<li>Time</li>
<li>Class Inheritence</li>
<li>Adv. Objects</li>

## What was Learned/Practiced:
The main subject was Class Inheritence & Adv. Objects,<br> we inherited the Turtle class into our Scoreboard & Food classes to crate advanced objects who are responsible for essential functional components within the game.

The program composes of 3 main classes:
1. Food
2. Scoreboard
3. Snake

### Class: Food
This class is responsible for generating the food object in the screen, a turtle from the Turtle class is used to create the food as well as move/refresh the food’s location. 
<br>
The class is composed of 1 method: .refresh()

### Class: Scoreboard
This class is responsible for creating the score on the screen, a turtle from the Turtle class is also created and writes the updated score on the screen. 
<br>
The class is composed of 3 methods: update_scorebaord(), reset(), and increase_score()

### Class: Snake
This class is responsible for the snake in the game, along with its movement. An array of turtles is created from the Turtle class and modified with necessary attributes to reflect the shape of the snake on screen and give the user feedback.
<br>
This class is composed of 9 methods: create_snake(), add_segment(), reset(), extend(), move(), up(), down(), right(), and left()

### The .move() method
Perhaps the most challenging part of this project, the movement of the snake. As previously mentioned, the snake was a list of turtles that reflected the image of the snake onto the screen. In order for us to move this array of turtles we had to place each turtle on top of one another, that way so we know when to move the next turtle in the array and update the screen on the display to create a "moving forward" effect on screen. On paper this may sound very confusing at first but once a look is taken at the move() method and if you were to closely at the movement of the snake on screen, you would perhaps understand what I am trying to explain.
