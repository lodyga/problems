class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: dp, bottom-up
    * @param {number[]} numbers
    * @return {number}
    */
   rob(numbers) {
      if (numbers.length <= 2) {
         return Math.max(...numbers)
      }
      let cache = Array(
         numbers[0],
         Math.max(numbers[0], numbers[1])
      );

      for (const number of numbers.slice(2,)) {
         cache = [cache[1], Math.max(cache[0] + number, cache[1])];
      }
      return cache[cache.length - 1]
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, bottom-up
    * mutate input list
    * @param {number[]} numbers
    * @return {number}
    */
   rob(numbers) {
      if (numbers.length <= 2) {
         return Math.max(...numbers)
      }
      numbers[1] = Math.max(...numbers.slice(0, 2));

      for (let index = 2; index < numbers.length; index++) {
         numbers[index] = Math.max(
            numbers[index] + numbers[index - 2],
            numbers[index - 1]);
      }
      return numbers[numbers.length - 1]
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, bottom-up
    * @param {number[]} numbers
    * @return {number}
    */
   rob(numbers) {
      if (numbers.length <= 2) {
         return Math.max(...numbers)
      }
      const cache = Array(numbers.length);
      cache[0] = numbers[0];
      cache[1] = Math.max(...numbers.slice(0, 2));

      for (let index = 2; index < numbers.length; index++) {
         cache[index] = Math.max(
            numbers[index] + cache[index - 2],
            cache[index - 1]);
      }
      return cache[cache.length - 1]
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, top-down with memoization as hash map
    * @param {number[]} numbers
    * @return {number}
    */
   rob(numbers) {
      const memo = new Map();
      memo.set(numbers.length, 0);
      memo.set(numbers.length + 1, 0);

      function dfs(index) {
         if (memo.get(index) !== undefined)
            return memo.get(index)

         return Math.max(
            numbers[index] + dfs(index + 2),
            dfs(index + 1)
         )
      }
      return dfs(0)
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, top-down with memoization as list
    * @param {number[]} numbers
    * @return {number}
    */
   rob(numbers) {
      const memo = Array(numbers.length + 1).fill(null);
      memo[numbers.length] = 0;
      memo[numbers.length + 1] = 0;

      function dfs(index) {
         if (memo[index] !== null)
            return memo[index]

         return Math.max(
            numbers[index] + dfs(index + 2),
            dfs(index + 1)
         )
      }
      return dfs(0)
   };
}


class Solution {
   /**
    * Time complexity: O(2^n)
    * Auxiliary space complexity: O(n)
    * Tags: brute-force, tle
    * @param {number[]} numbers
    * @return {number}
    */
   rob(numbers) {
      function dfs(index) {
         if (index >= numbers.length)
            return 0

         return Math.max(
            numbers[index] + dfs(index + 2),
            dfs(index + 1)
         )
      }
      return dfs(0)
   };
}


console.log(new Solution().rob([2]) === 2)
console.log(new Solution().rob([0]) === 0)
console.log(new Solution().rob([2, 1]) === 2)
console.log(new Solution().rob([2, 100, 9, 3, 100]) === 200)
console.log(new Solution().rob([100, 9, 3, 100, 2]) === 200)
console.log(new Solution().rob([1, 2, 3, 1]) === 4)
console.log(new Solution().rob([2, 7, 9, 3, 1]) === 12)
console.log(new Solution().rob([183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168, 128, 177, 235, 50, 81, 185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]) === 3365)
console.log(new Solution().rob([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) === 0)