# Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree/description/

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

<pre>
Example 1:

    __3
   /   \
  4     5
 / \
1   2
Input: root = [3,4,5,1,2]

  4
 / \
1   2
subRoot = [4,1,2]

Output: true

Example 2:

    ____3
   /     \
  4__     5
 /   \
1     2
     /
    0
Input: root = [3,4,5,1,2,null,null,null,null,0]


  4
 / \
1   2
subRoot = [4,1,2]

Output: false
</pre>