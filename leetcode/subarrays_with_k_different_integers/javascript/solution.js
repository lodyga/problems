class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map
    *     A: sliding window
    * @param {number[]} nums
    * @param {number} k
    * @return {number}
    */
   subarraysWithKDistinct(nums, k) {
      const numFreq = new Map();
      let left = 0;
      let right = 0;
      let res = 0;

      for (const num of nums) {
         numFreq.set(num, (numFreq.get(num) || 0) + 1);

         if (numFreq.size < k) {
            continue;
         }

         if (numFreq.size > k) {
            numFreq.delete(nums[right]);
            right++;
            left = right;
         }

         while (numFreq.get(nums[right]) > 1) {
            numFreq.set(nums[right], numFreq.get(nums[right]) - 1);
            right++;
         }

         res += right - left + 1;
      }

      return res;
   }
}


const subarraysWithKDistinct = new Solution().subarraysWithKDistinct;
console.log(new Solution().subarraysWithKDistinct([1, 2, 1, 2, 3], 2) === 7)
console.log(new Solution().subarraysWithKDistinct([1, 2, 1, 3, 4], 3) === 3)
