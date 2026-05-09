# Count Good Nodes in Binary Tree
https://leetcode.com/problems/count-good-nodes-in-binary-tree/

<p>
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
</p>

<pre>
<b>Example 1:</b>

    3__
   /   \
  1     4
 /     / \
3     1   5

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
</pre>

<pre>
<b>Example 2:</b>

    __3
   /
  3
 / \
4   2

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
</pre>


<pre>
<b>Example 3:</b>
Input: root = [1]
Output: 1
Explanation: Root is considered as good.
</pre>
