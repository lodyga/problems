# Leaf-Similar Trees
https://leetcode.com/problems/leaf-similar-trees/description/

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
<pre>
    ______3__
   /         \
  5__         1
 /   \       / \
6     2     9   8
     / \
    7   4
</pre>

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 
<pre>
Example 1:
    ______3__
   /         \
  5__         1
 /   \       / \
6     2     9   8
     / \
    7   4

    __3__
   /     \
  5       1__
 / \     /   \
6   7   4     2
             / \
            9   8
Input:   root1 = [3,5,1,6,2,9,8,null,null,7,4], 
         root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true


Example 2:

  1
 / \
2   3

  1
 / \
3   2

Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
</pre>