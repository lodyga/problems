class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags: binary search
    * @param {number[]} numbers
    * @param {number} target
    * @return {number}
    */
   search(numbers, target) {
      let left = 0;
      let right = numbers.length - 1;

      while (left <= right) {
         let middle = (left + right) >> 1;
         const middleNumber = numbers[middle];

         if (target === middleNumber) {
            return middle
         }
         // right side portion is contiguous
         else if (middleNumber < numbers[right]) {
            if (
               middleNumber < target &&
               target <= numbers[right]
            ) {
               left = ++middle;
            } else {
               right = --middle;
            }
         }
         // left side portion is contiguous
         else {
            if (
               numbers[left] <= target &&
               target < middleNumber
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