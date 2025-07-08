# Jump Game VII
https://leetcode.com/problems/jump-game-vii/

You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.

<b>Example 1:</b>\
Input: s = "011010", minJump = 2, maxJump = 3\
Output: true\
Explanation:\
In the first step, move from index 0 to index 3.\
In the second step, move from index 3 to index 5.

<b>Example 2:</b>\
Input: s = "01101110", minJump = 2, maxJump = 3\
Output: false