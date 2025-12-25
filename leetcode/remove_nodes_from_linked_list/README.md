# Remove Nodes From Linked List
https://leetcode.com/problems/remove-nodes-from-linked-list/description/


You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.


<b>Example 1:</b>\
Input: head = [5,2,13,3,8]\
5 &rarr; 2 &rarr; 13 &rarr; 3 &rarr; 8\
Output: [13,8]\
13 &rarr; 8\
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.

<b>Example 2:</b>\
Input: head = [1,1,1,1]\
1 &rarr; 1 &rarr; 1 &rarr; 1\
Output: [1,1,1,1]\
1 &rarr; 1 &rarr; 1 &rarr; 1\
Explanation: Every node has value 1, so no nodes are removed.