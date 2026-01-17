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
      const stoneSum = stones.reduce((sum, value) => sum + value, 0);
      const half = stoneSum >> 1;
      const memo = new Map();

      const dfs = (index, total) => {
         const memoInd = `${index},${total}`;
         if (
            total >= half ||
            index == stones.length
         ) {
            return Math.abs(total - (stoneSum - total))
         } else if (memo.has(memoInd)) {
            return memo.get(memoInd)
         }

         const stone = stones[index];
         const skip = dfs(index + 1, total);
         const take = dfs(index + 1, stone + total);
         const res = Math.min(skip, take);
         memo.set(memoInd, res);
         return res
      }
      return dfs(0, 0)
   };
}


const lastStoneWeightII = new Solution().lastStoneWeightII;
console.log(new Solution().lastStoneWeightII([3, 3]) === 0)
console.log(new Solution().lastStoneWeightII([2, 7, 4, 1, 8, 1]) === 1)
console.log(new Solution().lastStoneWeightII([31, 26, 33, 21, 40]) === 5)
