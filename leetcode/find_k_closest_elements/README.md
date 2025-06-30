# Find K Closest Elements
https://leetcode.com/problems/find-k-closest-elements/description/

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 
<b>Example 1:</b>\
Input: arr = [1,2,3,4,5], k = 4, x = 3\
Output: [1,2,3,4]

<b>Example 2:</b>\
Input: arr = [1,1,2,3,4,5], k = 4, x = -1\
Output: [1,1,2,3]