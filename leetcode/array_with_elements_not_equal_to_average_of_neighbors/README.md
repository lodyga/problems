# Array With Elements Not Equal to Average of Neighbors
https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/description/

You are given a 0-indexed array nums of distinct integers. You want to rearrange the elements in the array such that every element in the rearranged array is not equal to the average of its neighbors.

More formally, the rearranged array should have the property such that for every i in the range 1 <= i < nums.length - 1, (nums[i-1] + nums[i+1]) / 2 is not equal to nums[i].

Return any rearrangement of nums that meets the requirements.

<b>Example 1:</b>\
Input: nums = [1,2,3,4,5]\
Output: [1,2,4,5,3]\
Explanation:\
When i=1, nums[i] = 2, and the average of its neighbors is (1+4) / 2 = 2.5.\
When i=2, nums[i] = 4, and the average of its neighbors is (2+5) / 2 = 3.5.\
When i=3, nums[i] = 5, and the average of its neighbors is (4+3) / 2 = 3.5.

<b>Example 2:</b>\
Input: nums = [6,2,0,9,7]\
Output: [9,7,6,2,0]\
Explanation:\
When i=1, nums[i] = 7, and the average of its neighbors is (9+6) / 2 = 7.5.\
When i=2, nums[i] = 6, and the average of its neighbors is (7+2) / 2 = 4.5.\
When i=3, nums[i] = 2, and the average of its neighbors is (6+0) / 2 = 3.