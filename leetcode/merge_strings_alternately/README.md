# Merge Strings Alternately
https://leetcode.com/problems/merge-strings-alternately/description/

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

<b>Example 1:</b>\
Input: word1 = "abc", word2 = "pqr"\
Output: "apbqcr"\
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

<b>Example 2:</b>\
Input: word1 = "ab", word2 = "pqrs"\
Output: "apbqrs"\
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

<b>Example 3:</b>\
Input: word1 = "abcd", word2 = "pq"\
Output: "apbqcd"\
Explanation: Notice that as word1 is longer, "cd" is appended to the end.\
word1:  a   b   c   d\
word2:    p   q \
merged: a p b q c   d