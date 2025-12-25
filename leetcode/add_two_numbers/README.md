# Add Two Numbers
https://leetcode.com/problems/add-two-numbers/description/


You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


<b>Example 1:</b>\
Input: l1 = [2,4,3], l2 = [5,6,4]\
l1: 2 &rarr; 4 &rarr; 3\
l2: 5 &rarr; 6 &rarr; 4\
Output: [7,0,8]\
7 &rarr; 0 &rarr; 8\
Explanation: 342 + 465 = 807.

<b>Example 2:</b>\
Input: l1 = [0], l2 = [0]\
Output: [0]

<b>Example 3:</b>\
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]\
l1: 9 &rarr; 9 &rarr; 9 &rarr; 9 &rarr; 9 &rarr; 9 &rarr; 9\
l2: 9 &rarr; 9 &rarr; 9 &rarr; 9\
Output: [8,9,9,9,0,0,0,1]
8 &rarr; 9 &rarr; 9 &rarr; 9 &rarr; 0 &rarr; 0 &rarr; 0 &rarr; 1