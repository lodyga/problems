# Count Good Nodes in Binary Tree
https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/


Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.


<b>Example 1:</b>\
Input: root = [3,1,4,3,null,1,5]\
<pre>
    3__
   /   \
  1     4
 /     / \
3     1   5
</pre>
Output: 4\
Explanation: Nodes in blue are good.\
Root Node (3) is always a good node.\
Node 4 -> (3,4) is the maximum value in the path starting from the root.\
Node 5 -> (3,4,5) is the maximum value in the path\
Node 3 -> (3,1,3) is the maximum value in the path.

<b>Example 2:</b>\
Input: root = [3,3,null,4,2]\
<pre>
    __3
   /
  3
 / \
4   2
</pre>
Output: 3\
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

<b>Example 3:</b>\
Input: root = [1]\
Output: 1\
Explanation: Root is considered as good.