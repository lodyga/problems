# All Possible Full Binary Trees
https://leetcode.com/problems/all-possible-full-binary-trees/

<p>
Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.
</p>

<pre>
<b>Example 1:</b>
Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
</pre>

<table>
  <tr>
    <td>
        <pre>
  0__
 /   \
0     0__
     /   \
    0     0
         / \
        0   0
        </pre>
    </td>
    <td>
        <pre>
  0______
 /       \
0       __0
       /   \
      0     0
     / \
    0   0
        </pre>
    </td>
    <td>
        <pre>
    __0__
   /     \
  0       0
 / \     / \
0   0   0   0
        </pre>
    </td>
    <td>
        <pre>
    ______0
   /       \
  0__       0
 /   \
0     0
     / \
    0   0
        </pre>
    </td>
    <td>
        <pre>
        __0
       /   \
    __0     0
   /   \
  0     0
 / \
0   0
        </pre>
    </td>
  </tr>
</table>

<pre>
<b>Example 2:</b>
Input: n = 3
Output: [[0,0,0]]
</pre>