# Valid Parenthesis String
https://leetcode.com/problems/valid-parenthesis-string/

<p>
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:
- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
</p>

<pre>
<b>Example 1:</b>
Input: s = "()"
Output: true
</pre>

<pre>
<b>Example 2:</b>
Input: s = "(*)"
Output: true
</pre>

<pre>
<b>Example 3:</b>
Input: s = "(*))"
Output: true
</pre>