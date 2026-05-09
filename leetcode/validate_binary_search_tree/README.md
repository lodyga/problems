# Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/

<p>
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.
</p>

<pre>
<b>Example 1:</b>

  2
 / \
1   3

Input: root = [2,1,3]
Output: true
</pre>

<pre>
<b>Example 2:</b>

  5__
 /   \
1     4
     / \
    3   6

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
</pre>
