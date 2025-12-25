# Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/description/


Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


<b>Example 1:</b>\
Input: s = "egg", t = "add"\
Output: true\
Explanation:\
The strings s and t can be made identical by:\
Mapping 'e' to 'a'.\
Mapping 'g' to 'd'.

<b>Example 2:</b>\
Input: s = "foo", t = "bar"\
Output: false\
Explanation:\
The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

<b>Example 3:</b>\
Input: s = "paper", t = "title"\
Output: true