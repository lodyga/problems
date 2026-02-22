class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: list
    *     A: bit manipulation, prefix sum
    * @param {number[]} nums
    * @param {number} maximumBit
    * @return {number[]}
    */
   getMaximumXor(nums, maximumBit) {
      const k = (1 << maximumBit) - 1;
      let xor = 0;
      const res = [];

      for (const num of nums) {
         xor ^= num;
         res.push(xor ^ k);
      }

      return res.reverse()
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: list
    *     A: bit manipulation, prefix sum
    * @param {number[]} nums
    * @param {number} maximumBit
    * @return {number[]}
    */
   getMaximumXor(nums, maximumBit) {
      const k = (1 << maximumBit) - 1;
      let xor = 0;
      const res = [];

      for (const num of nums) {
         xor ^= num;
      }

      for (const num of nums.reverse()) {
         res.push(xor ^ k);
         xor ^= num;
      }
      
      return res
   };
}


const getMaximumXor = new Solution().getMaximumXor;
console.log(new Solution().getMaximumXor([0, 1, 1, 3], 2).toString() === [0, 3, 2, 3].toString())
console.log(new Solution().getMaximumXor([2, 3, 4, 7], 3).toString() === [5, 2, 6, 5].toString())
console.log(new Solution().getMaximumXor([0, 1, 2, 2, 5, 7], 3).toString() === [4, 3, 6, 4, 6, 7].toString())
