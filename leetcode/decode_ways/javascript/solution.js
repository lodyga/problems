class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: dp, bottom-up
    * @param {string} text
    * @return {number}
    */
   numDecodings(text) {
      const cache = [1, 1];

      for (let index = text.length - 1; index >= 0; index--) {
         if (text[index] === '0') {
            [cache[0], cache[1]] = [0, cache[0]];
            continue
         }

         let currentCache = cache[0];

         if (
            index + 1 < text.length &&
            text.slice(index, index + 2) <= '26'
         ) {
            currentCache += cache[1]
         }
         [cache[0], cache[1]] = [currentCache, cache[0]];
      }
      return cache[0]
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, bottom-up with cache as list
    * @param {string} text
    * @return {number}
    */
   numDecodings(text) {
      const cache = Array(text.length + 1).fill(0);
      cache[cache.length - 1] = 1;

      for (let index = text.length - 1; index >= 0; index--) {
         if (text[index] === '0')
            continue

         cache[index] = cache[index + 1];

         if (
            index + 1 < text.length &&
            text.slice(index, index + 2) <= '26'
         ) {
            cache[index] += cache[index + 2]
         }
      }
      return cache[0]
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, top-down with memoization as hash map
    * @param {string} text
    * @return {number}
    */
   numDecodings(text) {
      const memo = new Map([[text.length, 1]]);
      return dfs(0)

      function dfs(index) {
         if (memo.has(index)) {
            return memo.get(index)
         } else if (text[index] === '0') {
            return 0
         }
         
         memo.set(index, dfs(index + 1));
         if (
            index + 1 < text.length &&
            text.slice(index, index + 2) <= '26'
         ) {
            memo.set(index, memo.get(index) + dfs(index + 2));
         }
         
         return memo.get(index)
      }  
   };
}


console.log(new Solution().numDecodings('5') === 1)
console.log(new Solution().numDecodings('23') === 2)
console.log(new Solution().numDecodings('226') === 3)
console.log(new Solution().numDecodings('2261') === 3)
console.log(new Solution().numDecodings('12') === 2)
console.log(new Solution().numDecodings('2101') === 1)
console.log(new Solution().numDecodings('06') === 0)
console.log(new Solution().numDecodings('0') === 0)
console.log(new Solution().numDecodings('111111111111111111111111111111111111111111111') === 1836311903)