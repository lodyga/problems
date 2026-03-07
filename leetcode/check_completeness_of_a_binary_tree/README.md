# Check Completeness of a Binary Tree
https://leetcode.com/problems/check-completeness-of-a-binary-tree/

<p>
Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
</p>

<pre>
<b>Example 1:</b>
Input: root = [1,2,3,4,5,6]
    __1__
   /     \
  2       3
 / \     /
4   5   6

Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
</pre>

<pre>
<b>Example 2:</b>
Input: root = [1,2,3,4,5,null,7]
    __1
   /   \
  2     3
 / \     \
4   5     7

Output: false
Explanation: The node with value 7 isn't as far left as possible.
</pre>

<pre>
<b>Example 3:</b>
Input: root = [1,2,3,4,5,6,7,8,9,10,11,12,13,null,null,15]
           ________1________
          /                 \
       __2___             ___3
      /      \           /    \
     4       _5        _6      7
    / \     /  \      /  \
  _8   9   10   11   12   13
 /
15

Output: false
Explanation: The node with value 7 isn't as far left as possible.
</pre>