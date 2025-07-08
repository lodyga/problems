# Append Characters to String to Make Subsequence
https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

You are given two strings s and t consisting of only lowercase English letters.

Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

<b>Example 1:</b>\
Input: s = "coaching", t = "coding"\
Output: 4\
Explanation: Append the characters "ding" to the end of s so that s = "coachingding".\
Now, t is a subsequence of s ("coachingding").\
It can be shown that appending any 3 characters to the end of s will never make t a subsequence.

<b>Example 2:</b>\
Input: s = "abcde", t = "a"\
Output: 0\
Explanation: t is already a subsequence of s ("abcde").

<b>Example 3:</b>\
Input: s = "z", t = "abcde"\
Output: 5\
Explanation: Append the characters "abcde" to the end of s so that s = "zabcde".\
Now, t is a subsequence of s ("zabcde").\
It can be shown that appending any 4 characters to the end of s will never make t a subsequence.