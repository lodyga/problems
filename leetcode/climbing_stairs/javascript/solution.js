class Solution {
   /**
    * Time complexity: O(2^n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: brute-force, pure recursion
    * @param {number} n
    * @return {number}
    */
   climbStairs(n) {
      const dfs = (idx) => {
         if (idx >= n) {
            return idx === n
         }

         return dfs(idx + 1) + dfs(idx + 2);
      }
      return dfs(0)
   };

   /**
    * Time complexity: O(2^n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: brute-force, shared state
    * @param {number} n
    * @return {number}
    */
   climbStairs(n) {
      let res = 0;

      const dfs = (idx) => {
         if (idx >= n) {
            res += idx === n;
            return
         }

         dfs(idx + 1);
         dfs(idx + 2);
      }

      dfs(0)
      return res
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:    
    *    DS: hash map
    *    A: top-down
    * @param {number} n
    * @return {number}
    */
   climbStairs(n) {
      const memo = Array(n).fill(-1);
      memo.push(1);
      memo.push(0);

      const dfs = (idx) => {
         if (memo[idx] !== -1) {
            return memo[idx]
         }

         memo[idx] = dfs(idx + 1) + dfs(idx + 2);
         return memo[idx]
      }
      return dfs(0)
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {number} n
    * @return {number}
    */
   climbStairs(n) {
      const cache = Array(n).fill(0);
      cache.push(1);
      cache.push(0);

      for (let idx = n - 1; idx > - 1; idx--) {
         cache[idx] = cache[idx + 1] + cache[idx + 2];
      }
      return cache[0]
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {number} n
    * @return {number}
    */
   climbStairs(n) {
      const cache = [1, 0];

      for (let idx = n - 1; idx > - 1; idx--) {
         [cache[0], cache[1]] = [cache[0] + cache[1], cache[0]];
      }

      return cache[0]
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: bottom-up
    * @param {number} num
    * @return {number}
    */
   climbStairs1(num) {
      let a = 0;
      let b = 1;

      for (let idx = 0; idx < num; idx++) {
         [a, b] = [b, a + b]
         // b = a + b;
         // a = b - a;
      }
   
      return b
   };
}


const climbStairs = new Solution().climbStairs;
console.log(new Solution().climbStairs(1) === 1)
console.log(new Solution().climbStairs(2) === 2)
console.log(new Solution().climbStairs(3) === 3)
console.log(new Solution().climbStairs(4) === 5)
console.log(new Solution().climbStairs(5) === 8)
console.log(new Solution().climbStairs(6) === 13)
console.log(new Solution().climbStairs1(44) === 1134903170)
