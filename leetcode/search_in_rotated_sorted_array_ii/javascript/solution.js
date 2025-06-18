class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: binary search
    * @param {number[]} numbers
    * @param {number} target
    * @return {boolean}
    */
   search(numbers, target) {
      let left = 0;
      let right = numbers.length - 1;

      while (left <= right) {
         const middle = (left + right) >> 1;
         const middleNumber = numbers[middle];

         if (
            target === middleNumber ||
            target === numbers[left] ||
            target === numbers[right]
         )
            return true
         else if (middleNumber < numbers[right]) {
            if (
               middleNumber < target &&
               target < numbers[right]
            ) left = middle + 1;
            else
               right = middle - 1;
         }
         else if (numbers[left] < middleNumber) {
            if (
               numbers[left] < target &&
               target < middleNumber
            ) right = middle - 1;
            else
               left = middle + 1;
         }
         else {
            left++;
            right--;
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
console.log(new Solution().search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], 2) === true)
console.log(new Solution().search([1, 0, 1, 1, 1], 0) === true)
console.log(new Solution().search([1, 0, 0], 1) === true)