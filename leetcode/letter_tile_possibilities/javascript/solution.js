class Solution {
   /**
    * Time complexity: O(n!)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map
    *     A: recursion
    * @param {string} tiles
    * @return {number}
    */
   numTilePossibilities(tiles) {
      const letterFreq = new Map();

      for (const tile of tiles) {
         letterFreq.set(tile, (letterFreq.get(tile) || 0) + 1);
      }

      const backtrack = () => {
         let res = 0;

         for (const letter of [...letterFreq.keys()]) {
            letterFreq.set(letter, letterFreq.get(letter) - 1);

            if (letterFreq.get(letter) === 0) {
               letterFreq.delete(letter);
            }

            res += 1 + backtrack();
            letterFreq.set(letter, (letterFreq.get(letter) || 0) + 1);
         }

         return res
      }

      return backtrack()
   };
}


const numTilePossibilities = new Solution().numTilePossibilities;
console.log(new Solution().numTilePossibilities("AAB") === 8)
console.log(new Solution().numTilePossibilities("AAABBC") === 188)
console.log(new Solution().numTilePossibilities("V") === 1)
