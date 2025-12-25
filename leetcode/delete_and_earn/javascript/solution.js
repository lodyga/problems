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
         numFreq.set(num, (numFreq.get(num) || 0) + num);
      }
      const sortedNums = [...numFreq.keys()].sort((a, b) => a - b);
      const memo = Array(sortedNums.length + 2).fill(-1);
      memo[memo.length - 1] = 0;
      memo[memo.length - 2] = 0;

      const dfs = (index) => {
         if (memo[index] !== -1)
            return memo[index]

         const val = numFreq.get(sortedNums[index]);
         const skip = dfs(index + 1);
         let take = val + dfs(index + 2);
         if (
            index + 1 < sortedNums.length &&
            sortedNums[index] + 1 !== sortedNums[index + 1]
         )
            take = Math.max(take, val + dfs(index + 1));

         memo[index] = Math.max(skip, take);
         return memo[index]
      }
      return dfs(0)
   };

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
      const sortedNums = [...numFreq.keys()].sort((a, b) => a - b);
      const cache = Array(sortedNums.length + 2).fill(0);

      for (let index = sortedNums.length - 1; index > -1; index--) {
         const val = numFreq.get(sortedNums[index]);
         cache[index] = Math.max(cache[index + 1], val + cache[index + 2]);
         if (
            index + 1 < sortedNums.length &&
            sortedNums[index] + 1 !== sortedNums[index + 1]
         )
            cache[index] = Math.max(cache[index], val + cache[index + 1]);
      }
      return cache[0]
   };

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
         numFreq.set(num, (numFreq.get(num) || 0) + num);
      }
      const sortedNums = [...numFreq.keys()].sort((a, b) => a - b);
      const cache = Array(sortedNums.length + 2).fill(0);

      for (let index = sortedNums.length - 1; index > -1; index--) {
         const val = numFreq.get(sortedNums[index]);
         let cache0 = Math.max(cache[0], val + cache[1]);
         if (
            index + 1 < sortedNums.length &&
            sortedNums[index] + 1 !== sortedNums[index + 1]
         )
            cache0 = Math.max(cache[index], val + cache[0]);
         cache[1] = cache[0];
         cache[0] = cache0;
      }
      return cache[0]
   };
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
