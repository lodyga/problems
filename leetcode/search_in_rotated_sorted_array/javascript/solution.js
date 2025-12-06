class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     A: binary search
    * @param {number[]} nums
    * @param {number} target
    * @return {number}
    */
   search(nums, target) {
      let left = 0;
      let right = nums.length - 1;

      while (left <= right) {
         let middle = (left + right) >> 1;
         const middleNum = nums[middle];

         if (target === middleNum) {
            return middle
         }
         // right side portion is contiguous
         else if (middleNum < nums[right]) {
            if (
               middleNum < target &&
               target <= nums[right]
            ) {
               left = ++middle;
            } else {
               right = --middle;
            }
         }
         // left side portion is contiguous
         else {
            if (
               nums[left] <= target &&
               target < middleNum
            ) {
               right = --middle;
            } else {
               left = ++middle;
            }
         }
      }
      return -1
   };
}


const search = new Solution().search;
console.log(new Solution().search([1, 3, 5], 5) === 2)
console.log(new Solution().search([3, 5, 1], 3) === 0)
console.log(new Solution().search([3, 5, 1], 1) === 2)
console.log(new Solution().search([4, 5, 6, 7, 8, 1, 2, 3], 8) === 4)
console.log(new Solution().search([5, 1, 3], 3) === 2)
console.log(new Solution().search([4, 5, 6, 7, 0, 1, 2], 0) === 4)
console.log(new Solution().search([4, 5, 6, 7, 0, 1, 2], 3) === -1)
console.log(new Solution().search([1], 0) === -1)
console.log(new Solution().search([5, 1, 3], 4) === -1)
console.log(new Solution().search([4, 5, 6, 7, 8, 1, 2, 3], 8) === 4)
