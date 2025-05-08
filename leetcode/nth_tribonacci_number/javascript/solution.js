class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: dp, bottom-up
    * @param {number} number
    * @return {number}
    */
   tribonacci = function (number) {
      const cache = [0, 1, 1];

      for (let index = 3; index < number + 1; index++) {
         const last = cache[0] + cache[1] + cache[2];
         [cache[0], cache[1], cache[2]] = [cache[1], cache[2], last];
      }
      return cache[2]
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, bottom-up
    * @param {number} number
    * @return {number}
    */
   tribonacci = function (number) {
      const cache = Array(number + 1).fill(1);
      cache[0] = 0;

      for (let index = 3; index < number + 1; index++) {
         cache[index] = (
            cache[index - 1] +
            cache[index - 2] +
            cache[index - 3]);
      }
      return cache[number]
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, top-down with memoization as hash map
    * @param {number} number
    * @return {number}
    */
   tribonacci = function (number) {
      const memo = new Map([[0, 0], [1, 1], [2, 1]]);

      function dfs(number) {
         if (memo.has(number)) {
            return memo.get(number)
         }
         const value = dfs(number - 1) + dfs(number - 2) + dfs(number - 3);
         memo.set(number, value)
         return memo.get(number)
      }
      return dfs(number)
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: dp, bottom-up, fancy
    * @param {number} number
    * @return {number}
    */
   tribonacci = function (number) {
      const triplet = [0, 1, 1];

      for (let index = 3; index < number + 1; index++) {
         triplet[index % 3] = triplet.reduce((total, current) => total + current);
      }

      return triplet[number % 3]
   };
}


console.log(new Solution().tribonacci(0), 0)
console.log(new Solution().tribonacci(3), 2)
console.log(new Solution().tribonacci(4), 4)
console.log(new Solution().tribonacci(25), 1389537)
console.log(new Solution().tribonacci(31), 53798080)
console.log(new Solution().tribonacci(35), 615693474)