class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: two pointers
    * @param {number[]} nums
    * @param {number} target
    * @return {number[]}
    */
   twoSum(nums, target) {
      let left = 0;
      let right = nums.length - 1;

      while (left < right) {
         const pair = nums[left] + nums[right];

         if (target === pair) {
            return [left + 1, right + 1]
         } else if (target < pair) {
            right--;
         } else {
            left++;
         }
      }
   }
};


const twoSum = new Solution().twoSum;
console.log(new Solution().twoSum([2, 7, 11, 15], 9), [1, 2])
console.log(new Solution().twoSum([2, 3, 4], 6), [1, 3])
console.log(new Solution().twoSum([-1, 0], -1), [1, 2])
