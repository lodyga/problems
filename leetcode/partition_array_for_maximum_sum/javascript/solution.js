class Solution {
   /**
    * Time complexity: O(k*n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: top-down
    * @param {number[]} nums
    * @param {number} k
    * @return {number}
    */
   maxSumAfterPartitioning(nums, k) {
      const memo = Array(nums.length).fill(-1);
      memo.push(0);

      const dfs = (left) => {
         if (memo[left] !== -1) {
            return memo[left]
         }

         let maxVal = 0;
         let res = 0;

         for (let right = left; right < Math.min(left + k, nums.length); right++) {
            maxVal = Math.max(maxVal, nums[right]);
            const subSum = maxVal * (right - left + 1);
            res = Math.max(res, subSum + dfs(right + 1));
         }

         memo[left] = res;
         return res
      }

      return dfs(0)
   };

   /**
    * Time complexity: O(k*n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {number[]} nums
    * @param {number} k
    * @return {number}
    */
   maxSumAfterPartitioning(nums, k) {
      const cache = Array(nums.length + 1).fill(0);

      for (let left = nums.length - 1; left > -1; left--) {
         let maxVal = 0;

         for (let right = left; right < Math.min(left + k, nums.length); right++) {
            maxVal = Math.max(maxVal, nums[right]);
            const subSum = maxVal * (right - left + 1);
            cache[left] = Math.max(cache[left], subSum + cache[right + 1]);
         }
      }

      return cache[0]
   };

   /**
    * Time complexity: O(k*n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: bottom-up
    *     Circular array.
    * @param {number[]} nums
    * @param {number} k
    * @return {number}
    */
   maxSumAfterPartitioning(nums, k) {
      const cache = Array(k).fill(0);

      for (let left = nums.length - 1; left > -1; left--) {
         let maxVal = 0;
         let nextCache = 0;

         for (let right = left; right < Math.min(left + k, nums.length); right++) {
            maxVal = Math.max(maxVal, nums[right]);
            const subSum = maxVal * (right - left + 1);
            nextCache = Math.max(nextCache, subSum + cache[(right + 1) % k]);
         }

         cache[left % k] = nextCache;
      }

      return cache[0]
   };
}


const maxSumAfterPartitioning = new Solution().maxSumAfterPartitioning;
console.log(new Solution().maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3) === 84)
console.log(new Solution().maxSumAfterPartitioning([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4) === 83)
console.log(new Solution().maxSumAfterPartitioning([1], 1) === 1)
console.log(new Solution().maxSumAfterPartitioning([20779, 436849, 274670, 543359, 569973, 280711, 252931, 424084, 361618, 430777, 136519, 749292, 933277, 477067, 502755, 695743, 413274, 168693, 368216, 677201, 198089, 927218, 633399, 427645, 317246, 403380, 908594, 854847, 157024, 719715, 336407, 933488, 599856, 948361, 765131, 335089, 522119, 403981, 866323, 519161, 109154, 349141, 764950, 558613, 692211], 26) === 42389649)
