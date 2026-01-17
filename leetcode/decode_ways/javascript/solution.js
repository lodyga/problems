class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, top-down with memoization as hash map
    * @param {string} text
    * @return {number}
    */
   numDecodings(text) {
      const memo = Array(text.length + 1).fill(-1);
      memo[memo.length - 1] = 1;

      const dfs = (index) => {
         if (memo[index] !== -1) {
            return memo[index]
         }

         const num = text[index];
         // (0-9)
         let oneDigitNum = 0;
         if (num !== '0')
            oneDigitNum = dfs(index + 1);
         // (10-26)
         let twoDigitNum = 0;
         if (
            index + 1 < text.length &&
            (num === '1' ||
               (num === '2' && text[index + 1] >= '0' && text[index + 1] <= '6'))
         )
            twoDigitNum = dfs(index + 2);

         memo[index] = oneDigitNum + twoDigitNum;
         return memo[index]
      }
      return dfs(0)
   };

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
      const cache = Array(text.length + 1).fill(0);
      cache[cache.length - 1] = 1;

      for (let index = text.length - 1; index > -1; index--) {
         const num = text[index];
         if (num === '0')
            continue

         cache[index] = cache[index + 1];

         if (
            index + 1 < text.length &&
            (num === '1' ||
               (num === '2' && text[index + 1] >= '0' && text[index + 1] <= '6'))
         ) {
            cache[index] += cache[index + 2];
         }
      }
      return cache[0]
   };

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

      for (let index = text.length - 1; index > -1; index--) {
         const num = text[index];
         if (num === '0') {
            cache[1] = cache[0];
            cache[0] = 0;
            continue
         }

         let cacheAtIndex = cache[0];

         if (
            index + 1 < text.length &&
            (num === '1' ||
               (num === '2' && text[index + 1] >= '0' && text[index + 1] <= '6'))
         ) {
            cacheAtIndex += cache[1];
         }
         cache[1] = cache[0];
         cache[0] = cacheAtIndex;
      }
      return cache[0]
   };
}


const numDecodings = new Solution().numDecodings;
console.log(new Solution().numDecodings('5') === 1)
console.log(new Solution().numDecodings('23') === 2)
console.log(new Solution().numDecodings('226') === 3)
console.log(new Solution().numDecodings('2261') === 3)
console.log(new Solution().numDecodings('12') === 2)
console.log(new Solution().numDecodings('2101') === 1)
console.log(new Solution().numDecodings('06') === 0)
console.log(new Solution().numDecodings('0') === 0)
console.log(new Solution().numDecodings('2617') == 4)
console.log(new Solution().numDecodings('111111111111111111111111111111111111111111111') === 1836311903)
