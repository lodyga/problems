class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: top-down
    * @param {string} text
    * @return {number}
    */
   numDecodings(text) {
      const memo = Array(text.length).fill(-1);
      memo.push(1);

      const dfs = (idx) => {
         if (memo[idx] !== -1) {
            return memo[idx]
         }

         const char = text[idx];

         if (char === '0') {
            return 0
         }

         let res = dfs(idx + 1);

         if (
            idx + 1 < text.length &&
            (
               char === '1' ||
               (char === '2' && text[idx + 1] <= '6')
            )
         )
            res += dfs(idx + 2);

         memo[idx] = res
         return res
      }
      return dfs(0)
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {string} text
    * @return {number}
    */
   numDecodings(text) {
      const cache = Array(text.length).fill(0);
      cache.push(1);

      for (let idx = text.length - 1; idx > -1; idx--) {
         const char = text[idx];
         if (char === '0') {
            continue
         }

         cache[idx] = cache[idx + 1];

         if (
            idx + 1 < text.length &&
            (
               char === '1' ||
               (char === '2' && text[idx + 1] <= '6'))
         ) {
            cache[idx] += cache[idx + 2];
         }
      }

      return cache[0]
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {string} text
    * @return {number}
    */
   numDecodings(text) {
      const cache = Array(2).fill(1);

      for (let idx = text.length - 1; idx > -1; idx--) {
         const char = text[idx];

         if (char === '0') {
            [cache[0], cache[1]] = [0, cache[0]];
            continue
         }

         let cache0 = cache[0];

         if (
            idx + 1 < text.length &&
            (
               char === '1' ||
               (char === '2' && text[idx + 1] <= '6'))
         ) {
            cache0 += cache[1];
         }

         [cache[0], cache[1]] = [cache0, cache[0]];
      }

      return cache[0]
   }
}


const numDecodings = new Solution().numDecodings;
console.log(new Solution().numDecodings('5') === 1)
console.log(new Solution().numDecodings('23') === 2)
console.log(new Solution().numDecodings('27') === 1)
console.log(new Solution().numDecodings('226') === 3)
console.log(new Solution().numDecodings('2261') === 3)
console.log(new Solution().numDecodings('12') === 2)
console.log(new Solution().numDecodings('2101') === 1)
console.log(new Solution().numDecodings('06') === 0)
console.log(new Solution().numDecodings('0') === 0)
console.log(new Solution().numDecodings('2617') == 4)
console.log(new Solution().numDecodings('111111111111111111111111111111111111111111111') === 1836311903)
