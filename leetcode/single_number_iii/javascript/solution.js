class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash set
    *     A: iteration
    * @param {number[]} nums
    * @return {number[]}
    */
   singleNumber(nums) {
      const numSet = new Set();

      for (const num of nums) {
         if (numSet.has(num)) {
            numSet.delete(num);
         } else {
            numSet.add(num);
         }
      }
      return [...numSet]
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: bit manipulation
    * @param {number[]} nums
    * @return {number[]}
    */
   singleNumber(nums) {
      let xor = 0;

      for (const num of nums) {
         xor ^= num;
      }

      let diffBit = 1;

      while ((xor & diffBit) === 0) {
         diffBit <<= 1;
      }

      const res = [0, 0];

      for (const num of nums) {
         if (num & diffBit) {
            res[1] ^= num;
         } else {
            res[0] ^= num;
         }
      }
      
      return res
   };
}

const singleNumber = new Solution().singleNumber;
console.log(new Solution().singleNumber([1, 2, 1, 3, 2, 5]).sort().toString() === [3, 5].sort().toString())
console.log(new Solution().singleNumber([-1, 0]).sort().toString() === [-1, 0].sort().toString())
console.log(new Solution().singleNumber([0, 1]).sort().toString() === [0, 1].sort().toString())
