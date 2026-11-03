class Solution2 {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: brute-froce
    * @param {number[]} nums
    * @return {number}
    */
   maxSubarraySumCircular(nums) {
      const N = nums.length;
      let res = nums[0];

      for (let idx = 0; idx < N; idx++) {
         let currSum = 0;

         for (let jdx = idx; jdx < N + idx; jdx++) {
            currSum += nums[jdx % N]
            res = Math.max(res, currSum);
         }
      }

      return res;
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy
    * @param {number[]} nums
    * @return {number}
    */
   maxSubarraySumCircular(nums) {
      let localMaxSum = 0;
      let localMinSum = 0;
      let globalMaxSum = nums[0];
      let globlaMinSum = nums[0];
      let total = nums.reduce((total, val) => total + val, 0);

      for (const num of nums) {
         localMaxSum = Math.max(localMaxSum + num, num);
         globalMaxSum = Math.max(globalMaxSum, localMaxSum);

         localMinSum = Math.min(localMinSum + num, num);
         globlaMinSum = Math.min(globlaMinSum, localMinSum);
      }

      if (globalMaxSum > 0) {
         return Math.max(globalMaxSum, total - globlaMinSum);
      }
      else {
         return globalMaxSum;
      }
   }
}


const maxSubarraySumCircular = new Solution().maxSubarraySumCircular;
console.log(new Solution().maxSubarraySumCircular([1, -2, 3, -2]) === 3)
console.log(new Solution().maxSubarraySumCircular([5, -3, 5]) === 10)
console.log(new Solution().maxSubarraySumCircular([-3, -2, -3]) === -2)
console.log(new Solution().maxSubarraySumCircular([-1, -2, -3]) === -1)
console.log(new Solution().maxSubarraySumCircular([-2, 4, -5, 4, -5, 9, 4]) === 15)
console.log(new Solution().maxSubarraySumCircular([3, 1, 3, 2, 6]) === 15)
console.log(new Solution().maxSubarraySumCircular([0, 5, 8, -9, 9, -7, 3, -2]) === 16)
