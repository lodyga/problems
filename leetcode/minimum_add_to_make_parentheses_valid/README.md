# Minimum Add to Make Parentheses Valid
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

<p>
A parentheses string is valid if and only if:

- It is the empty string,
- It can be written as AB (A concatenated with B), where A and B are valid strings, or
- It can be written as (A), where A is a valid string.

You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

- For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".

Return the minimum number of moves required to make s valid.
</p>

<pre>
<b>Example 1:</b>
Input: s = "())"
Output: 1
</pre>

<pre>
<b>Example 2:</b>
Input: s = "((("
Output: 3
</pre>

<pre>
<b>Example 3:</b>
Input: s = "()))(("
Output: 4
</pre>