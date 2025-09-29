class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags: dp, top-down with memoization as hash map
    * @param {string} text1
    * @param {string} text2
    * @return {number}
    */
   numDistinct(text1, text2) {
      const memo = new Map();

      const dfs = (index1, index2) => {
         if (index2 === text2.length)
            return 1
         else if (index1 === text1.length)
            return 0
         else if (memo.has(`${index1},${index2}`))
            return memo.get(`${index1},${index2}`)

         const letter1 = text1[index1];
         const letter2 = text2[index2];

         // skip letter
         let subCounter = dfs(index1 + 1, index2);

         // take letter
         if (letter1 === letter2)
            subCounter += dfs(index1 + 1, index2 + 1)

         memo.set(`${index1},${index2}`, subCounter);
         return subCounter
      };

      return dfs(0, 0)
   };
}


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags: dp, top-down with memoization as array
    * @param {string} text1
    * @param {string} text2
    * @return {number}
    */
   numDistinct(text1, text2) {
      const memo = Array.from({ length: text1.length }, () => Array(text2.length).fill(-1));

      const dfs = (index1, index2) => {
         if (index2 === text2.length)
            return 1
         else if (index1 === text1.length)
            return 0
         else if (memo[index1][index2] !== -1)
            return memo[index1][index2]

         const letter1 = text1[index1];
         const letter2 = text2[index2];

         // skip letter
         let subCounter = dfs(index1 + 1, index2);

         // take letter
         if (letter1 === letter2)
            subCounter += dfs(index1 + 1, index2 + 1)

         memo[index1][index2] = subCounter;
         return subCounter
      };

      return dfs(0, 0)
   };
}


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags: dp, bottom-up
    * @param {string} text1
    * @param {string} text2
    * @return {number}
    */
   numDistinct(text1, text2) {
      const ROWS = text1.length;
      const COLS = text2.length;
      const cache = Array.from({ length: ROWS + 1 }, () => Array(COLS + 1).fill(0));
      for (let row = 0; row < ROWS + 1; row++)
         cache[row][COLS] = 1

      for (let row = ROWS - 1; row > -1; row--) {
         for (let col = COLS - 1; col > - 1; col--) {
            cache[row][col] = cache[row + 1][col];
            if (text1[row] === text2[col])
               cache[row][col] += cache[row + 1][col + 1];
         }
      }
   return cache[0][0]
   };
}


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags: dp, bottom-up
    * @param {string} text1
    * @param {string} text2
    * @return {number}
    */
   numDistinct(text1, text2) {
      const ROWS = text1.length;
      const COLS = text2.length;
      let nextCache = Array(COLS + 1).fill(0);
      nextCache[nextCache.length - 1] = 1;

      for (let row = ROWS - 1; row > -1; row--) {
         const currentCache = Array(COLS + 1).fill(0);
         currentCache[currentCache.length - 1] = 1;

         for (let col = COLS - 1; col > - 1; col--) {
            currentCache[col] = nextCache[col];
            if (text1[row] === text2[col])
               currentCache[col] += nextCache[col + 1];
         }
         nextCache = currentCache;
      }
   return nextCache[0]
   };
}

const numDistinct = new Solution().numDistinct;
console.log(new Solution().numDistinct('rabbbit', 'rabbit') === 3)
console.log(new Solution().numDistinct('babgbag', 'bag') === 5)
console.log(new Solution().numDistinct('daacaedaceacabbaabdccdaaeaebacddadcaeaacadbceaecddecdeedcebcdacdaebccdeebcbdeaccabcecbeeaadbccbaeccbbdaeadecabbbedceaddcdeabbcdaeadcddedddcececbeeabcbecaeadddeddccbdbcdcbceabcacddbbcedebbcaccac', 'ceadbaa') === 8556153)