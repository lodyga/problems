class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     A: binary search
    * @param {number[]} nums
    * @param {number} target
    * @return {number[]}
    */
   searchRange(nums, target) {
      let left = 0;
      let right = nums.length - 1;
      let starting = -1;

      while (left <= right) {
         const mid = (left + right) >> 1;
         const midNum = nums[mid];

         if (target <= midNum) {
            if (target == midNum)
               starting = mid;
            right = mid - 1;
         } else {
            left = mid + 1;
         }
      }

      left = 0;
      right = nums.length - 1;
      let ending = -1;

      while (left <= right) {
         const mid = (left + right) >> 1;
         const midNum = nums[mid];

         if (target >= midNum) {
            if (target == midNum)
               ending = mid;
            left = mid + 1;
         } else {
            right = mid - 1;
         }
      }
      return [starting, ending]
   };
}


const searchRange = new Solution().searchRange;
console.log(new Solution().searchRange([5, 5, 7], 5).toString() === [0, 1].toString())
console.log(new Solution().searchRange([5, 7, 7], 7).toString() === [1, 2].toString())
console.log(new Solution().searchRange([5, 7, 7, 8, 8, 10], 8).toString() === [3, 4].toString())
console.log(new Solution().searchRange([5, 7, 7, 8, 8, 10], 6).toString() === [-1, -1].toString())
console.log(new Solution().searchRange([], 0).toString() === [-1, -1].toString())
console.log(new Solution().searchRange([1], 1).toString() === [0, 0].toString())
