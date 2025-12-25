class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *    A: two pointers, in-place method
    * @param {number[]} nums
    * @param {number} val
    * @return {number}
    */
   removeElement(nums, val) {
      let left = 0;

      for (let right = 0; right < nums.length; right++) {
         if (nums[right] !== val) {
            [nums[left], nums[right]] = [nums[right], nums[left]];
            left++;
         }
      }
      return left
   };
}


const removeElement = new Solution().removeElement;
console.log(new Solution().removeElement([3, 2, 2, 3], 3) === 2)
console.log(new Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) === 5)
