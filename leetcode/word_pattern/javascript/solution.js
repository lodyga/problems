class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map, hash set
    *     A: iteration
    * @param {string} pattern
    * @param {string[]} text
    * @return {boolean}
    */
   wordPattern(pattern, text) {
      const words = text.split(' ');
      if (pattern.length !== words.length)
         return false

      const letterMap = new Map();
      const wordSet = new Set();

      for (let index = 0; index < pattern.length; index++) {
         const letter = pattern[index];
         const word = words[index];

         if (letterMap.has(letter)) {
            if (letterMap.get(letter) !== word)
               return false
         } else {
            if (wordSet.has(word))
               return false
            letterMap.set(letter, word);
            wordSet.add(word);
         }
      }
      return true
   };
}


const wordPattern = new Solution().wordPattern;
console.log(new Solution().wordPattern('abba', 'dog cat cat dog') === true)
console.log(new Solution().wordPattern('abba', 'dog cat cat fish') === false)
console.log(new Solution().wordPattern('aaaa', 'dog cat cat dog') === false)
console.log(new Solution().wordPattern('abba', 'dog dog dog dog') === false)
console.log(new Solution().wordPattern('aaa', 'aa aa aa aa') === false)
