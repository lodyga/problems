# Flip Columns For Maximum Number of Equal Rows
https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

<p>
You are given an m x n binary matrix matrix.

You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).

Return the maximum number of rows that have all values equal after some number of flips.
</p>

<pre>
<b>Example 1:</b>
Input: matrix = [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.
</pre>

<pre>
<b>Example 2:</b>
Input: matrix = [[0,1],[1,0]]
Output: 2
Explanation: After flipping values in the first column, both rows have equal values.
</pre>

<pre>
<b>Example 3:</b>
Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows have equal values.
</pre>