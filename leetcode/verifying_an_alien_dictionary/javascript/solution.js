class Solution {
   /**
    * Time complexity: O(n*k)
    *     n: word count
    *     k: avg word length
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array, string
    *     A: iteration
    * @param {string[]} words
    * @param {string} order
    * @return {boolean}
    */
   isAlienSorted(words, order) {
      const areTwoWordsSorted = (word1, word2) => {
         for (let idx = 0; idx < Math.max(word1.length, word2.length); idx++) {
            if (idx === word1.length) {
               return true;
            }
            else if (idx === word2.length) {
               return false;
            }

            const letter1 = word1[idx];
            const letter2 = word2[idx];

            if (letter1 === letter2) {
               continue;
            }
            else if (letterIdx[letter1.charCodeAt(0) - 'a'.charCodeAt(0)] < letterIdx[letter2.charCodeAt(0) - 'a'.charCodeAt(0)]) {
               return true;
            }
            else {  // else if letterIdx[letter1] > letterIdx[letter2]{
               return false;
            }
         }

         return true;
      }

      const letterIdx = Array(26);
      
      for (let idx = 0; idx < order.length; idx++) {
         const letter = [...order][idx];
         const i = letter.charCodeAt(0) - 'a'.charCodeAt(0);
         letterIdx[i] = idx;
      }

      for (let idx = 0; idx < words.length - 1; idx++) {
         const word1 = words[idx];
         const word2 = words[idx + 1];

         if (!areTwoWordsSorted(word1, word2)) {
            return false;
         }
      }

      return true;
   }
}


const isAlienSorted = new Solution().isAlienSorted;
console.log(new Solution().isAlienSorted(['hello', 'leetcode'], 'hlabcdefgijkmnopqrstuvwxyz') === true)
console.log(new Solution().isAlienSorted(['word', 'world', 'row'], 'worldabcefghijkmnpqstuvxyz') === false)
console.log(new Solution().isAlienSorted(['apple', 'app'], 'abcdefghijklmnopqrstuvwxyz') === false)
console.log(new Solution().isAlienSorted(['ubg', 'kwh'], 'qcipyamwvdjtesbghlorufnkzx') === true)
console.log(new Solution().isAlienSorted(['kuvp', 'q'], 'ngxlkthsjuoqcpavbfdermiywz') === true)
