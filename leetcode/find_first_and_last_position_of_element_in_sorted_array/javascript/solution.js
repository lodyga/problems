class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags: binary search
    * @param {number[]} numbers
    * @param {number} target
    * @return {number[]}
    */
   searchRange(numbers, target) {
      let left = 0;
      let right = numbers.length - 1;
      let lowerBound = -1;
      
      while (left <= right) {
         const middle = (left + right) >> 1;
         const middleNumber = numbers[middle];

         if (middleNumber === target) {
            lowerBound = middle;
            right = middle - 1;
         } else if (middleNumber > target) {
            right = middle - 1;
         } else {
            left = middle + 1;
         }
      }
      
      left = 0;
      right = numbers.length - 1;
      let upperBound = -1;

      while (left <= right) {
         const middle = (left + right) >> 1;
         const middleNumber = numbers[middle];

         if (middleNumber === target) {
            upperBound = middle;
            left = middle + 1;
         } else if (middleNumber < target) {
            left = middle + 1;
         } else {
            right = middle - 1;
         }
      }
      return [lowerBound, upperBound]
   };
}
const searchRange = new Solution().searchRange;


console.log(new Solution().searchRange([5, 5, 7], 5), [0, 1])
console.log(new Solution().searchRange([5, 7, 7], 7), [1, 2])
console.log(new Solution().searchRange([5, 7, 7, 8, 8, 10], 8), [3, 4])
console.log(new Solution().searchRange([5, 7, 7, 8, 8, 10], 6), [-1, -1])
console.log(new Solution().searchRange([], 0), [-1, -1])
console.log(new Solution().searchRange([1], 1), [0, 0])