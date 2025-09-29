class Solution {
   /**
    * Time complexity: O(nm)
    *     m: sum(numbers)
    * Auxiliary space complexity: O(nm)
    * Tags: dp, top-down with memoization as hash map
    * @param {number[]} numbers
    * @param {number} target
    * @return {number}
    */
   findTargetSumWays(numbers, target) {
      const memo = new Map();

      const dfs = (index, total) => {
         if (index === numbers.length)
            return total === target
         else if (memo.has(`${index},${total}`))
            return memo.get(`${index},${total}`)

         const number = numbers[index];

         const positive = dfs(index + 1, total + number)
         const negative = dfs(index + 1, total - number)
         memo.set(`${index},${total}`, positive + negative)
         return memo.get(`${index},${total}`)
      };
      return dfs(0, 0)
   };
}
const findTargetSumWays = new Solution(). findTargetSumWays;


console.log(new Solution().findTargetSumWays([1, 1, 1, 1, 1], 3) === 5)
console.log(new Solution().findTargetSumWays([2, 2, 2], 2) === 3)
console.log(new Solution().findTargetSumWays([1], 1) === 1)
console.log(new Solution().findTargetSumWays([35, 42, 34, 22, 35, 39, 35, 44, 33, 48, 46, 18, 4, 39, 1, 50, 28, 43, 15, 37], 36) === 5115)