# Linked List in Binary Tree
https://leetcode.com/problems/linked-list-in-binary-tree/

Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.


<b>Example 1:</b>
<pre>
4 &rarr; 2 &rarr; 8

  ____1__________
 /               \
4__         ______4
   \       /
    2     2__
   /     /   \
  1     6     8
             / \
            1   3
</pre>
Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]\
Output: true\
Explanation: Nodes in blue form a subpath in the binary Tree.  


<b>Example 2:</b>
<pre>
1 &rarr; 4 &rarr; 2 &rarr; 6

  ____1__________
 /               \
4__         ______4
   \       /
    2     2__
   /     /   \
  1     6     8
             / \
            1   3
</pre>
Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]\
Output: true

<b>Example 3:</b>
<pre>
1 &rarr; 4 &rarr; 2 &rarr; 6 &rarr; 8

  ____1__________
 /               \
4__         ______4
   \       /
    2     2__
   /     /   \
  1     6     8
             / \
            1   3
</pre>
Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]\
Output: false\
Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.