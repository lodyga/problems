class Solution {
   /**
    * Time complexity: O(nsqrtn)
    * Auxiliary space complexity: O(n)
    * Tags: dp, bottom-up
    * @param {number} number
    * @return {number}
    */
   numSquares(number) {
      const cache = Array(number + 1).fill(number + 1);
      const primarySquared = Array.from({ length: Number(number ** 0.5) + 1 }, (_, index) => index ** 2);

      for (let index = 1; index <= number; index++) {
         if (primarySquared.includes(index)) {
            cache[index] = 1;
            continue
         }
       
         for (const number of primarySquared) {
            if (index - number > 0) {
               cache[index] = Math.min(
                  cache[index], 
                  cache[index - number] + 1)
            }
         }
      }

      return cache[cache.length - 1]
   };
}


console.log(new Solution().numSquares(1) === 1)  // 1
console.log(new Solution().numSquares(9) === 1)  // 9
console.log(new Solution().numSquares(16) === 1)  // 16
console.log(new Solution().numSquares(2) === 2)  // 2 = 1 + 1
console.log(new Solution().numSquares(5) === 2)  // 5 = 4 + 1
console.log(new Solution().numSquares(13) === 2)  // 13 = 9 + 4
console.log(new Solution().numSquares(12) === 3)  // 12 = 4 + 4 + 4
console.log(new Solution().numSquares(7) === 4)  // 7 = 4 + 1 + 1 + 1
console.log(new Solution().numSquares(28) === 4)  // 28 = 16 + 9 + 1 + 1 + 1 or 28 = 25 + 1 + 1 + 1
console.log(new Solution().numSquares(43) === 3)  // 43 = 25 + 9 + 9