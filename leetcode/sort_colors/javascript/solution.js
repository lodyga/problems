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
      let index = 0;

      while (index <= right) {
         if (nums[index] === 0) {
            [nums[index], nums[left]] = [nums[left], nums[index]];
            left++;
         } else if (nums[index] === 2) {
            [nums[index], nums[right]] = [nums[right], nums[index]];
            right--;
            index--;
         }
         index++;
      }
      return nums
   };
}


const sortColors = new Solution().sortColors;
console.log(new Solution().sortColors([2, 0, 1]).toString() === [0, 1, 2].toString())
console.log(new Solution().sortColors([2, 0, 2, 1, 1, 0]).toString() === [0, 0, 1, 1, 2, 2].toString())
