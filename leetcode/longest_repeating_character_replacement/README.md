# Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character.
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

<b>Example 1:</b>\
Input: s = "ABAB", k = 2\
Output: 4\
Explanation: Replace the two 'A's with two 'B's or vice versa.

<b>Example 2:</b>\
Input: s = "AABABBA", k = 1\
Output: 4\
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".\
The substring "BBBB" has the longest repeating letters, which is 4.\
There may exists other ways to achieve this answer too.