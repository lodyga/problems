class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy
    * @param {number[]} nums
    * @return {number}
    */
   maxSubArray(nums) {
      let subSum = 0;
      let res = nums[0];

      for (const num of nums) {
         subSum > 0 ? subSum += num : subSum = num
         res = Math.max(res, subSum);
      }
      return res
   };
}


const maxSubArray = new Solution().maxSubArray;
console.log(new Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) === 6)
console.log(new Solution().maxSubArray([1]) === 1)
console.log(new Solution().maxSubArray([5, 4, -1, 7, 8]) === 23)
console.log(new Solution().maxSubArray([-4, -2, -1, -3]) === -1)
