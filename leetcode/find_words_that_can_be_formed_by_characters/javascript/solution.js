class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags: hash map
    * @param {string[]} words
    * @param {string} chars
    * @return {number}
    */
   countCharacters(words, chars) {
      const charLeterFrequency = new Map();
      let lengthsSum = 0;

      for (const char of chars) {
         charLeterFrequency.set(char, (charLeterFrequency.get(char) || 0) + 1);
      }
      for (const word of words) {
         if (isWordGood(word))
            lengthsSum += word.length;
      }
      return lengthsSum

      function isWordGood(word) {
         const charLeterFrequencyCopy = new Map(charLeterFrequency);

         for (const letter of word) {
            if (
               !charLeterFrequencyCopy.has(letter) ||
               charLeterFrequencyCopy.get(letter) === 0
            ) {
               return false
            }
            charLeterFrequencyCopy.set(letter, charLeterFrequencyCopy.get(letter) - 1);
         }
         return true
      };
   };
}
const countCharacters = new Solution().countCharacters;


console.log(new Solution().countCharacters(['cat', 'bt', 'hat', 'tree'], 'atach'), 6)
console.log(new Solution().countCharacters(['hello', 'world', 'leetcode'], 'welldonehoneyr'), 10)