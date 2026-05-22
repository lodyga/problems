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
      const N = nums.length;

      if (total < x) {
         return -1;
      } else if (total === x) {
         return nums.length;
      }

      const target = total - x;
      let left = 0;
      let windowSum = 0;
      let windowLength = -1;

      for (let right = 0; right < nums.length; right++) {
         windowSum += nums[right];

         while (windowSum > target) {
            windowSum -= nums[left];
            left++;
         }

         if (windowSum === target) {
            windowLength = Math.max(windowLength, right - left + 1);
         }
      }

      return windowLength === -1 ? -1 : N - windowLength;
   }
}


const minOperations = new Solution().minOperations;
console.log(new Solution().minOperations([1, 1, 4, 2, 3], 5) === 2)
console.log(new Solution().minOperations([5, 6, 7, 8, 9], 4) === -1)
console.log(new Solution().minOperations([3, 2, 20, 1, 1, 3], 10) === 5)
console.log(new Solution().minOperations([5, 2, 3, 1, 1], 5) === 1)
console.log(new Solution().minOperations([1, 2], 3) === 2)
console.log(new Solution().minOperations([1, 1], 3) === -1)
console.log(new Solution().minOperations([8828, 9581, 49, 9818, 9974, 9869, 9991, 10000, 10000, 10000, 9999, 9993, 9904, 8819, 1231, 6309], 134365) === 16)
