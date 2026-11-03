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

      const dfs = (idx, total) => {
         const key = `${idx},${total}`;
         
         if (idx === nums.length) {
            return total === target;
         } 
         else if (memo.has(key)) {
            return memo.get(key);
         }

         const val = nums[idx];
         let res = dfs(idx + 1, total + val);
         res += dfs(idx + 1, total - val);
         memo.set(key, res);
         return res;
      };

      const memo = new Map();
      return dfs(0, 0);
   }
}


class Solution {
   /**
    * Time complexity: O(n*m)
    *     n: num count
    *     m: num sum
    * Auxiliary space complexity: O(n*m)
    * Tags:
    *     DS: array, hash map
    *     A: bottom-up
    * @param {number[]} nums
    * @param {number} target
    * @return {number}
    */
   findTargetSumWays(nums, target) {
      const N = nums.length;
      const cache = Array.from({ length: N + 1 }, () => ({}));
      cache[0][0] = 1;

      for (let idx = 0; idx < N; idx++) {
         const val = nums[idx];
         
         for (let total in cache[idx]) {
            total = Number(total);
            const counter = cache[idx][total];
            cache[idx + 1][total + val] = (cache[idx + 1][total + val] || 0) + counter;
            cache[idx + 1][total - val] = (cache[idx + 1][total - val] || 0) + counter;
         }
      }

      return cache[N][target];
   }
}


class Solution {
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

      return cache.get(target);
   }
}


const findTargetSumWays = new Solution().findTargetSumWays;
console.log(new Solution().findTargetSumWays([1], 1) === 1)
console.log(new Solution().findTargetSumWays([2, 2, 2], 2) === 3)
console.log(new Solution().findTargetSumWays([1, 1, 1, 1, 1], 3) === 5)
console.log(new Solution().findTargetSumWays([35, 42, 34, 22, 35, 39, 35, 44, 33, 48, 46, 18, 4, 39, 1, 50, 28, 43, 15, 37], 36) === 5115)
