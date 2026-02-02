# Maximum Difference Between Even and Odd Frequency I
https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/

<p>
You are given a string s consisting of lowercase English letters.

Your task is to find the maximum difference diff = freq(a1) - freq(a2) between the frequency of characters a1 and a2 in the string such that:

- a1 has an odd frequency in the string.
- a2 has an even frequency in the string.

Return this maximum difference.
</p>

<pre>
<b>Example 1:</b>
Input: s = "aaaaabbc"

Output: 3

Explanation:

The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
The maximum difference is 5 - 2 = 3.
</pre>

<pre>
<b>Example 2:</b>
Input: s = "abcabcab"

Output: 1

Explanation:

The character 'a' has an odd frequency of 3, and 'c' has an even frequency of 2.
The maximum difference is 3 - 2 = 1.
</pre>