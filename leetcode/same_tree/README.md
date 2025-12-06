# Same Tree
https://leetcode.com/problems/same-tree/description/


Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


<b>Example 1:</b>\
Input: p = [1,2,3], q = [1,2,3]
<pre>
  1        1
 / \      / \
2   3    2   3
</pre>
Output: true

<b>Example 1:</b>\
Input: p = [1,2], q = [1,null,2]
<pre>
  1      1
 /        \
2          2
</pre>
Output: false

<b>Example 1:</b>\
Input: p = [1,2,1], q = [1,1,2]
<pre>
  1        1
 / \      / \
2   1    1   2
</pre>
Output: false