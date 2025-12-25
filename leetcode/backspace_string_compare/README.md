# Backspace String Compare
https://leetcode.com/problems/backspace-string-compare/description/


Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.


<b>Example 1:</b>\
Input: s = "ab#c", t = "ad#c"\
Output: true\
Explanation: Both s and t become "ac".

<b>Example 2:</b>\
Input: s = "ab##", t = "c#d#"\
Output: true\
Explanation: Both s and t become "".

<b>Example 3:</b>\
Input: s = "a#c", t = "b"\
Output: false\
Explanation: s becomes "c" while t becomes "b".