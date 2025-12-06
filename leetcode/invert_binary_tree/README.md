# Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/description/


Given the root of a binary tree, invert the tree, and return its root.


<b>Example 1:</b>\
Input: root = [4,2,7,1,3,6,9]
<pre>
    __4__
   /     \
  2       7
 / \     / \
1   3   6   9
</pre>
Output: [4,7,2,9,6,3,1]
<pre>
    __4__
   /     \
  7       2
 / \     / \
9   6   3   1
</pre>

<b>Example 2:</b>\
Input: root = [2,1,3]
<pre>
  2
 / \
1   3
</pre>
Output: [2,3,1]
<pre>
  2
 / \
3   1
</pre>

<b>Example 3:</b>\
Input: root = []\
Output: []