class Solution {
   /**
    * Time complexity: O(n*m)
    *     n: num count
    *     m: num sum
    * Auxiliary space complexity: O(nm)
    * Tags:
    *     DS: hash map
    *     A: top-down
    * @param {number[]} nums
    * @param {number} target
    * @return {number}
    */
   findTargetSumWays(nums, target) {
      const memo = new Map();

      const dfs = (index, total) => {
         const memoInd = `${index},${total}`;
         if (index === nums.length) {
            return total === target
         } else if (memo.has(memoInd)) {
            return memo.get(memoInd)
         }


         const num = nums[index];
         const addNum = dfs(index + 1, total + num);
         const subtractNum = dfs(index + 1, total - num);
         memo.set(memoInd, addNum + subtractNum);
         return memo.get(memoInd)
      };
      return dfs(0, 0)
   };

   /**
    * Time complexity: O(n*m)
    *     n: num count
    *     m: num sum
    * Auxiliary space complexity: O(n*m)
    * Tags:
    *     DS: hash map
    *     A: bottom-up
    * @param {number[]} nums
    * @param {number} target
    * @return {number}
    */
   findTargetSumWays(nums, target) {
      const N = nums.length;
      const cache = Array.from({ length: N + 1 }, () => ({}));
      cache[0][0] = 1;

      for (let index = 0; index < N; index++) {
         const num = nums[index];
         for (let total in cache[index]) {
            total = Number(total);
            const counter = cache[index][total];
            cache[index + 1][total + num] = (cache[index + 1][total + num] || 0) + counter;
            cache[index + 1][total - num] = (cache[index + 1][total - num] || 0) + counter;
         }
      }
      return cache[N][target] || 0
   };

   /**
    * Time complexity: O(n*m)
    *     n: num count
    *     m: num sum
    * Auxiliary space complexity: O(m)
    * Tags:
    *     DS: hash map
    *     A: bottom-up
    * @param {number[]} nums
    * @param {number} target
    * @return {number}
    */
   findTargetSumWays(nums, target) {
      const N = nums.length;
      let cache = new Map();
      cache.set(0, 1);

      for (const num of nums) {
         const nextCache = new Map();
         for (const [total, counter] of cache) {
            nextCache.set(total + num, (nextCache.get(total + num) || 0) + counter);
            nextCache.set(total - num, (nextCache.get(total - num) || 0) + counter);
         }
         cache = nextCache;
      }
      return cache.get(target) || 0
   };
}


const findTargetSumWays = new Solution().findTargetSumWays;
console.log(new Solution().findTargetSumWays([1], 1) === 1)
console.log(new Solution().findTargetSumWays([2, 2, 2], 2) === 3)
console.log(new Solution().findTargetSumWays([1, 1, 1, 1, 1], 3) === 5)
console.log(new Solution().findTargetSumWays([35, 42, 34, 22, 35, 39, 35, 44, 33, 48, 46, 18, 4, 39, 1, 50, 28, 43, 15, 37], 36) === 5115)
