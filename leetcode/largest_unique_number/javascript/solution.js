class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map
    *     A: iteration
    * @param {number[]} nums
    * @return {number}
    */
   largestUniqueNumber(nums) {
      const numFreq = new Map();
      let res = -1;

      for (const num of nums) {
         numFreq.set(num, (numFreq.get(num) || 0) + 1);
      }

      for (const [num, freq] of numFreq.entries()) {
         if (freq === 1) {
            res = Math.max(res, num);
         }
      }

      return res
   };
}


const largestUniqueNumber = new Solution().largestUniqueNumber;
console.log(new Solution().largestUniqueNumber([5, 7, 3, 9, 4, 9, 8, 3, 1]) === 8)
console.log(new Solution().largestUniqueNumber([9, 9, 8, 8]) === -1)
