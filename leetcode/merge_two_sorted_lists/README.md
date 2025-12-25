# Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/description/


You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


<b>Example 1:</b>\
Input: list1 = [1,2,4]\
1 &rarr; 2 &rarr; 4\
list2 = [1,3,4]\
1 &rarr; 3 &rarr; 4\
Output: [1,1,2,3,4,4]\
1 &rarr; 1 &rarr; 2 &rarr; 4 &rarr; 4 &rarr; 4

<b>Example 2:</b>\
Input: list1 = [], list2 = []\
Output: []

<b>Example 3:</b>\
Input: list1 = [], list2 = [0]\
Output: [0]