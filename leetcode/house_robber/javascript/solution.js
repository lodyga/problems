class Solution {
   /**
    * Time complexity: O(2^n)
    * Auxiliary space complexity: O(n)
    * Tags: brute-force, tle
    * @param {number[]} houses
    * @return {number}
    */
   rob(houses) {
      const dfs = (index) => {
         if (index >= houses.length)
            return 0

         const robHouse = houses[index] + dfs(index + 2);
         const skipHouse = dfs(index + 1);
         return Math.max(robHouse, skipHouse)
      }
      return dfs(0)
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, top-down with memoization as hash map
    * @param {number[]} houses
    * @return {number}
    */
   rob(houses) {
      const memo = new Map();
      
      const dfs = (index) => {
         if (index >= houses.length)
            return 0
         else if (memo.has(index))
            return memo.get(index)

         const robHouse = houses[index] + dfs(index + 2);
         const skipHouse = dfs(index + 1);
         memo.set(index, Math.max(robHouse, skipHouse));
         return memo.get(index)
      }
      return dfs(0)
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, top-down with memoization as array
    * @param {number[]} houses
    * @return {number}
    */
   rob(houses) {
      const memo = Array(houses.length).fill(-1);
      
      const dfs = (index) => {
         if (index >= houses.length)
            return 0
         else if (memo[index] !== -1)
            return memo[index]

         const robHouse = houses[index] + dfs(index + 2);
         const skipHouse = dfs(index + 1);
         memo[index] = Math.max(robHouse, skipHouse);
         return memo[index]
      }
      return dfs(0)
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, bottom-up
    * @param {number[]} houses
    * @return {number}
    */
   rob(houses) {
      const cache = Array(houses.length + 2).fill(0);
      
      for (let index = houses.length - 1; index > -1; index--) {
         const robHouse = houses[index] + cache[index + 2];
         const skipHouse = cache[index + 1]
         cache[index] = Math.max(robHouse, skipHouse);
      }
      return cache[0]
   };
}


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
    * Auxiliary space complexity: O(1)
    * Tags: dp, bottom-up
    * @param {number[]} houses
    * @return {number}
    */
   rob(houses) {
      const cache = [0, 0];
      
      for (let index = houses.length - 1; index > -1; index--) {
         const robHouse = houses[index] + cache[1];
         const skipHouse = cache[0];
         [cache[0], cache[1]] = [Math.max(robHouse, skipHouse), cache[0]];
      }
      return cache[0]
   };
}


const rob = new Solution().rob;
console.log(new Solution().rob([2]) === 2)
console.log(new Solution().rob([0]) === 0)
console.log(new Solution().rob([2, 1]) === 2)
console.log(new Solution().rob([2, 100, 9, 3, 100]) === 200)
console.log(new Solution().rob([100, 9, 3, 100, 2]) === 200)
console.log(new Solution().rob([1, 2, 3, 1]) === 4)
console.log(new Solution().rob([2, 7, 9, 3, 1]) === 12)
console.log(new Solution().rob([183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168, 128, 177, 235, 50, 81, 185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]) === 3365)
console.log(new Solution().rob([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) === 0)