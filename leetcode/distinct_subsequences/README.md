# Distinct Subsequences
https://leetcode.com/problems/distinct-subsequences/

<p>
Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.
</p>

<pre>
<b>Example 1:</b>
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
<u>rabb</u>b<u>it</u>
<strong>rab</strong>b<strong>bit</strong>
<mark>ra</mark>b<mark>bbit</mark>
</pre>

<pre>
<b>Example 2:</b>
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
<u>ba</u>b<u>g</u>bag
<u>ba</u>bgba<u>g</u>
<u>b</u>abgb<u>ag</u>
ba<u>b</u>gb<u>ag</u>
babg<u>bag</u>
</pre>