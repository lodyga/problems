# Remove All Adjacent Duplicates in String II
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

<b>Example 1:</b>\
Input: s = "abcd", k = 2\
Output: "abcd"\
Explanation: There's nothing to delete.

<b>Example 2:</b>\
Input: s = "deeedbbcccbdaa", k = 3\
Output: "aa"\
Explanation:\
First delete "eee" and "ccc", get "ddbbbdaa"\
Then delete "bbb", get "dddaa"\
Finally delete "ddd", get "aa"

<b>Example 3:</b>\
Input: s = "pbbcggttciiippooaais", k = 2\
Output: "ps"