# Construct K Palindrome Strings
https://leetcode.com/problems/construct-k-palindrome-strings/

Given a string s and an integer k, return true if you can use all the characters in s to construct non-empty k palindrome strings or false otherwise.


<b>Example 1:</b>\
Input: s = "annabelle", k = 2\
Output: true\
Explanation: You can construct two palindromes using all characters in s.\
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"

<b>Example 2:</b>\
Input: s = "leetcode", k = 3\
Output: false\
Explanation: It is impossible to construct 3 palindromes using all the characters of s.

<b>Example 3:</b>\
Input: s = "true", k = 4\
Output: true\
Explanation: The only possible solution is to put each character in a separate string.