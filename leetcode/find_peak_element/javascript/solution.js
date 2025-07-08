class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags: binary search
    * @param {number[]} numbers
    * @return {number}
    */
   findPeakElement(numbers) {
      let left = 0;
      let right = numbers.length - 1;

      while (left <= right) {
         const middle = (left + right) >> 1;
         const middleNumber = numbers[middle];
         const prevNumebr = middle === 0 ? middleNumber - 1 : numbers[middle - 1];
         const nextNumber = middle === numbers.length - 1 ? middleNumber - 1 : numbers[middle + 1];

         if (
            prevNumebr < middleNumber &&
            middleNumber > nextNumber
         ) {
            return middle
         } else if (
            middle !== numbers.length - 1 &&
            middleNumber < numbers[middle + 1]
         ) {
            left = middle + 1;
         } else {
            right = middle - 1
         }
      }
   };
}


console.log(new Solution().findPeakElement([1, 2, 3, 1]) == 2)
console.log(new Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]) == 5)
console.log(new Solution().findPeakElement([1]) == 0)
console.log(new Solution().findPeakElement([1, 2]) == 1)