# Zigzag Conversion
https://leetcode.com/problems/zigzag-conversion/

<p>
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
</p>

<pre>
<b>Example 1:</b>
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
</pre>

<pre>
<b>Example 2:</b>
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
</pre>

<pre>
<b>Example 3:</b>
Input: s = "A", numRows = 1
Output: "A"
</pre>