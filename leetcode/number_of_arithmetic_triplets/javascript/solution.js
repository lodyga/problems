class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * @param {number[]} numbers
    * @param {number} delta
    * @return {number}
    */
   arithmeticTriplets(numbers, delta) {
      const uniqueNumbers = new Set(numbers);
      let counter = 0;

      for (const number of numbers) {
         if (
            uniqueNumbers.has(number + delta) &&
            uniqueNumbers.has(number + 2 * delta)
         ) {
            counter++;
         }
      }
      return counter
   };
}


console.log(new Solution().arithmeticTriplets([0, 1, 4, 6, 7, 10], 3), 2)
console.log(new Solution().arithmeticTriplets([4, 5, 6, 7, 8, 9], 2), 2)