class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy (Kadane)
    * @param {number[]} nums
    * @return {number}
    */
   maxAbsoluteSum(nums) {
      let positiveSum = 0;
      let maxPositive = nums[0];

      let negative_sum = 0;
      let minNegative = nums[0];

      for (const num of nums) {
         positiveSum = Math.max(positiveSum + num, num)
         maxPositive = Math.max(maxPositive, positiveSum)

         negative_sum = Math.min(negative_sum + num, num);
         minNegative = Math.min(minNegative, negative_sum);
      }

      return Math.max(maxPositive, -minNegative);
   };
}


const maxAbsoluteSum = new Solution().maxAbsoluteSum;
console.log(new Solution().maxAbsoluteSum([1, -3, 2, 3, -4]) === 5)
console.log(new Solution().maxAbsoluteSum([2, -5, 1, -4, 3, -2]) === 8)
console.log(new Solution().maxAbsoluteSum([-1, 5]) === 5)
