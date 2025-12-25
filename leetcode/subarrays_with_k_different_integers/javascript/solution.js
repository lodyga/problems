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
      // {number: frequency}
      const window = new Map();
      let left = 0;
      let farLeft = 0;
      let counter = 0;

      for (const num of nums) {
         window.set(num, (window.get(num) || 0) + 1);

         if (window.size > k) {
            window.delete(nums[left]);
            left++;
            farLeft = left;
         }

         while (window.get(nums[left]) > 1) {
            window.set(nums[left], window.get(nums[left]) - 1);
            left++;
         }

         if (window.size === k) {
            counter += left - farLeft + 1;
         }
      }
      return counter
   };
}


const subarraysWithKDistinct = new Solution().subarraysWithKDistinct;
console.log(new Solution().subarraysWithKDistinct([1, 2, 1, 2, 3], 2) === 7)
console.log(new Solution().subarraysWithKDistinct([1, 2, 1, 3, 4], 3) === 3)
