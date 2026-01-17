class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags:
    *    A: binary search
    * @param {number[]} nums
    * @return {number}
    */
   findPeakElement(nums) {
      let left = 0;
      let right = nums.length - 1;

      while (left <= right) {
         const middle = (left + right) >> 1;
         const middleNum = nums[middle];

         if (
            (middle === left || nums[middle - 1] < middleNum) &&
            (middle === right || middleNum > nums[middle + 1])
         ) {
            return middle
         } else if (
            middle === left ||
            middleNum < nums[middle + 1]
         ) {
            left = middle + 1;
         } else {
            right = middle - 1;
         }
      }
   };
}


const findPeakElement = new Solution().findPeakElement;
console.log(new Solution().findPeakElement([1, 2, 3, 1]) === 2)
console.log(new Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]) === 5)
console.log(new Solution().findPeakElement([1]) === 0)
console.log(new Solution().findPeakElement([1, 2]) === 1)
