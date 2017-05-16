# SudokuSolver
A simple Sudoku solver that uses backtracking to solve any puzzle regardless of difficulty.

## Introduction
This is just a quick and dirty implementation of the [backtracking](https://en.wikipedia.org/wiki/Sudoku_solving_algorithms#Backtracking) algorithm for Sudoku solving. This uses [Numpy](http://www.numpy.org/) for nicer array manipulation, but that's not necessary, it just made development quicker.

## Features
Solves sudoku puzzles of any difficulty, either while describing each step in the process (if you use the first script) or silently (if you use the second script). It's barebones, designed to be a simple understandable implementation, rather than anything too fancy.

![Animation illustrating the computational steps made in solving a puzzle](https://raw.githubusercontent.com/aricooperdavis/SudokuSolver/master/sudoku/animation.gif)

## Installation & Usage
Clone the repo, and install Python (and Numpy).

Edit one of the scripts and type in a puzzle on line 5, using 0's as blank spaces. For example:

    (6, 0, 0, 0, 0, 0, 0, 5, 1),
    (0, 0, 0, 3, 0, 0, 9, 0, 0),
    (0, 0, 8, 0, 0, 0, 0, 0, 0),
    (0, 4, 0, 7, 0, 0, 5, 0, 0),
    (0, 0, 0, 0, 9, 0, 8, 0, 0),
    (0, 0, 1, 8, 5, 0, 0, 3, 7),
    (5, 0, 2, 6, 0 ,0, 0, 0, 4),
    (3, 0, 0, 0, 0, 7, 0, 2, 9),
    (0, 0, 4, 0, 0, 0, 0, 0, 0)

Save the script and run it; it will print the puzzle and then return the solution:

    C:\...\SudokuSolver>python sudoku_1.py

    [[6 0 0 0 0 0 0 5 1]
     [0 0 0 3 0 0 9 0 0]
     [0 0 8 0 0 0 0 0 0]
     [0 4 0 7 0 0 5 0 0]
     [0 0 0 0 9 0 8 0 0]
     [0 0 1 8 5 0 0 3 7]
     [5 0 2 6 0 0 0 0 4]
     [3 0 0 0 0 7 0 2 9]
     [0 0 4 0 0 0 0 0 0]]

     Processing...

    [[6 3 9 2 8 4 7 5 1]
     [2 1 7 3 6 5 9 4 8]
     [4 5 8 1 7 9 2 6 3]
     [8 4 3 7 2 1 5 9 6]
     [7 6 5 4 9 3 8 1 2]
     [9 2 1 8 5 6 4 3 7]
     [5 9 2 6 1 8 3 7 4]
     [3 8 6 5 4 7 1 2 9]
     [1 7 4 9 3 2 6 8 5]]

    C:\...\SudokuSolver>

## Contributing
Feel free to contribute as you wish, I'll accept all pull and merge requests if they're decent.

## License
See LICENSE for details of the GNU GPL v3.0 license that this software falls under.
