# Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/

Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

<b>Example 1:</b>\
Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4\
Output: 3\
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).

<b>Example 2:</b>\
Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5\
Output: 6\
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.