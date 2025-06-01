# Minimum Operations to Reduce X to Zero
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

<b>Example 1:</b>\
Input: nums = [1,1,4,2,3], x = 5\
Output: 2\
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

<b>Example 2:</b>\
Input: nums = [5,6,7,8,9], x = 4\
Output: -1

<b>Example 3:</b>\
Input: nums = [3,2,20,1,1,3], x = 10\
Output: 5\
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.