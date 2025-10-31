# Check If a String Contains All Binary Codes of Size K
https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.


<b>Example 1:</b>\
Input: s = "00110110", k = 2\
Output: true\
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.

<b>Example 2:</b>\
Input: s = "0110", k = 1\
Output: true\
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 

<b>Example 3:</b>\
Input: s = "0110", k = 2\
Output: false\
Explanation: The binary code "00" is of length 2 and does not exist in the array.