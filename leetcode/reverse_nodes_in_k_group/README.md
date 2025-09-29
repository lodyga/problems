# Reverse Nodes in k-Group
https://leetcode.com/problems/reverse-nodes-in-k-group/

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.


<b>Example 1:</b>\
1 &rarr; 2 &rarr; 3 &rarr; 4 &rarr; 5\
Input: head = [1,2,3,4,5], k = 2\
2 &rarr; 1 &rarr; 4 &rarr; 3 &rarr; 5\
Output: [2,1,4,3,5]

<b>Example 2:</b>\
1 &rarr; 2 &rarr; 3 &rarr; 4 &rarr; 5\
Input: head = [1,2,3,4,5], k = 3\
3 &rarr; 2 &rarr; 1 &rarr; 4 &rarr; 5\
Output: [3,2,1,4,5]