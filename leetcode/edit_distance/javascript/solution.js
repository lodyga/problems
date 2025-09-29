class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags: dp, top-down with memoization as hash map
    * @param {string} word1
    * @param {string} word2
    * @return {number}
    */
   minDistance(word1, word2) {
      const UPPER_BOUND = word1.length + word2.length;
      const memo = new Map();

      const dfs = (index1, index2) => {
         if (index1 === word1.length)
            return word2.length - index2
         else if (index2 === word2.length)
            return word1.length - index1
         else if (memo.has(`${index1},${index2}`))
            return memo.get(`${index1},${index2}`)

         let distance;
         if (word1[index1] === word2[index2]) {
            distance = dfs(index1 + 1, index2 + 1);
         } else {
            // insert
            const insertChar = dfs(index1 + 1, index2);
            // delete
            const deleteChar = dfs(index1, index2 + 1);
            // replace
            const replaceChar = dfs(index1 + 1, index2 + 1);
            distance = Math.min(insertChar, deleteChar, replaceChar) + 1
         }

         memo.set(`${index1},${index2}`, distance)
         return distance
      }
      return dfs(0, 0)
   };
}


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags: dp, bottom-up with tabulation as array
    * @param {string} word1
    * @param {string} word2
    * @return {number}
    */
   minDistance(word1, word2) {
      const ROWS = word1.length;
      const COLS = word2.length;
      // [[index1][index2]: min distance]
      const cache = Array.from({ length: ROWS + 1 }, () => Array(COLS + 1).fill(ROWS + COLS));

      for (let row = 0; row < ROWS + 1; row++) {
         cache[row][COLS] = ROWS - row;
      }
      for (let col = 0; col < COLS + 1; col++) {
         cache[ROWS][col] = COLS - col;
      }

      for (let row = ROWS - 1; row > -1; row--) {
         for (let col = COLS - 1; col > -1; col--) {
            if (word1[row] === word2[col])
               // match
               cache[row][col] = cache[row + 1][col + 1]
            else
               cache[row][col] = 1 + Math.min(
                  // replace
                  cache[row + 1][col + 1],
                  // delete
                  cache[row + 1][col],
                  // insert
                  cache[row][col + 1]
               );
         }
      }
      return cache[0][0]
   };
}


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags: dp, bottom-up with tabulation as array
    * @param {string} word1
    * @param {string} word2
    * @return {number}
    */
   minDistance(word1, word2) {
      const ROWS = word1.length;
      const COLS = word2.length;
      // [[index1][index2]: min distance]
      let nextCache = Array.from({ length: COLS + 1 }, (_, col) => (COLS - col))

      for (let row = ROWS - 1; row > -1; row--) {
         let cache = Array(COLS + 1).fill(ROWS - row);

         for (let col = COLS - 1; col > -1; col--) {
            if (word1[row] === word2[col])
               // match
               cache[col] = nextCache[col + 1]
            else
               cache[col] = 1 + Math.min(
                  // replace
                  nextCache[col + 1],
                  // delete
                  nextCache[col],
                  // insert
                  cache[col + 1]
               );
         }
         nextCache = cache;
      }
      return nextCache[0]
   };
}
const minDistance = new Solution().minDistance;


console.log(new Solution().minDistance('a', 'a') === 0)
console.log(new Solution().minDistance('', 'b') === 1)
console.log(new Solution().minDistance('b', '') === 1)
console.log(new Solution().minDistance('a', 'b') === 1)
console.log(new Solution().minDistance('ab', 'b') === 1)
console.log(new Solution().minDistance('ba', 'b') === 1)
console.log(new Solution().minDistance('b', 'ba') === 1)
console.log(new Solution().minDistance('aa', 'b') === 2)
console.log(new Solution().minDistance('horse', 'ros') === 3)
console.log(new Solution().minDistance('intention', 'execution') === 5)
console.log(new Solution().minDistance('dinitrophenylhydrazine', 'acetylphenylhydrazine') === 6)