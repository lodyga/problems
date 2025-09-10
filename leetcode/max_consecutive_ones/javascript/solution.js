class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: iteration
    * @param {number[]} numbers
    * @return {number}
    */
   findMaxConsecutiveOnes(numbers) {
      let counter = 0;
      let maxCounter = 0;

      for (const number of numbers) {
         if (number) {
            counter++;
         } else {
            maxCounter = Math.max(maxCounter, counter);
            counter = 0;
         }
      }
      return Math.max(maxCounter, counter)
   };
}
const findMaxConsecutiveOnes = new Solution().findMaxConsecutiveOnes;


console.log(new Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) === 3)
console.log(new Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) === 2)
console.log(new Solution().findMaxConsecutiveOnes([1]) === 1)
console.log(new Solution().findMaxConsecutiveOnes([0]) === 0)