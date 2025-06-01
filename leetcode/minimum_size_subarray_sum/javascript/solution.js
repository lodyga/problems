class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: sliding window
    * @param {number} target
    * @param {number[]} numbers
    * @return {number}
    */
   minSubArrayLen(target, numbers) {
      let left = 0;
      let windowSum = 0;
      let windowLength = numbers.length + 1;

      for (let right = 0; right < numbers.length; right++) {
         windowSum += numbers[right];

         while (windowSum > target) {
            windowSum -= numbers[left];
            left++;
         }
         if (windowSum === target) {
            windowLength = Math.min(windowLength, right - left + 1);
         }
      }
      return windowLength === numbers.length + 1 ? 0 : windowLength
   };
}
const minSubArrayLen = new Solution().minSubArrayLen;


console.log(new Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2)
console.log(new Solution().minSubArrayLen(4, [1, 4, 4]) == 1)
console.log(new Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0)