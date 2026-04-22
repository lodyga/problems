class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash set
    *     A: iteration
    * @param {number[]} nums
    * @param {number} diff
    * @return {number}
    */
   arithmeticTriplets(nums, diff) {
      const numSet = new Set(nums);
      let res = 0;

      for (const num of nums) {
         if (
            numSet.has(num - diff) &&
            numSet.has(num - 2 * diff)
         ) {
            res++;
         }
      }

      return res
   };
}


const arithmeticTriplets = new Solution().arithmeticTriplets;
console.log(new Solution().arithmeticTriplets([0, 1, 4, 6, 7, 10], 3) === 2)
console.log(new Solution().arithmeticTriplets([4, 5, 6, 7, 8, 9], 2) === 2)
