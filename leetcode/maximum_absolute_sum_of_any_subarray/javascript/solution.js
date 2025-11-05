class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: greedy
    * Kadane's Algorithm
    * @param {number[]} numbers
    * @return {number}
    */
   maxAbsoluteSum(numbers) {
      // search for positive sums
      let element = 0;
      let maxElement = numbers[0];
      for (const number of numbers) {
         element > 0 ? element += number : element = number;
         maxElement = Math.max(maxElement, element);
      }
      // search for negative sums
      element = 0;
      let minElement = numbers[0];
      for (const number of numbers) {
         element < 0 ? element += number : element = number;
         minElement = Math.min(minElement, element);

      }
      return Math.max(maxElement, Math.abs(minElement))
   };
}


const maxAbsoluteSum = new Solution().maxAbsoluteSum;
console.log(new Solution().maxAbsoluteSum([1, -3, 2, 3, -4]) === 5)
console.log(new Solution().maxAbsoluteSum([2, -5, 1, -4, 3, -2]) === 8)
console.log(new Solution().maxAbsoluteSum([-1, 5]) === 5)
