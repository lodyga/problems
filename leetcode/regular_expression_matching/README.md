# Regular Expression Matching
https://leetcode.com/problems/regular-expression-matching/

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

<b>Example 1:</b>\
Input: s = "aa", p = "a"\
Output: false\
Explanation: "a" does not match the entire string "aa".

<b>Example 2:</b>\
Input: s = "aa", p = "a*"\
Output: true\
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

<b>Example 3:</b>\
Input: s = "ab", p = ".*"\
Output: true\
Explanation: ".*" means "zero or more (*) of any character (.)".