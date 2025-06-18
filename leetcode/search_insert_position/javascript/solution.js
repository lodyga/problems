class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags: binary search
    * @param {number[]} numbers
    * @param {number} target
    * @return {number}
    */
   searchInsert(numbers, target) {
      let left = 0;
      let right = numbers.length - 1;

      while (left <= right) {
         const middle = (left + right) >> 1;
         const middleNumber = numbers[middle];

         if (target === middleNumber) {
            return middle
         } else if (target < middleNumber) {
            right = middle - 1;
         } else {
            left = middle + 1;
         }
      }
      return left
   };
}


console.log(new Solution().searchInsert([1, 3, 5, 6], 1) === 0)
console.log(new Solution().searchInsert([1, 3, 5, 6], 3) === 1)
console.log(new Solution().searchInsert([1, 3, 5, 6], 5) === 2)
console.log(new Solution().searchInsert([1, 3, 5, 6], 6) === 3)
console.log(new Solution().searchInsert([1, 3, 5, 6], 0) === 0)
console.log(new Solution().searchInsert([1, 3, 5, 6], 2) === 1)
console.log(new Solution().searchInsert([1, 3, 5, 6], 4) === 2)
console.log(new Solution().searchInsert([1, 3, 5, 6], 7) === 4)