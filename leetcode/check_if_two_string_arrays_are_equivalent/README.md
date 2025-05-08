# Check If Two String Arrays are Equivalent
https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/

Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

<b>Example 1:</b>\
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]\
Output: true\
Explanation:\
word1 represents string "ab" + "c" -> "abc"\
word2 represents string "a" + "bc" -> "abc"\
The strings are the same, so return true.

<b>Example 2:</b>\
Input: word1 = ["a", "cb"], word2 = ["ab", "c"]\
Output: false

<b>Example 3:</b>\
Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]\
Output: true