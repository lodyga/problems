# Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/


Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


<b>Example 1:</b>\
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
<pre>
                 _
3        _      | |_   _
2    _  | |~ ~ ~|   |~| |_
1  _|_|~|___|~|___________|
   0 1 2 3 4 5 6 7 8 9 . :
</pre>
Output: 6\
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

<b>Example 2:</b>\
Input: height = [4,2,0,3,2,5]
<pre>
              _
5   _        | |
4  | |~ ~ ~ ~| |
3  | |~ ~| |~| |
2  |   |~|     |
1  |___|~|_____|
    0 1 2 3 4 5
</pre>
Output: 9