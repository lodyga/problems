class Solution {
   /**
    * Time complexity: O(n*m)
    *     n: stone count
    *     m: stone sum
    * Auxiliary space complexity: O(n*m)
    * Tags:
    *     DS: hash map
    *     A: top-down
    * @param {number[]} stones
    * @return {number}
    */
   lastStoneWeightII(stones) {
      const dfs = (idx, total) => {
         const key = `${idx},${total}`;
         if (
            total >= half ||
            idx == stones.length
         ) {
            return Math.abs(total - (stoneSum - total));
         } 
         else if (memo.has(key)) {
            return memo.get(key);
         }

         const stone = stones[idx];
         const skip = dfs(idx + 1, total);
         const take = dfs(idx + 1, stone + total);
         const res = Math.min(skip, take);
         memo.set(key, res);
         return res;
      };

      const stoneSum = stones.reduce((sum, value) => sum + value, 0);
      const half = Math.floor(stoneSum / 2);
      const memo = new Map();
      return dfs(0, 0);
   }
}


const lastStoneWeightII = new Solution().lastStoneWeightII;
console.log(new Solution().lastStoneWeightII([3, 3]) === 0)
console.log(new Solution().lastStoneWeightII([2, 7, 4, 1, 8, 1]) === 1)
console.log(new Solution().lastStoneWeightII([31, 26, 33, 21, 40]) === 5)
