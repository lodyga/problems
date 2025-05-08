class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: hash map, hash set
    * @param {string} pattern
    * @param {string[]} text
    * @return {boolean}
    */
   wordPattern(pattern, text) {
      const wordList = text.split(' ');
      const uniqueWords = new Set();
      const letterToWordMap = new Map();

      if (pattern.length !== wordList.length)
         return false

      for (let index = 0; index < pattern.length; index++) {
         const letter = pattern[index];
         const word = wordList[index];

         if (!letterToWordMap.has(letter)) {
            if (uniqueWords.has(word))
               return false
            letterToWordMap.set(letter, word);
            uniqueWords.add(word);
         } else {
            if (letterToWordMap.get(letter) !== word)
               return false
         }
      }
      return true
   };
}
const wordPattern = new Solution().wordPattern;


console.log(new Solution().wordPattern('abba', 'dog cat cat dog'), true)
console.log(new Solution().wordPattern('abba', 'dog cat cat fish'), false)
console.log(new Solution().wordPattern('aaaa', 'dog cat cat dog'), false)
console.log(new Solution().wordPattern('abba', 'dog dog dog dog'), false)