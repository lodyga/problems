class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: hash map
    * @param {string} word1
    * @param {string} word2
    * @return {boolean}
    */
   isIsomorphic(word1, word2) {
      if (word1.length !== word2.length) {
         return false
      }
      const letter1MapLetter2 = new Map();
      const letters2 = new Set();

      for (let index = 0; index < word1.length; index++) {
         const letter1 = word1[index];
         const letter2 = word2[index];

         if (letter1MapLetter2.has(letter1)) {
            if (letter1MapLetter2.get(letter1) !== letter2) {
               return false
            }
         } else {
            if (letters2.has(letter2)) {
               return false
            }
            letter1MapLetter2.set(letter1, letter2);
            letters2.add(letter2);
         }
      }
      return true
   };
}
const isIsomorphic = new Solution().isIsomorphic;


console.log(new Solution().isIsomorphic('egg', 'add'), true)
console.log(new Solution().isIsomorphic('foo', 'bar'), false)
console.log(new Solution().isIsomorphic('paper', 'title'), true)
console.log(new Solution().isIsomorphic('badc', 'baba'), false)