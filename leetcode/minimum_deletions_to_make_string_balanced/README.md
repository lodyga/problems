# Minimum Deletions to Make String Balanced
https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

<p>
You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.
</p>

<pre>
<b>Example 1:</b>
Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
</pre>

<pre>
<b>Example 2:</b>
Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.
</pre>