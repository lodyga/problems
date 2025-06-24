class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags: dp, top-down with memoization as hash map
    * @param {number} number
    * @return {number}
    */
   integerBreak(number) {
      // {number: product}  maximum product for current number
      const memo = new Map([[0, 1]]);
      return dfs(number, false)

      function dfs(index, isTwoPart)  {
         if (memo.has(index)) {
            return memo.get(index)
         }

         let maxNumber = 0;

         for (let number = 1; number < index + Boolean(isTwoPart); number++) {
            maxNumber = Math.max(
               maxNumber, 
               (number * dfs(index - number, true)))
         }

         memo.set(index, maxNumber);
         return maxNumber
      }
   };
}


console.log(new Solution().integerBreak(2) === 1)  // Explanation: 2 = 1 + 1, 1 × 1 = 1.
console.log(new Solution().integerBreak(3) === 2)  // Explanation: 3 = 1 + 2, 1 × 2 = 2.
console.log(new Solution().integerBreak(4) === 4)  // Explanation: 4 = 2 + 2, 2 × 2 = 4.
console.log(new Solution().integerBreak(5) === 6)  // Explanation: 5 = 2 + 3, 2 × 3 = 6.
console.log(new Solution().integerBreak(6) === 9)  // Explanation: 6 = 3 + 3, 3 × 3 = 9.
console.log(new Solution().integerBreak(7) === 12)  // Explanation: 7 = 3 + 4, 3 × 4 = 12; 2 = 2 + 2 + 3, 2 x 2 x 3 = 12.
console.log(new Solution().integerBreak(10) === 36)  // Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
console.log(new Solution().integerBreak(24) === 6561)  // tle testcase