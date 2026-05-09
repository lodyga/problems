# Walls and Gates
https://neetcode.io/problems/islands-and-treasure

<p>
You are given an m x n grid rooms initialized with these three possible values.

- -1 A wall or an obstacle.
- 0 A gate.
- INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
</p>

<pre>
<b>Example 1:</b>

┌─────────┐          ┌─────────┐
│ ∞ ■ · ∞ │          │ 3 ■ 0 1 │
│ ∞ ∞ ∞ ■ │    =>    │ 2 2 1 ■ │
│ ∞ ■ ∞ ■ │          │ 1 ■ 2 ■ │
│ · ■ ∞ ∞ │          │ 0 ■ 3 4 │
└─────────┘          └─────────┘

Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]


Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]
</pre>

<pre>
<b>Example 2:</b>

┌─────┐         ┌─────┐
│ · ■ │    =>   │ 0 ■ │
│ ∞ ∞ │         │ 1 2 │
└─────┘         └─────┘

Input: [
  [0,-1],
  [2147483647,2147483647]
]

Output: [
  [0,-1],
  [1,2]
]
</pre>

<pre>
<b>Example 3:</b>

┌───┐
│ ■ │
└───┘

Input: rooms = [[-1]]
Output: [[-1]]
</pre>
