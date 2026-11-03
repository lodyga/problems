class Solution {
   /**
    * Time complexity: O(n3)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: hash map
    *     A: top-down
    * @param {number[]} piles
    * @return {number}
    */
   stoneGameII(piles) {

      const dfs = (start, m, isAlice) => {
         const key = `${start},${m},${isAlice}`;

         if (start === piles.length) {
            return 0;
         }
         else if (memo.has(key)) {
            return memo.get(key);
         }

         let score = isAlice ? 0 : UPPER_BOUND;
         let subpileSum = 0;
         const end = Math.min(start + 2 * m, piles.length);

         for (let idx = start; idx < end; idx++) {
            subpileSum += piles[idx];

            const nextDfs = dfs(idx + 1, Math.max(m, idx - start + 1), !isAlice);

            if (isAlice) {
               score = Math.max(score, subpileSum + nextDfs);
            }
            else {
               score = Math.min(score, nextDfs);
            }
         }

         memo.set(key, score);
         return score;
      };

      const UPPER_BOUND = 1e6;
      const memo = new Map();
      return dfs(0, 1, true);
   }
}


class Solution {
   /**
    * Time complexity: O(n3)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array
    *     A: top-down
    * @param {number[]} piles
    * @return {number}
    */
   stoneGameII(piles) {

      const dfs = (start, m, isAlice) => {
         if (start === N) {
            return 0;
         }
         else if (memo[isAlice ? 1 : 0][start][m] !== -1) {
            return memo[isAlice ? 1 : 0][start][m];
         }

         let score = isAlice ? 0 : UPPER_BOUND;
         let subpileSum = 0;
         const end = Math.min(start + 2 * m, N);

         for (let idx = start; idx < end; idx++) {
            subpileSum += piles[idx];

            const nextDfs = dfs(idx + 1, Math.max(m, idx - start + 1), !isAlice);

            if (isAlice) {
               score = Math.max(score, subpileSum + nextDfs);
            }
            else {
               score = Math.min(score, nextDfs);
            }
         }

         memo[isAlice ? 1 : 0][start][m] = score;
         return score;
      };

      const UPPER_BOUND = 1e6;
      const N = piles.length;

      if (N === 1){
         return piles[0];
      }

      const memo = Array.from({ length: 2 }, () => Array.from({ length: N }, () => Array(N).fill(-1)));
      return dfs(0, 1, true);
   }
}


const stoneGameII = new Solution().stoneGameII;
console.log(new Solution().stoneGameII([2, 7]) === 9)
console.log(new Solution().stoneGameII([2, 7, 9, 4, 4]) === 10)
console.log(new Solution().stoneGameII([1, 2, 3, 4, 5, 100]) === 104)
console.log(new Solution().stoneGameII([2, 100]) === 102)
console.log(new Solution().stoneGameII([1, 2, 100]) === 3)
console.log(new Solution().stoneGameII([77, 12, 64, 35, 28, 4, 87, 21, 20]) === 217)
console.log(new Solution().stoneGameII([8270, 7145, 575, 5156, 5126, 2905, 8793, 7817, 5532, 5726, 7071, 7730, 5200, 5369, 5763, 7148, 8287, 9449, 7567, 4850, 1385, 2135, 1737, 9511, 8065, 7063, 8023, 7729, 7084, 8407]) === 98008)
