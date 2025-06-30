class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: sliding window
    * @param {number[]} numbers
    * @return {number}
    */
   minOperations(numbers) {
      const uniqueNumbers = [...new Set(numbers)].sort((a, b) => a - b);
      let minOperations = numbers.length - 1;
      let right = 0;

      for (let left = 0; left < numbers.length; left++) {
         while (
            right < uniqueNumbers.length &&
            uniqueNumbers[right] < uniqueNumbers[left] + numbers.length
         ) {
            right++;
         }
         const window = right - left;
         const operations = numbers.length - window;
         minOperations = Math.min(minOperations, operations);
      }
      return minOperations
   };
}
const minOperations = new Solution().minOperations;


console.log(new Solution().minOperations([2, 3, 5, 9]) === 1)
console.log(new Solution().minOperations([4, 2, 5, 3]) === 0)
console.log(new Solution().minOperations([1, 2, 3, 5, 6]) === 1)
console.log(new Solution().minOperations([1, 10, 100, 1000]) === 3)
console.log(new Solution().minOperations([8, 5, 9, 9, 8, 4]) === 2)
console.log(new Solution().minOperations([8, 10, 16, 18, 10, 10, 16, 13, 13, 16]) === 6)