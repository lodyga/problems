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
      return -1
   };
}


console.log(new Solution().search([-1, 0, 3, 5, 9, 12], -1) === 0)
console.log(new Solution().search([-1, 0, 3, 5, 9, 12], 0) === 1)
console.log(new Solution().search([-1, 0, 3, 5, 9, 12], 3) === 2)
console.log(new Solution().search([-1, 0, 3, 5, 9, 12], 5) === 3)
console.log(new Solution().search([-1, 0, 3, 5, 9, 12], 9) === 4)
console.log(new Solution().search([-1, 0, 3, 5, 9, 12], 12) === 5)
console.log(new Solution().search([-1, 0, 3, 5, 9, 12], 2) === -1)