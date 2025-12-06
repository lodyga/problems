class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array
    *     A: iteration
    * @param {string} text1 
    * @param {string} text2 
    * @returns {boolean}
    */
   isAnagram(text1, text2) {
      if (text1.length !== text2.length)
         return false

      const letterFrequency = Array(26).fill(0);

      for (let index = 0; index < text1.length; index++) {
         letterFrequency[text1.charCodeAt(index) - 'a'.charCodeAt(0)]++;
         letterFrequency[text2.charCodeAt(index) - 'a'.charCodeAt(0)]--;
      }

      for (const frequency of letterFrequency) {
         if (frequency !== 0)
            return false
      }
      return true
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: hash map
    *     A: iteration
    * @param {string} text1 
    * @param {string} text2 
    * @returns {boolean}
    */
   isAnagram(text1, text2) {
      if (text1.length !== text2.length)
         return false

      const letterFrequency = new Map();

      for (const letter of text1) {
         letterFrequency.set(letter, (letterFrequency.get(letter) || 0) + 1);
      }
      for (const letter of text2) {
         if (letterFrequency.has(letter)) {
            letterFrequency[letter.charCodeAt(0) - 'a'.charCodeAt(0)]--;
            if (letterFrequency.get(letter) === 0)
               letterFrequency.delete(letter);
         } else {
            return false
         }
      }
      return true
   };
}


const isAnagram = new Solution().isAnagram;
console.log(new Solution().isAnagram('anagram', 'nagaram') === true)
console.log(new Solution().isAnagram('rat', 'car') === false)
console.log(new Solution().isAnagram('', '') === true)
