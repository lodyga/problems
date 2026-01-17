class Solution {
   /**
    * Time complexity: O(2^n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: brute-force
    * @param {number[]} piles
    * @return {number}
    */
   stoneGameII(piles) {
      const UPPER_BOUND = 10 ** 6;

      const dfs = (start, m, isAliceTurn) => {
         if (start === piles.length) {
            return 0
         }

         let score = isAliceTurn ? 0 : UPPER_BOUND;
         let subpileSum = 0;

         for (let index = start; index < Math.min(start + 2 * m, piles.length); index++) {
            subpileSum += piles[index];

            const getRestPiles = dfs(
               index + 1,
               Math.max(m, index - start + 1),
               !isAliceTurn
            )

            if (isAliceTurn) {
               score = Math.max(score, subpileSum + getRestPiles);
            } else {
               score = Math.min(score, getRestPiles);
            }
         }
         return score
      }
      return dfs(0, 1, true)
   };

   /**
    * Time complexity: O(n3)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: hash map
    *     A: top-down, prefix sum
    * @param {number[]} piles
    * @return {number}
    */
   stoneGameII(piles) {
      const UPPER_BOUND = 10 ** 6;
      const memo = new Map();
      const prefix = [0];
      piles.forEach((num, index) => prefix.push(prefix[index] + num));

      const dfs = (start, m, isAliceTurn) => {
         const memoInd = (`${start},${m},${isAliceTurn}`);

         if (start === piles.length) {
            return 0
         } else if (memo.has(memoInd)) {
            return memo.get(memoInd)
         }

         let score = isAliceTurn ? 0 : UPPER_BOUND;

         for (let index = start; index < Math.min(start + 2 * m, piles.length); index++) {
            const subpileSum = prefix[index + 1] - prefix[start];

            const getRestPiles = dfs(
               index + 1,
               Math.max(m, index - start + 1),
               !isAliceTurn
            )

            if (isAliceTurn) {
               score = Math.max(score, subpileSum + getRestPiles);
            } else {
               score = Math.min(score, getRestPiles);
            }
         }
         memo.set(memoInd, score);
         return score
      }
      return dfs(0, 1, true)
   };
}


const stoneGameII = new Solution().stoneGameII;
console.log(new Solution().stoneGameII([2, 7]) === 9)
console.log(new Solution().stoneGameII([2, 7, 9, 4, 4]) === 10)
console.log(new Solution().stoneGameII([1, 2, 3, 4, 5, 100]) === 104)
console.log(new Solution().stoneGameII([2, 100]) === 102)
console.log(new Solution().stoneGameII([1, 2, 100]) === 3)
console.log(new Solution().stoneGameII([77, 12, 64, 35, 28, 4, 87, 21, 20]) === 217)
console.log(new Solution().stoneGameII([8270, 7145, 575, 5156, 5126, 2905, 8793, 7817, 5532, 5726, 7071, 7730, 5200, 5369, 5763, 7148, 8287, 9449, 7567, 4850, 1385, 2135, 1737, 9511, 8065, 7063, 8023, 7729, 7084, 8407]) === 98008)
