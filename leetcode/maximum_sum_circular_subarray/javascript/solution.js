class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy, Kadane
    * @param {number[]} nums
    * @return {number}
    */
   maxSubarraySumCircular(nums) {
      let currentMax = 0;
      let currentMin = 0;
      let largestSum = nums[0];
      let smallestSum = nums[0];
      let total = 0;

      for (const number of nums) {
         if (currentMax < 0)
            currentMax = 0
         currentMax += number;
         largestSum = Math.max(largestSum, currentMax);

         if (currentMin > 0)
            currentMin = 0
         currentMin += number;
         smallestSum = Math.min(smallestSum, currentMin);

         total += number;
      }
      if (largestSum < 0)
         return largestSum
      else
         return Math.max(largestSum, total - smallestSum)
   };
}


const maxSubarraySumCircular = new Solution().maxSubarraySumCircular;
console.log(new Solution().maxSubarraySumCircular([1, -2, 3, -2]) === 3)
console.log(new Solution().maxSubarraySumCircular([5, -3, 5]) === 10)
console.log(new Solution().maxSubarraySumCircular([-3, -2, -3]) === -2)
console.log(new Solution().maxSubarraySumCircular([-1, -2, -3]) === -1)
console.log(new Solution().maxSubarraySumCircular([-2, 4, -5, 4, -5, 9, 4]) === 15)
console.log(new Solution().maxSubarraySumCircular([3, 1, 3, 2, 6]) === 15)
console.log(new Solution().maxSubarraySumCircular([0, 5, 8, -9, 9, -7, 3, -2]) === 16)
