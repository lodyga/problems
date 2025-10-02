# Count the Number of Consistent Strings
https://leetcode.com/problems/count-the-number-of-consistent-strings/

You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.


<b>Example 1:</b>\
Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]\
Output: 2\
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

<b>Example 2:</b>\
Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]\
Output: 7\
Explanation: All strings are consistent.

<b>Example 3:</b>\
Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]\
Output: 4\
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.