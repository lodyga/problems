# Path Crossing
https://leetcode.com/problems/path-crossing/description/

Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

<b>Example 1:</b>\
Input: path = "NES"\
Output: false\
Explanation: Notice that the path doesn't cross any point more than once.

<b>Example 2:</b>\
Input: path = "NESWW"\
Output: true\
Explanation: Notice that the path visits the origin twice.