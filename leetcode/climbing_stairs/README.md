# Climbing Stairs
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


### blueprint:
<pre>
             ___5
           _| 4
         _| 3
       _| 2: 
     _| 1: 1
____| 0: 0


           ___ 4
         _|  3
       _|  2
     _|  1
____|

         ___ 3
       _|  2
     _|  1
____|


Adding steps
                   0
             /1          \2
            1             2
        /1     \2      /1   \2
       2        3     3      4
     /1  \2    /1    /1
   3      4   4     4
  /1
 4

Subtracting steps
                   4
             /1          \2
            3             2
        /1     \2      /1   \2
       2        1     1      0
     /1  \2    /1    /1
   1      0   0     0
  /1
 0


5 -> 8 = 5 + 3
4 -> 5 = 3 + 2
3 -> 3 = 2 + 1
2 -> 2
1 -> 1
0 -> 0
</pre>
Fibonnacci problem
