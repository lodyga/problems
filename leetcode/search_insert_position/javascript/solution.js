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
   searchInsert(nums, target) {
      let left = 0;
      let right = nums.length - 1;

      while (left <= right) {
         const middle = (left + right) >> 1;
         const middleNum = nums[middle];

         if (target === middleNum) {
            return middle
         } else if (target < middleNum) {
            right = middle - 1;
         } else {
            left = middle + 1;
         }
      }
      return left
   };
}


const searchInsert = new Solution().searchInsert;
console.log(new Solution().searchInsert([1, 3, 5, 6], 1) === 0)
console.log(new Solution().searchInsert([1, 3, 5, 6], 3) === 1)
console.log(new Solution().searchInsert([1, 3, 5, 6], 5) === 2)
console.log(new Solution().searchInsert([1, 3, 5, 6], 6) === 3)
console.log(new Solution().searchInsert([1, 3, 5, 6], 0) === 0)
console.log(new Solution().searchInsert([1, 3, 5, 6], 2) === 1)
console.log(new Solution().searchInsert([1, 3, 5, 6], 4) === 2)
console.log(new Solution().searchInsert([1, 3, 5, 6], 7) === 4)
