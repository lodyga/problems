class Solution {
   /**
    * Time complexity: O(n*t)
    *     n: numbers length
    *     t: target
    * Auxiliary space complexity: O(t)
    * Tags: dp, top-down with memoization as list
    * @param {number[]} numbers
    * @param {number} target
    * @return {number}
    */
   combinationSum4(numbers, target) {
      const memo = Array(target + 1);
      memo[memo.length - 1] = 1;
      dfs(0)
      return memo[0]

      function dfs(current) {
         if (current > target) {
            return 0
         } else if (memo[current]) {
            return memo[current]
         }

         //memo[current] = (
         //   numbers
         //      .map(number => dfs(current + number))
         //      .reduce((total, value) => total + value, 0)
         //)
         memo[current] = 0;
         for (const number of numbers) {
            memo[current] += dfs(current + number)
         }
         return memo[current]
      }
   };
}


class Solution {
   /**
    * Time complexity: O(n*t)
    *     n: numbers length
    *     t: target
    * Auxiliary space complexity: O(t)
    * Tags: dp, bottom-up
    * @param {number[]} numbers
    * @param {number} target
    * @return {number}
    */
   combinationSum4(numbers, target) {
      const cache = Array(target + 1).fill(0);
      cache[0] = 1;

      for (let index = 0; index < target + 1; index++) {
         for (const number of numbers) {
            if (index - number >= 0) {
               cache[index] += cache[index - number]
            }
         }
      }
      return cache[target]
   };
}


console.log(new Solution().combinationSum4([5], 5) === 1)
console.log(new Solution().combinationSum4([2, 3], 7) === 3)
console.log(new Solution().combinationSum4([1, 2, 3], 4) === 7)
console.log(new Solution().combinationSum4([9], 3) === 0)
console.log(new Solution().combinationSum4([4, 2, 1], 32) === 39882198)