# Max Points on a Line
https://leetcode.com/problems/max-points-on-a-line/

<p>
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.
</p>

<pre>
<b>Example 1:</b>
y
5 | .  .  .  .  .  .
4 | .  .  .  .  .  .
3 | .  .  .  X  .  .
2 | .  .  X  .  .  .
1 | .  X  .  .  .  .
0 | .  .  .  .  .  .
    -----------------
      0  1  2  3  4  5   x
Input: points = [[1,1],[2,2],[3,3]]
Output: 3
</pre>

<pre>
<b>Example 2:</b>
y
5 | .  .  .  .  .  .
4 | .  X  .  .  .  .
3 | .  .  X  .  .  X
2 | .  .  .  X  .  .
1 | .  X  .  .  X  .
0 | .  .  .  .  .  .
    -----------------
      0  1  2  3  4  5   x
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
</pre>

<pre>
<b>Example 3:</b>
y
 5 | .  .  .  .  X  .
 4 | .  .  .  .  .  .
 3 | .  .  .  .  .  .
 2 | .  .  .  .  .  .
 1 | .  .  .  .  .  .
 0 | .  .  .  .  X  .
-1 | .  .  .  .  X  .
     -----------------
       0  1  2  3  4  5   x
Input: points = [[4,5],[4,-1],[4,0]]
Output: 3
</pre>