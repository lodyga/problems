class Solution {
   /**
    * Time complexity: O(n*m)
    *     n: stone count
    *     m: stone sum
    * Auxiliary space complexity: O(n*m)
    * Tags: dp, top-down with memoization as hash map
    * @param {number[]} stones
    * @return {number}
    */
   lastStoneWeightII(stones) {
      const total = stones.reduce((total, value) => total + value, 0);
      const target = (total + 1) >> 1;
      const memo = new Map();

      const dfs = (index, currentSum) => {
         if (
            currentSum >= target ||
            index == stones.length
         ) {
            return Math.abs(currentSum - (total - currentSum))
         } else if (memo.has(`${index},${currentSum}`)) {
            return memo.get(`${index},${currentSum}`)
         }
         memo.set(
            `${index},${currentSum}`,
            Math.min(
               dfs(index + 1, currentSum + stones[index]),
               dfs(index + 1, currentSum)
            )
         )
         return memo.get(`${index},${currentSum}`)
      }
      return dfs(0, 0)
   };
}
const lastStoneWeightII = new Solution().lastStoneWeightII;


console.log(new Solution().lastStoneWeightII([3, 3]) === 0)
console.log(new Solution().lastStoneWeightII([2, 7, 4, 1, 8, 1]) === 1)
console.log(new Solution().lastStoneWeightII([31, 26, 33, 21, 40]) === 5)