class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: two pointers, in-place method
    *     one pass
    * @param {number[]} nums
    * @return {number[]}
    */
   sortColors(nums) {
      let left = 0;
      let right = nums.length - 1;
      let idx = 0;

      while (idx <= right) {
         if (nums[idx] == 1) {
            idx++;
         } else if (nums[idx] === 0) {
            [nums[idx], nums[left]] = [nums[left], nums[idx]];
            left++;
            idx++;
         } else if (nums[idx] === 2) {
            [nums[idx], nums[right]] = [nums[right], nums[idx]];
            right--;
         }

      }

      // return nums;
   }
}


const sortColors = new Solution().sortColors;
console.log(new Solution().sortColors([2, 0, 1]).toString() === [0, 1, 2].toString())
console.log(new Solution().sortColors([2, 0, 2, 1, 1, 0]).toString() === [0, 0, 1, 1, 2, 2].toString())
