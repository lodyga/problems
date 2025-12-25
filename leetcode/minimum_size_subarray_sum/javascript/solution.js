class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     A: sliding window
    * @param {number} target
    * @param {number[]} nums
    * @return {number}
    */
   minSubArrayLen(target, nums) {
      let windowSum = 0;
      let left = 0;
      let windowLength = nums.length + 1;

      for (let right = 0; right < nums.length; right++) {
         windowSum += nums[right];

         while (windowSum >= target) {
            windowLength = Math.min(windowLength, right - left + 1);
            windowSum -= nums[left];
            left++;
         }
      }
      return windowLength === nums.length + 1 ? 0 : windowLength
   };
}


const minSubArrayLen = new Solution().minSubArrayLen;
console.log(new Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) === 2)
console.log(new Solution().minSubArrayLen(4, [1, 4, 4]) === 1)
console.log(new Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) === 0)
