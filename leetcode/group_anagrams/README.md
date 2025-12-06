# Group Anagrams
https://leetcode.com/problems/group-anagrams/description/


Given an array of strings strs, group the
together. You can return the answer in any order.


<b>Example 1:</b>\
Input: strs = ["eat","tea","tan","ate","nat","bat"]\
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]\
Explanation:
- There is no string in strs that can be rearranged to form "bat".
- The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
- The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

<b>Example 2:</b>\
Input: strs = [""]\
Output: [[""]]

<b>Example 3:</b>\
Input: strs = ["a"]\
Output: [["a"]]