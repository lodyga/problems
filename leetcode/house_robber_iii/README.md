# House Robber III
https://leetcode.com/problems/house-robber-iii/

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

<b>Example 1:</b>\
Input: root = [3,2,3,null,3,null,1]
<pre>
  __3
 /   \
2     3
 \     \
  3     1
</pre>
Output: 7\
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

<b>Example 2:</b>\
Input: root = [3,4,5,1,3,null,1]
<pre>
    __3
   /   \
  4     5
 / \     \
1   3     1
</pre>
Output: 9\
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.