# Sign of the Product of an Array
https://leetcode.com/problems/sign-of-the-product-of-an-array/

<p>
Implement a function signFunc(x) that returns:

- 1 if x is positive.
- -1 if x is negative.
- 0 if x is equal to 0.

You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).
</p>

<pre>
<b>Example 1:</b>
Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1
</pre>

<pre>
<b>Example 2:</b>
Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0
</pre>

<pre>
<b>Example 3:</b>
Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1
</pre>