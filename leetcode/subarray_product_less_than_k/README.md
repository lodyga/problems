# Subarray Product Less Than K
https://leetcode.com/problems/subarray-product-less-than-k/description/

Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

<b>Example 1:</b>\
Input: nums = [10,5,2,6], k = 100\
Output: 8\
Explanation: The 8 subarrays that have product less than 100 are:\
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]\
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

<b>Example 2:</b>\
Input: nums = [1,2,3], k = 0\
Output: 0