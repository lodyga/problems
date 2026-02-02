# Word Break II
https://leetcode.com/problems/word-break-ii/

<p>
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
</p>

<pre>
<b>Example 1:</b>
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
</pre>

<pre>
<b>Example 2:</b>
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
</pre>

<pre>
<b>Example 3:</b>
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
</pre>