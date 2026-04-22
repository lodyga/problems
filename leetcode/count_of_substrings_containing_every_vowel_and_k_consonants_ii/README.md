# Count of Substrings Containing Every Vowel and K Consonants II
https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/

<p>
You are given a string word and a non-negative integer k.

Return the total number of of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.
</p>

<pre>
<b>Example 1:</b>
Input: word = "aeioqq", k = 1

Output: 0

Explanation:

There is no substring with every vowel.
</pre>

<pre>
<b>Example 2:</b>
Input: word = "aeiou", k = 0

Output: 1

Explanation:

The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".
</pre>

<pre>
<b>Example 3:</b>
Input: word = "ieaouqqieaouqq", k = 1

Output: 3

Explanation:

The substrings with every vowel and one consonant are:

    word[0..5], which is "ieaouq".
    word[6..11], which is "qieaou".
    word[7..12], which is "ieaouq".

</pre>