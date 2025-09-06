# Distinct Subsequences
https://leetcode.com/problems/distinct-subsequences/

Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

<b>Example 1:</b>\
Input: s = "rabbbit", t = "rabbit"\
Output: 3\
Explanation:\
As shown below, there are 3 ways you can generate "rabbit" from s.\
<strong>rabb</strong>b<strong>it</strong>\
<strong>rab</strong>b<strong>bit</strong>\
<strong>ra</strong>b<strong>bbit</strong>

<b>Example 2:</b>\
Input: s = "babgbag", t = "bag"\
Output: 5\
Explanation:\
As shown below, there are 5 ways you can generate "bag" from s.\
<mark>ba</mark>b<mark>g</mark>bag\
<mark>ba</mark>bgba<mark>g</mark>\
<mark>b</mark>abgb<mark>ag</mark>\
ba<mark>b</mark>gb<mark>ag</mark>\
babg<mark>bag</mark>\