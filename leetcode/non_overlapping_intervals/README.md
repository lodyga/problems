# Non-overlapping Intervals
https://leetcode.com/problems/non-overlapping-intervals/

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

<b>Example 1:</b>\
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]\
Output: 1\
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

<b>Example 2:</b>\
Input: intervals = [[1,2],[1,2],[1,2]]\
Output: 2\
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

<b>Example 3:</b>\
Input: intervals = [[1,2],[2,3]]\
Output: 0\
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.