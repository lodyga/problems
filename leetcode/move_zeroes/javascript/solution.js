class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     A: two pointers, in-place method
    * @param {number[]} nums
    * @return {number[]}
    */
   moveZeroes(nums) {
      let left = 0;

      for (let right = 0; right < nums.length; right++) {
         if (nums[right] !== 0) {
            [nums[left], nums[right]] = [nums[right], nums[left]];
            left++;
         }
      }
      return nums
   };
}


const moveZeroes = new Solution().moveZeroes;
console.log(JSON.stringify(new Solution().moveZeroes([0])) === JSON.stringify([0]))
console.log(JSON.stringify(new Solution().moveZeroes([1])) === JSON.stringify([1]))
console.log(JSON.stringify(new Solution().moveZeroes([0, 1, 0, 3, 12])) === JSON.stringify([1, 3, 12, 0, 0]))
