class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: sliding window
    * @param {number[]} nums
    * @param {number} x
    * @return {number}
    */
   minOperations(nums, x) {
      const total = nums.reduce((total, num) => total + num, 0);
      if (total === x) {
         return nums.length
      }
      const target = total - x;
      let windowLength = 0;
      let window = 0;
      let left = 0;

      for (let right = 0; right < nums.length; right++) {
         window += nums[right];

         while (
            left < right &&
            window > target
         ) {
            window -= nums[left];
            left++;
         }
         if (window === target) {
            windowLength = Math.max(windowLength, right - left + 1);
         }
      }
      return windowLength ? nums.length - windowLength : -1
   };
}


const minOperations = new Solution().minOperations;
console.log(new Solution().minOperations([1, 1, 4, 2, 3], 5) === 2)
console.log(new Solution().minOperations([5, 6, 7, 8, 9], 4) === -1)
console.log(new Solution().minOperations([3, 2, 20, 1, 1, 3], 10) === 5)
console.log(new Solution().minOperations([5, 2, 3, 1, 1], 5) === 1)
console.log(new Solution().minOperations([1, 2], 3) === 2)
console.log(new Solution().minOperations([1, 1], 3) === -1)
console.log(new Solution().minOperations([8828, 9581, 49, 9818, 9974, 9869, 9991, 10000, 10000, 10000, 9999, 9993, 9904, 8819, 1231, 6309], 134365) === 16)
