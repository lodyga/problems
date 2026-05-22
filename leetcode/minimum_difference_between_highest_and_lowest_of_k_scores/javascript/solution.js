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
      let minVal = nums[k - 1] - nums[0];

      for (let idx = k; idx < nums.length + 1; idx++) {
         const right = idx - 1;
         const left = idx - k;
         minVal = Math.min(minVal, nums[right] - nums[left]);
      }

      return minVal
   }
}


const minimumDifference = new Solution().minimumDifference;
console.log(new Solution().minimumDifference([90], 1) === 0)
console.log(new Solution().minimumDifference([9, 4, 1, 7], 2) === 2)
console.log(new Solution().minimumDifference([9, 4, 1, 7], 3) === 5)
console.log(new Solution().minimumDifference([87063, 61094, 44530, 21297, 95857, 93551, 9918], 6) === 74560)
