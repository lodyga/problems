class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags: dp, bottom-up
    * @param {string} text1
    * @param {string} text2
    * @return {number}
    */
   longestCommonSubsequence(text1, text2) {
      const rows = text2.length + 1;
      const cols = text1.length + 1;
      const cache = Array.from({ length: rows }, () => Array(cols).fill(0));

      for (let row = rows - 2; row >= 0; row--) {
         for (let col = cols - 2; col >= 0; col--) {
            if (text2[row] === text1[col]) {
               cache[row][col] = cache[row + 1][col + 1] + 1
            } else {
               cache[row][col] = Math.max(
                  cache[row + 1][col],
                  cache[row][col + 1]
               )
            }
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
   longestCommonSubsequence(text1, text2) {
      const rows = text2.length + 1;
      const cols = text1.length + 1;
      const prevCache = Array(cols).fill(0);
      
      for (let row = rows - 2; row >= 0; row--) {
         const cache = Array(cols).fill(0);

         for (let col = cols - 2; col >= 0; col--) {
            if (text2[row] === text1[col]) {
               cache[col] = prevCache[col + 1] + 1
            } else {
               cache[col] = Math.max(
                  prevCache[col],
                  cache[col + 1]
               )
            }
         }
         cache.forEach((value, index) => prevCache[index] = value);
      }
      return prevCache[0]
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
   longestCommonSubsequence(text1, text2) {
      const rows = text2.length;
      const cols = text1.length;
      const memo = Array.from({ length: rows }, () => Array(cols).fill(null));

      function dfs(row, col) {
         if (row === rows || col === cols) {
            return 0
         } else if (memo[row][col] !== null) {
            return memo[row][col]
         }

         if (text1[col] === text2[row]) {
            memo[row][col] = dfs(row + 1, col + 1) + 1;
         } else {
            memo[row][col] = Math.max(
               dfs(row + 1, col),
               dfs(row, col + 1)
            )
         }
         return memo[row][col]
      }
      return dfs(0, 0)
   };
}


console.log(new Solution().longestCommonSubsequence('abcde', 'ace') === 3)
console.log(new Solution().longestCommonSubsequence('abc', 'abc') === 3)
console.log(new Solution().longestCommonSubsequence('abc', 'def') === 0)
console.log(new Solution().longestCommonSubsequence('bsbininm', 'jmjkbkjkv') === 1)
console.log(new Solution().longestCommonSubsequence('pmjghexybyrgzczy', 'hafcdqbgncrcbihkd') === 4)