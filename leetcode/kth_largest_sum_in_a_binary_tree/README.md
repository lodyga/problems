# Kth Largest Sum in a Binary Tree
https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

<p>
You are given the root of a binary tree and a positive integer k.

The level sum in the tree is the sum of the values of the nodes that are on the same level.

Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.

Note that two nodes are on the same level if they have the same distance from the root.
</p>

<pre>
<b>Example 1:</b>
Input: root = [5,8,9,2,1,3,7,4,6], k = 2
        __5__
       /     \
    __8       9
   /   \     / \
  2     1   3   7
 / \
4   6

Output: 13
Explanation: The level sums are the following:
- Level 1: 5.
- Level 2: 8 + 9 = 17.
- Level 3: 2 + 1 + 3 + 7 = 13.
- Level 4: 4 + 6 = 10.

The 2nd largest level sum is 13.
</pre>

<pre>
<b>Example 1:</b>
Input: root = [1,2,null,3], k = 1
    1
   /
  2
 /
3

Output: 3
Explanation: The largest level sum is 3.
</pre>