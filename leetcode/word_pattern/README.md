# Word Pattern
https://leetcode.com/problems/word-pattern/description/


Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.

 
<b>Example 1:</b>\
Input: pattern = "abba", s = "dog cat cat dog"\
Output: true\
Explanation:\
The bijection can be established as:k
'a' maps to "dog".\
'b' maps to "cat".

<b>Example 2:</b>\
Input: pattern = "abba", s = "dog cat cat fish"\
Output: false

<b>Example 3:</b>\
Input: pattern = "aaaa", s = "dog cat cat dog"\
Output: false