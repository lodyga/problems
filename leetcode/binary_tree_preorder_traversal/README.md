# Binary Tree Preorder Traversal
https://leetcode.com/problems/binary-tree-preorder-traversal/description/


Given the root of a binary tree, return the preorder traversal of its nodes' values.


<b>Example 1:</b>\
Input: root = [1,null,2,3]
<pre>
1__
   \
    2
   /
  3
</pre>
Output: [1,2,3]

<b>Example 2:</b>\
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
<pre>
    ______1
   /       \
  2__       3__
 /   \         \
4     5         8
     / \       /
    6   7     9
</pre>
Output: [1,2,4,5,6,7,3,8,9]

<b>Example 3:</b>\
Input: root = []\
Output: []

<b>Example 4:</b>\
Input: root = [1]\
Output: [1]