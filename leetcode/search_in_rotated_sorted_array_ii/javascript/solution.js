class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: almost binary search but not quite
    * @param {number[]} nums
    * @param {number} target
    * @return {boolean}
    */
   search(nums, target) {
      return nums.includes(target)
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: almost binary search but not quite
    * @param {number[]} nums
    * @param {number} target
    * @return {boolean}
    */
   search(nums, target) {
      let left = 0;
      let right = nums.length - 1;

      while (left <= right) {
         const mid = (left + right) >> 1;
         const midNum = nums[mid];

         if (target === midNum) {
            return true
         } else if (
            nums[left] === midNum && 
            midNum === nums[right]
         ) {
            left++;
            right--;
         } else if (midNum <= nums[right]) {
            if (
               midNum < target &&
               target <= nums[right]
            ) {
               left = mid + 1;
            }
            else {
               right = mid - 1;
            }

         } else {
            if (
               nums[left] <= target &&
               target < midNum
            ) {
               right = mid - 1;
            }
            else {
               left = mid + 1;
            }
         }
      }
      return false
   };
}


const search = new Solution().search;
console.log(new Solution().search([1, 2, 3, 4, 5], 2) === true)
console.log(new Solution().search([2, 5, 6, 0, 0, 1, 2], 0) === true)
console.log(new Solution().search([2, 5, 6, 0, 0, 1, 2], 3) === false)
console.log(new Solution().search([1], 0) === false)
console.log(new Solution().search([0, 1], 0) === true)
console.log(new Solution().search([1, 0], 0) === true)
console.log(new Solution().search([0, 1], 1) === true)
console.log(new Solution().search([1, 0], 1) === true)
console.log(new Solution().search([0, 1, 1], 0) === true)
console.log(new Solution().search([1, 0, 1, 1, 1], 0) === true)
console.log(new Solution().search([1, 0, 0], 1) === true)
console.log(new Solution().search([1, 2, 1], 1) === true)
console.log(new Solution().search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], 2) === true)
