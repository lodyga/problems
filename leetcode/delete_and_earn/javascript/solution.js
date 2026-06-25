class Solution {
   /**
    * Time complexity: O(n + mlogm)
    *     n: num count
    *     m: unique num count
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array, hash map
    *     A: top-down
    * @param {number[]} nums
    * @return {number}
    */
   deleteAndEarn(nums) {
      const numFreq = new Map();

      for (const num of nums) {
         numFreq.set(num, (numFreq.get(num) || 0) + 1);
      }

      const sortedUniqueNums = [...numFreq.keys()].sort((a, b) => a - b);
      const memo = Array(sortedUniqueNums.length + 2).fill(-1);
      memo[memo.length - 1] = 0;
      memo[memo.length - 2] = 0;

      const dfs = (idx) => {
         if (memo[idx] !== -1) {
            return memo[idx]
         }

         const num = sortedUniqueNums[idx]
         const val = num * numFreq.get(num);

         if (
            idx + 1 < sortedUniqueNums.length &&
            sortedUniqueNums[idx] + 1 < sortedUniqueNums[idx + 1]
         ) {
            memo[idx] = val + dfs(idx + 1);
            return memo[idx];
         }

         const skip = dfs(idx + 1);
         const take = val + dfs(idx + 2);

         memo[idx] = Math.max(skip, take);
         return memo[idx];
      }

      return dfs(0);
   }
}


class Solution {
   /**
    * Time complexity: O(n + mlogm)
    *     n: num count
    *     m: unique num count
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array, hash map
    *     A: bottom-up
    * @param {number[]} nums
    * @return {number}
    */
   deleteAndEarn(nums) {
      const numFreq = new Map();
      for (const num of nums) {
         numFreq.set(num, (numFreq.get(num) || 0) + num);
      }
      const sortedUniqueNums = [...numFreq.keys()].sort((a, b) => a - b);
      const cache = Array(sortedUniqueNums.length + 2).fill(0);

      for (let idx = sortedUniqueNums.length - 1; idx > -1; idx--) {
         const num = sortedUniqueNums[idx]
         const val = numFreq.get(num);

         if (
            idx + 1 < sortedUniqueNums.length &&
            sortedUniqueNums[idx] + 1 < sortedUniqueNums[idx + 1]
         ) {
            cache[idx] = Math.max(cache[idx], val + cache[idx + 1]);
         } else {
            cache[idx] = Math.max(
               cache[idx + 1],
               val + cache[idx + 2]
            );
         }
      }

      return cache[0];
   }
}


class Solution {
   /**
    * Time complexity: O(n + mlogm)
    *     n: num count
    *     m: unique num count
    * Auxiliary space complexity: O(m)
    * Tags:
    *     DS: array, hash map
    *     A: bottom-up
    * @param {number[]} nums
    * @return {number}
    */
   deleteAndEarn(nums) {
      const numFreq = new Map();

      for (const num of nums) {
         numFreq.set(num, (numFreq.get(num) || 0) + 1);
      }

      const sortedUniqueNums = [...numFreq.keys()].sort((a, b) => a - b);
      const cache = [0, 0];

      for (let idx = sortedUniqueNums.length - 1; idx > -1; idx--) {
         const num = sortedUniqueNums[idx];
         const val = num * numFreq.get(num);
         let cache0;
         
         if (
            idx + 1 < sortedUniqueNums.length &&
            sortedUniqueNums[idx] + 1 < sortedUniqueNums[idx + 1]
         ) {
            cache0 = Math.max(val + cache[0]);
         } else {
            cache0 = Math.max(cache[0], val + cache[1]);
         }

         cache[1] = cache[0];
         cache[0] = cache0;
      }

      return cache[0]
   }
}


const deleteAndEarn = new Solution().deleteAndEarn;
console.log(new Solution().deleteAndEarn([1]) === 1)
console.log(new Solution().deleteAndEarn([2, 3]) === 3)
console.log(new Solution().deleteAndEarn([2, 4]) === 6)
console.log(new Solution().deleteAndEarn([3, 4, 2]) === 6)
console.log(new Solution().deleteAndEarn([2, 2, 3, 3, 3, 4]) === 9)
console.log(new Solution().deleteAndEarn([8, 10, 4, 9, 1, 3, 5, 9, 4, 10]) === 37)
console.log(new Solution().deleteAndEarn([1, 1, 1, 2, 4, 5, 5, 5, 6]) === 18)
console.log(new Solution().deleteAndEarn([1, 6, 3, 3, 8, 4, 8, 10, 1, 3]) === 43)
console.log(new Solution().deleteAndEarn([1, 1, 1]) === 3)
console.log(new Solution().deleteAndEarn([12, 32, 93, 17, 100, 72, 40, 71, 37, 92, 58, 34, 29, 78, 11, 84, 77, 90, 92, 35, 12, 5, 27, 92, 91, 23, 65, 91, 85, 14, 42, 28, 80, 85, 38, 71, 62, 82, 66, 3, 33, 33, 55, 60, 48, 78, 63, 11, 20, 51, 78, 42, 37, 21, 100, 13, 60, 57, 91, 53, 49, 15, 45, 19, 51, 2, 96, 22, 32, 2, 46, 62, 58, 11, 29, 6, 74, 38, 70, 97, 4, 22, 76, 19, 1, 90, 63, 55, 64, 44, 90, 51, 36, 16, 65, 95, 64, 59, 53, 93]) === 3451)
