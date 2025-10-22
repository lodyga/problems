# Minimum Increment to Make Array Unique
https://leetcode.com/problems/minimum-increment-to-make-array-unique/

You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

Return the minimum number of moves to make every value in nums unique.

The test cases are generated so that the answer fits in a 32-bit integer.


<b>Example 1:</b>\
Input: nums = [1,2,2]\
Output: 1\
Explanation: After 1 move, the array could be [1, 2, 3].

<b>Example 2:</b>\
Input: nums = [3,2,1,2,1,7]\
Output: 6\
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].\
It can be shown that it is impossible for the array to have all unique values with 5 or less moves.