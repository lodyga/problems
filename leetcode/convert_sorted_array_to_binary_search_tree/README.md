# Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced
 binary search tree.

<pre>
Example 1:

Input: nums = [-10,-3,0,5,9]

      _0__
     /    \
   _-3     9
  /       /
-10      5

Output: [0,-3,9,-10,null,5]

   ____0
  /     \
-10      5
   \      \
    -3     9

Explanation: [0,-10,5,null,-3,null,9] is also accepted:


Example 2:

Input: nums = [1,3]

  3
 /
1

Output: [3,1]

1
 \
  3

Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
</pre>