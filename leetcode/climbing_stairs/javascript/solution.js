class Solution {
   /**
    * Time complexity: O(2^n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *    A: brute-force, pure recursion
    * 'counter' as a return statement from dfs
    * converts to top-down
    * @param {number} steps
    * @return {number}
    */
   climbStairs(steps) {
      const dfs = (index) => {
         if (index === 0 || index === 1)
            return 1
         return dfs(index - 1) + dfs(index - 2);
      }
      return dfs(steps)
   };

   /**
    * Time complexity: O(2^n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *    A: brute-force, shared state
    * `counter` as shared variable
    * @param {number} steps
    * @return {number}
    */
   climbStairs(steps) {
      let counter = 0;
      const dfs = (index) => {
         if (index === 0 || index === 1) {
            counter++;
            return
         }
         dfs(index - 1);
         dfs(index - 2);
      }
      dfs(steps)
      return counter
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:    
    *    DS: hash map
    *    A: top-down
    * @param {number} steps
    * @return {number}
    */
   climbStairs(steps) {
      const memo = new Map([[0, 1], [1, 1]]);

      const dfs = (index) => {
         if (memo.has(index))
            return memo.get(index)
      
         memo.set(index, (dfs(index - 1) + dfs(index - 2)));
         return memo.get(index);
      }
      return dfs(steps)
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: array
    *     A: top-down
    * @param {number} steps
    * @return {number}
    */
   climbStairs(steps) {
      const memo = Array(steps + 1).fill(-1);
      memo[0] = 1;
      memo[1] = 1;

      const dfs = (index) => {
         if (memo[index] !== -1)
            return memo[index]

         memo[index] = dfs(index - 1) + dfs(index - 2);
         return memo[index];
      }
      return dfs(steps)
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: array
    *     A: bottom-up
    * @param {number} steps
    * @return {number}
    */
   climbStairs(steps) {
      const cache = Array(steps + 1).fill(1);

      for (let index = 2; index < steps + 1; index++) {
         cache[index] = cache[index - 1] + cache[index - 2];
      }
      return cache[steps]
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     A: greedy
    * @param {number} steps
    * @return {number}
    */
   climbStairs(steps) {
      const cache = [1, 1];

      for (let index = 2; index < steps + 1; index++) {
         cache[index % 2] = cache[0] + cache[1];
      }
      return cache[steps % 2]
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: greedy
    * @param {number} number
    * @return {number}
    */
   climbStairs1(number) {
      let a = 0;
      let b = 1;
      
      for (let index = 0; index < number; index++) {
         [a, b] = [b, a + b]
         // b = a + b;
         // a = b - a;
      }
      return b
   };
}


const climbStairs = new Solution().climbStairs;
console.log(new Solution().climbStairs1(1) === 1)
console.log(new Solution().climbStairs1(2) === 2)
console.log(new Solution().climbStairs1(3) === 3)
console.log(new Solution().climbStairs1(4) === 5)
console.log(new Solution().climbStairs1(5) === 8)
console.log(new Solution().climbStairs1(6) === 13)
console.log(new Solution().climbStairs1(44) === 1134903170)
