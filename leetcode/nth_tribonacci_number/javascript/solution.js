class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map
    *     A: top-down
    * @param {number} num
    * @return {number}
    */
   tribonacci(ind) {
      const memo = new Map([[0, 0], [1, 1], [2, 1]]);

      const dfs = (ind) => {
         if (memo.has(ind)) {
            return memo.get(ind);
         }

         const triplet = dfs(ind - 1) + dfs(ind - 2) + dfs(ind - 3);
         memo.set(ind, triplet);
         return triplet
      }

      return dfs(ind)
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: bottom-up
    * @param {number} num
    * @return {number}
    */
   tribonacci(num) {
      const cache = [0, 1, 1];

      for (let idx = 3; idx < num + 1; idx++) {
         cache.push(
            cache[idx - 1]
            + cache[idx - 2]
            + cache[idx - 3]
         );
      }

      return cache[num];
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {number} num
    * @return {number}
    */
   tribonacci(num) {
      const cache = [0, 1, 1];

      for (let idx = 3; idx < num + 1; idx++) {
         cache[idx % 3] = cache[0] + cache[1] + cache[2];
      }

      return cache[num % 3];
   }
}


const tribonacci = new Solution().tribonacci;
console.log(new Solution().tribonacci(0) === 0)
console.log(new Solution().tribonacci(3) === 2)
console.log(new Solution().tribonacci(4) === 4)
console.log(new Solution().tribonacci(25) === 1389537)
console.log(new Solution().tribonacci(31) === 53798080)
console.log(new Solution().tribonacci(35) === 615693474)
