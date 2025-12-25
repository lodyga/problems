class Solution {
   /**
    * Time complexity: O(n*k)
    *     n: word count
    *     k: avg word length
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: hash map, string
    *     A: iteration
    * @param {string[]} words
    * @param {string} order
    * @return {boolean}
    */
   isAlienSorted(words, order) {
      const letterIndex = new Map([...order].map((letter, index) => [letter, index]));

      for (let index = 0; index < words.length - 1; index++) {
         const word1 = words[index];
         const word2 = words[index + 1];

         for (let i2 = 0; i2 < word1.length; i2++) {
            if (
               i2 === word2.length ||
               letterIndex.get(word1[i2]) > letterIndex.get(word2[i2])
            )
               return false
            else if (letterIndex.get(word1[i2]) < letterIndex.get(word2[i2]))
               break
         }
      }
      return true
   };
}


const isAlienSorted = new Solution().isAlienSorted;
console.log(new Solution().isAlienSorted(['hello', 'leetcode'], 'hlabcdefgijkmnopqrstuvwxyz') === true)
console.log(new Solution().isAlienSorted(['word', 'world', 'row'], 'worldabcefghijkmnpqstuvxyz') === false)
console.log(new Solution().isAlienSorted(['apple', 'app'], 'abcdefghijklmnopqrstuvwxyz') === false)
console.log(new Solution().isAlienSorted(['ubg', 'kwh'], 'qcipyamwvdjtesbghlorufnkzx') === true)
console.log(new Solution().isAlienSorted(['kuvp', 'q'], 'ngxlkthsjuoqcpavbfdermiywz') === true)
