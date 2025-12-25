# Range Sum of BST
https://leetcode.com/problems/range-sum-of-bst/description/


Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

 
<b>Example 1:</b>\
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
<pre>
    __10
   /    \
  5      15
 / \       \
3   7       18
</pre>
Output: 32\
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.


<b>Example 2:</b>\
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
<pre>
      ____10___
     /         \
    5__        _15
   /   \      /   \
  3     7    13    18
 /     /
1     6
</pre>
Output: 23\
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.