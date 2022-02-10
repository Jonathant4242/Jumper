# Jumper
A, B, C …Play with me! Are you lucky enough to keep your head until the end? This is going to be challenging, but a lot of fun, full of excitement.  
**Jumper** is a game in which the player seeks to solve a puzzle by guessing the letters of a secret word one at a time. The console choose 5 random letters for the player to guess. Player is prompted to input a letter one at a time. If the player guesses the right letter, it replaces the right dash. If the guess is wrong, one dash from the parachute is cut(deleted), and so on. The game will end if all the parts of the parachute are removed and the player loses his head. If he/she finds all 5 random letters before losing his head, the player wins.

---
## Getting Started
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python3 jumper 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the jumper folder and click the "run" icon.

## Project Structure
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- Jumper              (source code for game)
  +-- gameClasses       (specific classes)
    +-- picture.py      (code for picture class)
    +-- director.py     (code for director class)
    +-- guess.py       (code for guess class)
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Required Technologies
* Python 3.8.0

## Authors
Douglas DeMille, Haingotiana N Rambikarison, Jonathan Trok (CSE 210 Thur 11a Group)
