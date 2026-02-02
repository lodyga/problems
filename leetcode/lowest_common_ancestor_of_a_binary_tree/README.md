# Lowest Common Ancestor of a Binary Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

<p>
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
</p>

<pre>
<b>Example 1:</b>
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    ______3__
   /         \
  5__         1
 /   \       / \
6     2     0   8
     / \
    7   4

Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
</pre>

<pre>
<b>Example 2:</b>
    ______3__
   /         \
  5__         1
 /   \       / \
6     2     0   8
     / \
    7   4

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
</pre>

<pre>
Input: root = [1,2], p = 1, q = 2
<b>Example 3:</b>
  1
 /
2

Output: 1
</pre>