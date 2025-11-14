# Find the Kth Largest Integer in the Array
https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

You are given an array of strings nums and an integer k. Each string in nums represents an integer without leading zeros.

Return the string that represents the kth largest integer in nums.

Note: Duplicate numbers should be counted distinctly. For example, if nums is ["1","2","2"], "2" is the first largest integer, "2" is the second-largest integer, and "1" is the third-largest integer.


<b>Example 1:</b>\
Input: nums = ["3","6","7","10"], k = 4\
Output: "3"\
Explanation:\
The numbers in nums sorted in non-decreasing order are ["3","6","7","10"].\
The 4th largest integer in nums is "3".

<b>Example 2:</b>\
Input: nums = ["2","21","12","1"], k = 3\
Output: "2"\
Explanation:\
The numbers in nums sorted in non-decreasing order are ["1","2","12","21"].\
The 3rd largest integer in nums is "2".

<b>Example 3:</b>\
Input: nums = ["0","0"], k = 2\
Output: "0"\
Explanation:\
The numbers in nums sorted in non-decreasing order are ["0","0"].\
The 2nd largest integer in nums is "0".