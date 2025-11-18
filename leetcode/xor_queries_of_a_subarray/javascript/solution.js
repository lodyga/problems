class Solution {
   /**
    * Time complexity: O(n+q)
    * Auxiliary space complexity: O(n)
    * Tags: prefix sum, prefix xor
    * @param {number[]} nums
    * @param {number[][]} queries
    * @return {number[]}
    */
   xorQueries(nums, queries) {
      const prefix = Array(nums.length + 1).fill(0);
      for (let index = 1; index <= nums.length; index++)
         prefix[index] = prefix[index - 1] ^ nums[index - 1];

      const response = [];
      for (const [start, end] of queries)
         response.push(prefix[end + 1] ^ prefix[start]);

      return response
   };
}


const xorQueries = new Solution().xorQueries;
console.log(new Solution().xorQueries([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]]), [2, 7, 14, 8])
console.log(new Solution().xorQueries([4, 8, 2, 10], [[2, 3], [1, 3], [0, 0], [0, 3]]), [8, 0, 4, 4])
