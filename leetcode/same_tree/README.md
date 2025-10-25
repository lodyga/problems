# Same Tree
https://leetcode.com/problems/same-tree/description/

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


Example 1:
<pre>
  1        1
 / \      / \
2   3    2   3
</pre>
Input: p = [1,2,3], q = [1,2,3]\
Output: true

Example 2:
<pre>
  1      1
 /        \
2          2
</pre>
Input: p = [1,2], q = [1,null,2]\
Output: false

Example 3:
<pre>
  1        1
 / \      / \
2   1    1   2
</pre>
Input: p = [1,2,1], q = [1,1,2]\
Output: false