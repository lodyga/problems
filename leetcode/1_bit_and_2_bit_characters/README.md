# 1-bit and 2-bit Characters
https://leetcode.com/problems/1-bit-and-2-bit-characters/

We have two special characters:

    The first character can be represented by one bit 0.
    The second character can be represented by two bits (10 or 11).

Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.


<b>Example 1:</b>\
Input: bits = [1,0,0]\
Output: true\
Explanation: The only way to decode it is two-bit character and one-bit character.\
So the last character is one-bit character.


<b>Example 2:</b>\
Input: bits = [1,1,1,0]\
Output: false\
Explanation: The only way to decode it is two-b\
So the last character is not one-bit character.