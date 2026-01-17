# Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/

<p>
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
</p>

<pre>
<b>Example 1:</b>
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
</pre>

<pre>
<b>Example 2:</b>
Input: lists = []
Output: []
</pre>

<pre>
<b>Example 3:</b>
Input: lists = [[]]
Output: []
</pre>