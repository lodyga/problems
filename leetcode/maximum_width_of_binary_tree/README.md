# Maximum Width of Binary Tree
https://leetcode.com/problems/maximum-width-of-binary-tree/

<p>
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.
</p>

<pre>
<b>Example 1:</b>
Input: root = [1,3,2,5,3,null,9]
    __1
   /   \
  3     2
 / \     \
5   3     9

Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).
</pre>

<pre>
<b>Example 2:</b>
Input: root = [1,3,2,5,null,null,9,6,null,7]
      1
     / \
    3   2__
   /       \
  5         9
 /         /
6         7

Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).
</pre>

<pre>
<b>Example 3:</b>
Input: root = [1,3,2,5]
    1
   / \
  3   2
 /
5

Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).
</pre>