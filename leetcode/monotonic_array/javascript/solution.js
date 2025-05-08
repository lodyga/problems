class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * @param {number[]} numbers
    * @return {boolean}
    */
   isMonotonic(numbers) {
      return isIncreasing() || isDecreasing()
      
      function isIncreasing() {
         for (let index = 0; index < numbers.length - 1; index++) {
            if (numbers[index + 1] < numbers[index])
               return false
         }
         return true
      }
      function isDecreasing() {
         for (let index = 0; index < numbers.length - 1; index++) {
            if (numbers[index + 1] > numbers[index])
               return false
         }
         return true
      }
   };
}
const isMonotonic = new Solution().isMonotonic;


console.log(new Solution().isMonotonic([1, 2, 2, 3]), true)
console.log(new Solution().isMonotonic([6, 5, 4, 4]), true)
console.log(new Solution().isMonotonic([1, 3, 2]), false)