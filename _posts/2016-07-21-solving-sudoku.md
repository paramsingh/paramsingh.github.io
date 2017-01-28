---
layout: post
title: Solving Sudoku
---

I had been thinking about doing something small loosely related to AI
for a long time, so when I came across [this problem](https://projecteuler.net/problem=96)
on Project Euler, I decided I might as well start small and write a solver for Sudoku.

Sudoku is a puzzle that I tried a lot in my childhood but I never got far with pen and
paper. It involves filling numbers between 1 to 9 in a 9 x 9 grid according to some constraints.
The details are not too interesting to talk about but the puzzle will have too many
permutations to just check all of them until we reach a solution. So I thought I would just
go ahead with searching for a solution.

I wrote a pretty basic depth first search for
the solution in C++. At each node, I found the position which has the least number of possible
values and filled it with each one and recursively searched for a solution for this new board.
This seemed extremely basic to me, but the code was actually pretty efficient. It solved all
the puzzles in the Project Euler input in about 200 ms on my PC which was much much better
than I had ever expected. On average, the search expanded about 169.10 nodes and went to
a depth of 53.64 on the 50 puzzles Project Euler provided. Choosing the order of filling
in the blocks in the order of least possible values first was the thing that makes all
the difference.

This was a pretty basic application of search algorithms but it was still fun. The code that
I wrote for the solver is on Github [here](https://github.com/paramsingh/cp/blob/master/src/practice/numbers/euler/sudoku.cpp).

