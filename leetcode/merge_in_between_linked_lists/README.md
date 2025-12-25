# Merge In Between Linked Lists
https://leetcode.com/problems/merge-in-between-linked-lists/description/


You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:

Build the result list and return its head.


<b>Example 1:</b>\
Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]\
list1: 10 &rarr; 1 &rarr; 13 &rarr; 6 &rarr; 9 &rarr; 5\
list2: 1000000 &rarr; 1000001 &rarr; 1000002\
Output: [10,1,13,1000000,1000001,1000002,5]\
10 &rarr; 1 &rarr; 13 &rarr; 1000000 &rarr; 1000001 &rarr; 1000002 &rarr; 5\
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.

<b>Example 2:</b>\
Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]\
list1: 0 &rarr; 1 &rarr; 2 &rarr; 3 &rarr; 4 &rarr; 5 &rarr; 6\
list2: 1000000 &rarr; 1000001 &rarr; 1000002 &rarr; 1000003 &rarr; 1000004\
Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]\
0 &rarr; 1 &rarr; 1000000 &rarr; 1000001 &rarr; 1000002 &rarr; 1000003 &rarr; 1000004 &rarr; 6\
Explanation: The blue edges and nodes in the above figure indicate the result.