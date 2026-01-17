class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy (Kadane)
    * @param {number[]} nums
    * @return {number}
    */
   maxSubArray(nums) {
      let subSum = 0;
      let maxSubSum = nums[0];

      for (const num of nums) {
         subSum > 0 ? subSum += num : subSum = num
         // subSum = Math.max(subSum + num, num);
         maxSubSum = Math.max(maxSubSum, subSum);
      }
      return maxSubSum
   };
}


const maxSubArray = new Solution().maxSubArray;
console.log(new Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) === 6)
console.log(new Solution().maxSubArray([1]) === 1)
console.log(new Solution().maxSubArray([5, 4, -1, 7, 8]) === 23)
console.log(new Solution().maxSubArray([-4, -2, -1, -3]) === -1)
