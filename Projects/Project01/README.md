# Project 01

### Part 1: Create an LED scanner
Write a Python program called ledscanner.py to light up the LEDs in sequence one by one until it gets to the last LED, at which point is should switch direction and scan back the first LED, and so on back and forth. 

Your program should implemented using a “state machine” as illustrated on the right (see course on Moodle for more details). A state machine has a finite number of states and can change from one state to another in response to some external inputs. The change from one state to another is called a transition.
  
This state machine has six states: STATE 1 through STATE 6. Each state corresponds to one LED being on and the rest being off.
  
You should implement your state machine using a state variable to store the current state and another variable for direction. Use a loop with a multi-way if-elif statement to test the current state and perform the operations for each state. Your state machine should pause 0.2 seconds before checking for the next state transition.

### Part 2: Add an input switch
Add a single input switch to your wiring and add a callback function to your code so that when the switch is momentarily depressed the direction input in the state machine changes to the opposite direction.

## Built With

* Python - Code base used

## Authors

* **Zachary Chin** - *Initial work*
* **Juliana Lim** - *Initial work*

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
