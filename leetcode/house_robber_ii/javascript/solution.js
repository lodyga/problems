class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: dp, bottom-up
    * @param {number[]} numbers
    * @return {number}
    */
   rob(numbers) {
      if (numbers.length <= 3) {
         return Math.max(...numbers)
      }

      return Math.max(
         robInner(numbers.slice(0, -1)),
         robInner(numbers.slice(1,))
      )

      function robInner(numbers) {
         if (numbers.length <= 2) {
            return Math.max(...numbers)
         }
         let cache = Array(
            numbers[0],
            Math.max(numbers[0], numbers[1])
         );

         for (const number of numbers.slice(2,)) {
            cache = [cache[1], Math.max(cache[0] + number, cache[1])];
         }
         return cache[cache.length - 1]
      };
   };
}


console.log(new Solution().rob([2, 3, 2]) === 3)
console.log(new Solution().rob([1, 2, 3, 1]) === 4)
console.log(new Solution().rob([1, 2, 3]) === 3)
console.log(new Solution().rob([1]) === 1)
console.log(new Solution().rob([0, 0]) === 0)
console.log(new Solution().rob([1, 3, 1, 3, 100]) === 103)