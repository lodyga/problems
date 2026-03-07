# Regions Cut By Slashes
https://leetcode.com/problems/regions-cut-by-slashes/

<p>
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.

Given the grid grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.
</p>

<pre>
<b>Example 1:</b>
Input: grid = [" /","/ "]
Output: 2
</pre>

<pre>
<b>Example 2:</b>
Input: grid = [" /","/ "]
Output: 2
</pre>

<pre>
<b>Example 3:</b>
Input: grid = ["/\\","\\/"]
Output: 5
Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.
</pre>