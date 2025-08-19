class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, top-down with memoization as hash map
    * @param {number[]} stoneValue
    * @return {string}
    */
   stoneGameIII(stoneValue) {
      const memo = new Map();

      const dfs = (index, aliceToMove) => {
         if (index == stoneValue.length) {
            return 0
         } else if (memo.has(index)) {
            return memo.get(index)
         }
         let partSum = 0;
         memo.set(index, -Infinity);
         
         for (let x = index; x < Math.min(index + 3, stoneValue.length); x++) {
            partSum += stoneValue[x];
            const score = partSum - dfs(x + 1, !aliceToMove)
            memo.set(index, Math.max(memo.get(index), score));
         }
         return memo.get(index)
      }
      const result = dfs(0, true);
      return result === 0 ? 'Tie' : result > 0 ? 'Alice' : 'Bob'
   };
}
const stoneGameIII = new Solution().stoneGameIII;


console.log(new Solution().stoneGameIII([1, 2, 3, 7]), 'Bob')
console.log(new Solution().stoneGameIII([1, 2, 3, -9]), 'Alice')
console.log(new Solution().stoneGameIII([1, 2, 3, 6]), 'Tie')
console.log(new Solution().stoneGameIII([-1, -2]), 'Alice')
console.log(new Solution().stoneGameIII([-1, -2, -3]), 'Tie')