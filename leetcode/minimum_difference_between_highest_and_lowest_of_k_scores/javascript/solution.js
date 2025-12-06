class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: sorting
    * @param {number[]} nums
    * @param {number} k
    * @return {number}
    */
   minimumDifference(nums, k) {
      nums.sort((a, b) => a - b);
      let minDiff = nums[nums.length - 1];

      for (let index = 0; index < nums.length - k + 1; index++) {
         minDiff = Math.min(minDiff, nums[index + k - 1] - nums[index])
      }
      return minDiff
   };
}


const minimumDifference = new Solution().minimumDifference;
console.log(new Solution().minimumDifference([90], 1) === 0)
console.log(new Solution().minimumDifference([9, 4, 1, 7], 2) === 2)
console.log(new Solution().minimumDifference([87063, 61094, 44530, 21297, 95857, 93551, 9918], 6) === 74560)
