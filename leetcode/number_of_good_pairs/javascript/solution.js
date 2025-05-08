class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: math
    * @param {number[]} numbers
    * @return {number}
    */
   numIdenticalPairs(numbers) {
      const numberFrequency = new Map();
      let pairCounter = 0;

      for (const number of numbers) {
         numberFrequency.set(number, (numberFrequency.get(number) || 0) + 1);
      }

      // n! / ((n-2)! 2!) => n(n-1)/2
      for (const val of numberFrequency.values()) {
         if (val > 1) {
            pairCounter += val * (val - 1) / 2
         }
      }
      return pairCounter
   };
}


console.log(new Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]), 4)
console.log(new Solution().numIdenticalPairs([1, 1, 1, 1]), 6)
console.log(new Solution().numIdenticalPairs([1, 2, 3]), 0)