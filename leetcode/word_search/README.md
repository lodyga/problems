# Word Search
https://leetcode.com/problems/word-search/

<p>
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
</p>

<pre>
<b>Example 1:</b>
|A → B → C↓  E|
|S   F   C↓  S|
|A   D ← E   E|

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
</pre>

<pre>
<b>Example 2:</b>
|A   B   C   E |
|S   F   C   S↓|
|A   D   E ← E |

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
</pre>

<pre>
<b>Example 3:</b>
|A → B → C × E|
|S   F   C   S|
|A   D   E   E|

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
</pre>
