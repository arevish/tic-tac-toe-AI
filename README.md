# Tic Tac Toe with AI ![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)

### **Minimax AI Tic Tac Toe :** 
> Tic Tac Toe game where computer never looses, follows the concept of minimax algorithm
to never loose

playing Minimax AI computer **VS** AI Tic Tac Toe computer
Results after 350 matches!

```
Minimax Computer placed an 'O' in position  9 :
 O| O| X
---------
  | O|
---------
 X| X| O
Sorry, Minimax computer won this match !

After 350 iterations scores are
Old Computer player wins : 0 
Minimax Computer player wins : 350
Draws:  0
```

## **Tic Tac Toe AI :**
```
Welcome to Tic Tac Toe!
  |  |  
---------
  |  |  
---------
  |  |  

Please select a position to place an 'X' (1-9): gt
Please type a number!
```
  Program detects whether the given input is number or not and ask you to give a input in number again!

```
Please select a position to place an 'X' (1-9): 5
 O| X|
---------
  | X|
---------
  |  |
Computer placed an 'O' in position  8 :
 O| X|
---------
  | X|
---------
  | O|
```
Program smartly detects when it's going to loose and try to win, as above you can see insted of moving to any place computer place his move on 8th position to save itself from loosing.

```
Please select a position to place an 'X' (1-9): 9
 O| X|
---------
 O| X| X
---------
  | O| X
Computer placed an 'O' in position  7 :
 O| X|
---------
 O| X| X
---------
 O| O| X
Sorry, computer won this match !

Enter P to play again or any key to exit : p
```
It constantly look for places to make his move to make a win as above you can see, insted of moving to 3rd place where match can lead to draw situation, its move is to go for 7th position to make a win for itself.
And also asks you if you wanted to play again or not and continue the loop.

## PRE-REQUISITES
Your laptop with 3.7.x (onwards) installed.

**NOTE:** Those with Linux and MacOSX would have Python installed by default, no action required.

Windows: Download the version for your laptop via https://www.python.org/downloads/

**NOTES**
In your preferred editor, make sure indentation is set to "4 spaces".

---

Do not Delete any images Files or IT MAY CRASH THE GAME!

## Run using Python3.8+
1. Clone or download repositiory: https://github.com/arevish/tic-tac-toe-AI.git
2. In source folder, run `python3 'Tic tac toe AI.py'` to start program, optionally, run with `--help` argument to see other runtime options.

### ThankYou!
