# Island Perimeter
https://leetcode.com/problems/island-perimeter/description/

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

<b>Example 1:</b>\
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]\
Output: 16\
Explanation: The perimeter is the 16 yellow stripes in the image above.

<b>Example 2:</b>\
Input: grid = [[1]]\
Output: 4

<b>Example 3:</b>\
Input: grid = [[1,0]]\
Output: 4