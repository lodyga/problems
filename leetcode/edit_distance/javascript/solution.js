class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array
    *     A: top-down
    * @param {string} word1
    * @param {string} word2
    * @return {number}
    */
   minDistance(word1, word2) {
      const UPPER_BOUND = word1.length + word2.length;
      // memo = [(index1, index2): min distance]
      const memo = Array.from({ length: word1.length }, () => Array(word2.length).fill(-1));

      const dfs = (index1, index2) => {
         if (index1 === word1.length ||
            index2 === word2.length
         )
            return word2.length - index2 || word1.length - index1
         else if (memo[index1][index2] !== -1)
            return memo[index1][index2]

         let distance;
         // if letter match
         if (word1[index1] === word2[index2]) {
            distance = dfs(index1 + 1, index2 + 1);
         } else {
            const insertChr = dfs(index1 + 1, index2);
            const deleteChr = dfs(index1, index2 + 1);
            const replaceChr = dfs(index1 + 1, index2 + 1);
            distance = 1 + Math.min(insertChr, deleteChr, replaceChr);
         }

         memo[index1][index2] = distance
         return distance
      }
      return dfs(0, 0)
   };

   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {string} word1
    * @param {string} word2
    * @return {number}
    */
   minDistance(word1, word2) {
      const ROWS = word1.length;
      const COLS = word2.length;
      // cache = [(index1, index2): min distance]
      const cache = Array.from({ length: ROWS + 1 }, () => Array(COLS + 1).fill(0));

      for (let row = 0; row < ROWS; row++) {
         cache[row][COLS] = ROWS - row;
      }
      for (let col = 0; col < COLS; col++) {
         cache[ROWS][col] = COLS - col;
      }

      for (let row = ROWS - 1; row > -1; row--) {
         for (let col = COLS - 1; col > -1; col--) {
            // if letter match
            if (word1[row] === word2[col])
               cache[row][col] = cache[row + 1][col + 1]
            else
               cache[row][col] = 1 + Math.min(
                  // insert
                  cache[row][col + 1],
                  // delete
                  cache[row + 1][col],
                  // replace
                  cache[row + 1][col + 1]
               );
         }
      }
      return cache[0][0]
   };

   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {string} word1
    * @param {string} word2
    * @return {number}
    */
   minDistance(word1, word2) {
      const ROWS = word1.length;
      const COLS = word2.length;
      // cache = [index2: min distance]
      let nextCache = Array.from({ length: COLS + 1 }, (_, col) => (COLS - col))

      for (let row = ROWS - 1; row > -1; row--) {
         const cache = Array(COLS + 1).fill(ROWS - row);

         for (let col = COLS - 1; col > -1; col--) {
            // if letter match
            if (word1[row] === word2[col])
               cache[col] = nextCache[col + 1]
            else
               cache[col] = 1 + Math.min(
                  // insert
                  cache[col + 1],
                  // delete
                  nextCache[col],
                  // replace
                  nextCache[col + 1]
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
