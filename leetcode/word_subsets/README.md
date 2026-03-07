# Word Subsets
https://leetcode.com/problems/word-subsets/

<p>
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

- For example, "wrr" is a subset of "warrior" but is not a subset of "world".

A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.
</p>

<pre>
<b>Example 1:</b>
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]

Output: ["facebook","google","leetcode"]
</pre>

<pre>
<b>Example 2:</b>
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["lc","eo"]

Output: ["leetcode"]
</pre>

<pre>
<b>Example 3:</b>
Input: words1 = ["acaac","cccbb","aacbb","caacc","bcbbb"], words2 = ["c","cc","b"]

Output: ["cccbb"]
</pre>