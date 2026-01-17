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
      return -1
   };
}


const search = new Solution().search;
console.log(new Solution().search([-1, 0, 3, 5, 9, 12], -1) === 0)
console.log(new Solution().search([-1, 0, 3, 5, 9, 12], 0) === 1)
console.log(new Solution().search([-1, 0, 3, 5, 9, 12], 3) === 2)
console.log(new Solution().search([-1, 0, 3, 5, 9, 12], 5) === 3)
console.log(new Solution().search([-1, 0, 3, 5, 9, 12], 9) === 4)
console.log(new Solution().search([-1, 0, 3, 5, 9, 12], 12) === 5)
console.log(new Solution().search([-1, 0, 3, 5, 9, 12], 2) === -1)
