class Solution {
   /**
    * Time complexity: O(2^n)
    * Auxiliary space complexity: O(n)
    * Tags: brute force, pure recursion, tle
    * 'counter' as a return statement from dfs
    * converts to top-down
    * @param {number} number
    * @return {number}
    */
   climbStairs(number) {
      function dfs(index) {
         if (index < 0)
            return 0
         else if (index === 0)
            return 1

         return dfs(index - 1) + dfs(index - 2);
      }
      return dfs(number)
   };

   /**
    * Time complexity: O(2^n)
    * Auxiliary space complexity: O(n)
    * Tags: brute force, shared state, tle
    * `counter` as shared variable (list)
    * @param {number} number
    * @return {number}
    */
   climbStairs(number) {
      let counter = 0;

      function dfs(index) {
         if (index < 0)
            return
         else if (index === 0) {
            counter++;
            return
         }
         dfs(index - 1);
         dfs(index - 2);
      }

      dfs(number)
      return counter
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, top-down with memoization as hash map
    * @param {number} number
    * @return {number}
    */
   climbStairs(number) {
      const memo = new Map([[0, 1]]);

      function dfs(index) {
         if (index < 0)
            return 0
         else if (memo.has(index))
            return memo.get(index)

         memo.set(index, (dfs(index - 1) + dfs(index - 2)));
         return memo.get(index);
      }

      return dfs(number)
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, top-down with memoization as array
    * @param {number} number
    * @return {number}
    */
   climbStairs(number) {
      const memo = Array(number + 1).fill(null);
      memo[0] = 1;

      function dfs(index) {
         if (index < 0)
            return 0
         else if (memo[index] !== null)
            return memo[index]

         memo[index] = dfs(index - 1) + dfs(index - 2);
         return memo[index];
      }

      return dfs(number)
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, bottom-up
    * @param {number} number
    * @return {number}
    */
   climbStairs(number) {
      if (number < 4)
         return number

      const cache = Array(number + 1).fill(1);

      for (let index = 2; index < number + 1; index++) {
         cache[index] = cache[index - 1] + cache[index - 2];
      }

      return cache[cache.length - 1]
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: dp, bottom-up
    * @param {number} number
    * @return {number}
    */
   climbStairs(number) {
      if (number < 4)
         return number

      const cache = [1, 1];

      for (let index = 2; index < number + 1; index++) {
         [cache[0], cache[1]] = [cache[1], cache[0] + cache[1]];
      }

      return cache[1]
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: slick
    * @param {number} number
    * @return {number}
    */
   climbStairs(number) {
      if (number < 4)
         return number

      let a = 0;
      let b = 1;

      for (let index = 0; index < number; index++) {
         b = a + b;
         a = b - a;
         // [a, b] = [b, a + b]
      }
      return b
   };
}


console.log(new Solution().climbStairs(1) === 1)
console.log(new Solution().climbStairs(2) === 2)
console.log(new Solution().climbStairs(3) === 3)
console.log(new Solution().climbStairs(4) === 5)
console.log(new Solution().climbStairs(5) === 8)
console.log(new Solution().climbStairs(6) === 13)