# Path Sum
https://leetcode.com/problems/path-sum/description/


Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.


<b>Example 1:</b>\
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
<pre>
         5___
        /    \
    ___4     _8
   /        /  \
  11       13   4
 /  \            \
7    2            1
</pre>
Output: true\
Explanation: The root-to-leaf path with the target sum is shown.

<b>Example 2:</b>\
Input: root = [1,2,3], targetSum = 5
<pre>
  1
 / \
2   3
</pre>
Output: false\
Explanation: There are two root-to-leaf paths in the tree:\
(1 --> 2): The sum is 3.\
(1 --> 3): The sum is 4.\
There is no root-to-leaf path with sum = 5.

<b>Example 3:</b>\
Input: root = [], targetSum = 0\
Output: false\
Explanation: Since the tree is empty, there are no root-to-leaf paths.