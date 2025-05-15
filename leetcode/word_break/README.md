# Word Break
https://leetcode.com/problems/word-break/

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

<b>Example 1:</b>\
Input: s = "leetcode", wordDict = ["leet","code"]\
Output: true\
Explanation: Return true because "leetcode" can be segmented as "leet code".

<b>Example 2:</b>\
Input: s = "applepenapple", wordDict = ["apple","pen"]\
Output: true\
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".\
Note that you are allowed to reuse a dictionary word.

<b>Example 3:</b>\
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]\
Output: false