# Lowest Common Ancestor of a Binary Search Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

<b>Example 1:</b>\
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
<pre>
    ______6__
   /         \
  2__         8
 /   \       / \
0     4     7   9
     / \
    3   5
</pre>
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

<b>Example 2:</b>\
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
<pre>
    ______6__
   /         \
  2__         8
 /   \       / \
0     4     7   9
     / \
    3   5
</pre>
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

<b>Example 3:</b>\
Input: root = [2,1], p = 2, q = 1
<pre>
  2
 /
1
</pre>
Output: 2