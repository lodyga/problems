class Solution {
   /**
    * Time complexity: O(n3)
    * Auxiliary space complexity: O(n2)
    * Tags: dp, top-down with memoization as hash map
    * @param {number[]} piles
    * @return {number}
    */
   stoneGameII(piles) {
      const memo = new Map();

      const dfs = (index, aliceToMove, m) => {
         if (index === piles.length) {
            return 0
         } else if (memo.has(`${index},${aliceToMove},${m}`)) {
            return memo.get(`${index},${aliceToMove},${m}`)
         }
         memo.set(`${index},${aliceToMove},${m}`, aliceToMove ? 0 : Infinity)
         let partSum = 0;

         for (let x = 1; x < 2 * m + 1; x++) {
            if (index + x - 1 === piles.length) {
               break
            }
            partSum += aliceToMove ? piles[index + x - 1] : 0;
            const score = partSum + dfs(index + x, !aliceToMove, Math.max(m, x));
            memo.set(
               `${index},${aliceToMove},${m}`, 
               aliceToMove ? Math.max(memo.get(`${index},${aliceToMove},${m}`), score) : Math.min(memo.get(`${index},${aliceToMove},${m}`), score)
            )
         }
         return memo.get(`${index},${aliceToMove},${m}`)
      }

      return dfs(0, true, 1)
   };
}


console.log(new Solution().stoneGameII([2, 7]), 9)
console.log(new Solution().stoneGameII([2, 7, 9, 4, 4]), 10)
console.log(new Solution().stoneGameII([1, 2, 3, 4, 5, 100]), 104)
console.log(new Solution().stoneGameII([2, 100]), 102)
console.log(new Solution().stoneGameII([1, 2, 100]), 3)
console.log(new Solution().stoneGameII([77, 12, 64, 35, 28, 4, 87, 21, 20]), 217)
console.log(new Solution().stoneGameII([8270, 7145, 575, 5156, 5126, 2905, 8793, 7817, 5532, 5726, 7071, 7730, 5200, 5369, 5763, 7148, 8287, 9449, 7567, 4850, 1385, 2135, 1737, 9511, 8065, 7063, 8023, 7729, 7084, 8407]), 98008)