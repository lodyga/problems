# Count Subarrays Where Max Element Appears at Least K Times
https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/

You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.

<b>Example 1:</b>\
Input: nums = [1,3,2,3,3], k = 2\
Output: 6\
Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

<b>Example 2:</b>\
Input: nums = [1,4,2,1], k = 3\
Output: 0\
Explanation: No subarray contains the element 4 at least 3 times.