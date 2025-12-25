# Find the Town Judge
https://leetcode.com/problems/find-the-town-judge/description/

<p>
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
</p>

<pre>
<b>Example 1:</b>
Input: n = 2, trust = [[1,2]]
Output: 2
</pre>

<pre>
<b>Example 2:</b>
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
</pre>

<pre>
<b>Example 3:</b>
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
</pre>