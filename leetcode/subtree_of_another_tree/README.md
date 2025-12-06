# Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree/description/


Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.


<b>Example 1:</b>
Input: root = [3,4,5,1,2]
<pre>

    __3
   /   \
  4     5
 / \
1   2

</pre>
subRoot = [4,1,2]
<pre>
  4
 / \
1   2
</pre>
Output: true

<b>Example 2:</b>
Input: root = [3,4,5,1,2,null,null,null,null,0]
<pre>
    ____3
   /     \
  4__     5
 /   \
1     2
     /
    0
</pre>
subRoot = [4,1,2]
<pre>
  4
 / \
1   2
</pre>
Output: false