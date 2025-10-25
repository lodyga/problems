# Construct Binary Tree from Inorder and Postorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.


<b>Example 1:</b>\
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
<pre>
  3___
 /    \
9     _20
     /   \
    15    7
</pre>
Output: [3,9,20,null,null,15,7]

<b>Example 2:</b>\
Input: inorder = [-1], postorder = [-1]\
Output: [-1]