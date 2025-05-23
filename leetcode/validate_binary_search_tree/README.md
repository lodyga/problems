# Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/description/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

<b>Example 1:</b>\
Input: root = [2,1,3]
<pre>
  2
 / \
1   3
</pre>
Output: true

<b>Example 2:</b>\
Input: root = [5,1,4,null,null,3,6]
<pre>
  5__
 /   \
1     4
     / \
    3   6
</pre>
Output: false\
Explanation: The root node's value is 5 but its right child's value is 4.