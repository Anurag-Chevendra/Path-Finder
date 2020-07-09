# Path-Finder
This is a program that finds the path (NOTE: NOT the shortest path) from an initial point (S) to the end point (E).

If you wish to change E then open the code (ON YOUR LOCAL COMPUTER) and change the "level_1" array.

The biggest difficulty that I faced while creating this project was finding a way to integrate this code to a GUI . Since pygame is not compatible with python version 3.8 and + , things automatically became tough . I used the "Turtle" module of Python to create the GUI . 

The main purpose of creating this project was to show visually how the Recursive algorithm works . 

The code basically searches in a Path format until it reaches the End . On reaching E , it highlights a path back to the start

Blue Blocks   -Working of the Recursive algorithm.
Yellow Blocks -A path joining S and E .
