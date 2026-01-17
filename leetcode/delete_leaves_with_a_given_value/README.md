# Delete Leaves With a Given Value
https://leetcode.com/problems/delete-leaves-with-a-given-value/

<p>
Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).
</p>

<pre>
<b>Example 1:</b>
Input: root = [1,2,3,2,null,2,4], target = 2
    1__
   /   \
  2     3
 /     / \
2     2   4

Output: [1,null,3,null,4]\
1
 \
  3
   \
    4

Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left).
</pre>

<pre>
<b>Example 2:</b>
Input: root = [1,3,3,3,2], target = 3
    __1
   /   \
  3     3
 / \
3   2

Output: [1,3,null,null,2]
  __1
 /
3
 \
  2
</pre>

<pre>
<b>Example 3:</b>
Input: root = [1,2,null,2,null,2], target = 2
      1
     /
    2
   /
  2
 /
2

Output: [1]
1

Explanation: Leaf nodes in green with value (target = 2) are removed at each step.
</pre>