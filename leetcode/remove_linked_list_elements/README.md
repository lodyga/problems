# Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/description/


Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.


<b>Example 1:</b>\
Input: head = [1,2,6,3,4,5,6], val = 6\
1 &rarr; 2 &rarr; 6 &rarr; 3 &rarr; 4 &rarr; 5 &rarr; 6\
Output: [1,2,3,4,5]

<b>Example 2:</b>\
Input: head = [], val = 1\
Output: []

<b>Example 2:</b>\
Input: head = [7,7,7,7], val = 7\
7 &rarr; 7 &rarr; 7 &rarr; 7\
Output: []