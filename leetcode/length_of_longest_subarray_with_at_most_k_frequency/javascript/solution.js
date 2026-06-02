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
      const numFreq = new Map();
      let left = 0;
      let res = 0;

      for (let right = 0; right < nums.length; right++) {
         const num = nums[right];

         numFreq.set(num, (numFreq.get(num) || 0) + 1);

         while (numFreq.get(num) > k) {
            const leftNum = nums[left];
            numFreq.set(leftNum, numFreq.get(leftNum) - 1);
            
            if (numFreq.get(leftNum) === 0) {
               numFreq.delete(leftNum);
            }

            left++;
         }

         res = Math.max(res, right - left + 1);
      }

      return res;
   }
}


const maxSubarrayLength = new Solution().maxSubarrayLength;
console.log(new Solution().maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2) === 6)
console.log(new Solution().maxSubarrayLength([1, 2, 1, 2, 1, 2, 1, 2], 1) === 2)
console.log(new Solution().maxSubarrayLength([5, 5, 5, 5, 5, 5, 5], 4) === 4)
console.log(new Solution().maxSubarrayLength([1, 1, 2], 2) === 3)
console.log(new Solution().maxSubarrayLength([1, 4, 4, 3], 1) === 2)
