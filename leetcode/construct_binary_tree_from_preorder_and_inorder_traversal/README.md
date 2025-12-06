# Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/


Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.


<b>Example 1:</b>\
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
<pre>
  3___
 /    \
9     _20
     /   \
    15    7
</pre>
Output: [3,9,20,null,null,15,7]

<b>Example 2:</b>\
Input: preorder = [-1], inorder = [-1]\
Output: [-1]