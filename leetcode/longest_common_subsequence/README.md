# Longest Common Subsequence
https://leetcode.com/problems/longest-common-subsequence/

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

<b>Example 1:</b>\
Input: text1 = "abcde", text2 = "ace"\
Output: 3\
Explanation: The longest common subsequence is "ace" and its length is 3.

<b>Example 2:</b>\
Input: text1 = "abc", text2 = "abc"\
Output: 3\
Explanation: The longest common subsequence is "abc" and its length is 3.

<b>Example 3:</b>\
Input: text1 = "abc", text2 = "def"\
Output: 0\
Explanation: There is no such common subsequence, so the result is 0.