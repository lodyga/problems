# Destination City
https://leetcode.com/problems/destination-city/description/

You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

<b>Example 1:</b>\
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]\
Output: "Sao Paulo"\
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

<b>Example 2:</b>\
Input: paths = [["B","C"],["D","B"],["C","A"]]\
Output: "A"\
Explanation: All possible trips are:
- "D" -> "B" -> "C" -> "A". 
- "B" -> "C" -> "A". 
- "C" -> "A". 
- "A". 

Clearly the destination city is "A".

<b>Example 3:</b>\
Input: paths = [["A","Z"]]\
Output: "Z"