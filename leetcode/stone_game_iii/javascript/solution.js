class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: top-down
    * @param {number[]} stones
    * @return {string}
    */
   stoneGameIII(stones) {
      const dfs = (start) => {
         if (start == N) {
            return 0;
         }
         else if (memo[start] !== MIN_INT) {
            return memo[start];
         }

         let score = MIN_INT;
         const end = Math.min(start + 3, N)
         let subpileSum = 0;

         for (let idx = start; idx < end; idx++) {
            subpileSum += stones[idx];
            const points = subpileSum - dfs(idx + 1)
            score = Math.max(score, points);
         }

         memo[start] = score;
         return score;
      };

      const MIN_INT = -1e8;
      const N = stones.length;
      const memo = Array(N).fill(MIN_INT);
      const res = dfs(0);

      if (res > 0) {
         return "Alice";
      }
      else if (res === 0) {
         return "Tie";
      }
      return "Bob";
   };
}


class Solution2 {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {number[]} stones
    * @return {string}
    */
   stoneGameIII(stones) {
      const MIN_INT = -1e8;
      const N = stones.length;
      const cache = Array(N + 1).fill(0);

      for (let idx = N - 1; idx >= 0; idx--) {
         cache[idx] = MIN_INT;
         const end = Math.min(idx + 3, N)
         let subpileSum = 0;

         for (let jdx = idx; jdx < end; jdx++) {
            subpileSum += stones[jdx];
            cache[idx] = Math.max(
               cache[idx],
               subpileSum - cache[jdx + 1]
            );
         }
      }

      if (cache[0] > 0) {
         return "Alice";
      }
      else if (cache[0] === 0) {
         return "Tie";
      }
      return "Bob";
   };
}


const stoneGameIII = new Solution().stoneGameIII;
console.log(new Solution().stoneGameIII([1, 2, 3, 7]) === 'Bob')
console.log(new Solution().stoneGameIII([1, 2, 3, -9]) === 'Alice')
console.log(new Solution().stoneGameIII([1, 2, 3, 6]) === 'Tie')
console.log(new Solution().stoneGameIII([-1, -2]) === 'Alice')
console.log(new Solution().stoneGameIII([-1, -2, -3]) === 'Tie')
console.log(new Solution().stoneGameIII([-13, 17, 7, -13, 6, -3, -15, 15, -3, 4, 6, -5, 16, 0, 12, -6, 8, 13, 15, -4, -11, -16, 15]) === 'Alice')
