# Maximum Odd Binary Number
https://leetcode.com/problems/maximum-odd-binary-number/description/

You are given a binary string s that contains at least one '1'.

You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

Return a string representing the maximum odd binary number that can be created from the given combination.

Note that the resulting string can have leading zeros.

<b>Example 1:</b>\
Input: s = "010"\
Output: "001"\
Explanation: Because there is just one '1', it must be in the last position. So the answer is "001".

<b>Example 2:</b>\
Input: s = "0101"\
Output: "1001"\
Explanation: One of the '1's must be in the last position. The maximum number that can be made with the remaining digits is "100". So the answer is "1001".