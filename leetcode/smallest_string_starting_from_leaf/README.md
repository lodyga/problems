# Smallest String Starting From Leaf
https://leetcode.com/problems/smallest-string-starting-from-leaf/

<p>
You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

- For example, "ab" is lexicographically smaller than "aba".

A leaf of a node is a node that has no children.
</p>

<pre>
<b>Example 1:</b>
Input: root = [0,1,2,3,4,3,4]
     ___a*__
    /       \
  _b*        c
 /   \      / \
d*    e    d   e

Output: "dba"
</pre>

<pre>
<b>Example 2:</b>
Input: root = [25,1,3,1,3,0,2]
    __z*___
   /       \
  b        _d*
 / \      /   \
b   d    a*    c

Output: "adz"
</pre>

<pre>
<b>Example 3:</b>
Input: root = [2,2,1,null,1,0,null,0]
  ____c*___
 /         \
c__        _b*
   \      /
    b    a*
   /
  a

Output: "abc"
</pre>