# Delete Leaves With a Given Value
https://leetcode.com/problems/delete-leaves-with-a-given-value/

Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).

<b>Example 1:</b>
<pre>
    1__
   /   \
  2     3
 /     / \
2     2   4
</pre>
Input: root = [1,2,3,2,null,2,4], target = 2
<pre>
1
 \
  3
   \
    4
</pre>
Output: [1,null,3,null,4]\
Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left).\
<b>Example 2:</b>
<pre>
    __1
   /   \
  3     3
 / \
3   2
</pre>
Input: root = [1,3,3,3,2], target = 3
<pre>
  __1
 /
3
 \
  2
</pre>
Output: [1,3,null,null,2]

<b>Example 3:</b>
<pre>
      1
     /
    2
   /
  2
 /
2
</pre>
Input: root = [1,2,null,2,null,2], target = 2
<pre>
1
</pre>
Output: [1]\
Explanation: Leaf nodes in green with value (target = 2) are removed at each step.