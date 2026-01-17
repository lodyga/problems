class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(k)
    * Tags:
    *     DS: hash map
    *     A: sliding window
    * @param {number[]} nums
    * @param {number} k
    * @return {number}
    */
   maxSubarrayLength(nums, k) {
      const window = new Map();  // {number: frequency}
      let left = 0;
      let subarrayLen = 0;

      for (let right = 0; right < nums.length; right++) {
         const num = nums[right];

         window.set(num, (window.get(num) || 0) + 1);

         while (window.get(num) > k) {
            const leftNum = nums[left];
            window.set(leftNum, window.get(leftNum) - 1);
            if (window.get(leftNum) === 0)
               window.delete(leftNum);
            left++;
         }

         subarrayLen = Math.max(subarrayLen, right - left + 1);
      }
      return subarrayLen
   };
}


const maxSubarrayLength = new Solution().maxSubarrayLength;
console.log(new Solution().maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2) === 6)
console.log(new Solution().maxSubarrayLength([1, 2, 1, 2, 1, 2, 1, 2], 1) === 2)
console.log(new Solution().maxSubarrayLength([5, 5, 5, 5, 5, 5, 5], 4) === 4)
console.log(new Solution().maxSubarrayLength([1, 1, 2], 2) === 3)
console.log(new Solution().maxSubarrayLength([1, 4, 4, 3], 1) === 2)
