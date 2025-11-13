class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: greedy, prefix sum
    * @param {number[]} nums
    * @return {number}
    */
   minimizeArrayValue(nums) {
      let maxValue = nums[0];
      let prefix = 0;

      for (let index = 0; index < nums.length; index++) {
         const num = nums[index];
         prefix += num;
         if (num <= maxValue)
            continue

         maxValue = Math.max(maxValue, Math.ceil(prefix / (index + 1)))
      }

      return maxValue
   };
}


const minimizeArrayValue = new Solution().minimizeArrayValue;
console.log(new Solution().minimizeArrayValue([3, 7, 1, 6]) === 5);
console.log(new Solution().minimizeArrayValue([10, 1]) === 10);
console.log(new Solution().minimizeArrayValue([13, 13, 20, 0, 8, 9, 9]) === 16);
