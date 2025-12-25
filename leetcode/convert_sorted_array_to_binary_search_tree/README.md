# Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/


Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.


<b>Example 1:</b>\
Input: nums = [-10,-3,0,5,9]
<pre>
      _0__
     /    \
   _-3     9
  /       /
-10      5
</pre>
Output: [0,-3,9,-10,null,5]
<pre>
   ____0
  /     \
-10      5
   \      \
    -3     9
</pre>
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

<b>Example 2:</b>\
Input: nums = [1,3]
<pre>
  3
 /
1
</pre>
Output: [3,1]
<pre>
1
 \
  3
</pre>
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.