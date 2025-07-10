# Delete Node in a BST
https://leetcode.com/problems/delete-node-in-a-bst/

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
 

<b>Example 1:</b>\
Input: root = [5,3,6,2,4,null,7], key = 3
<pre>
    __5
   /   \
  3     6
 / \     \
2   4     7
</pre>
Output: [5,4,6,2,null,null,7]
<pre>
    5
   / \
  4   6
 /     \
2       7
</pre>
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.\

<b>Example 2:</b>\
Input: root = [5,3,6,2,4,null,7], key = 0\
Output: [5,3,6,2,4,null,7]\
Explanation: The tree does not contain a node with value = 0.

<b>Example 3:</b>\
Input: root = [], key = 0\
Output: []