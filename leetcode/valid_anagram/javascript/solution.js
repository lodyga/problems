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
      if (text1.length !== text2.length) return false

      const letterFreq = Array(26).fill(0);

      for (let index = 0; index < text1.length; index++) {
         const idx = text1.charCodeAt(index) - 'a'.charCodeAt(0);
         letterFreq[idx]++;
      }

      for (let index = 0; index < text2.length; index++) {
         const idx = text2.charCodeAt(index) - 'a'.charCodeAt(0)
         letterFreq[idx]--;
         if (letterFreq[idx] === -1) return false
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

      const letterFreq = new Map();

      for (const letter of text1) {
         letterFreq.set(letter, (letterFreq.get(letter) || 0) + 1);
      }

      for (const letter of text2) {
         if ((letterFreq.get(letter) || 0) === 0) {
            return false
         }

         letterFreq[letter.charCodeAt(0) - 'a'.charCodeAt(0)]--;
      }
      return true
   };
}


const isAnagram = new Solution().isAnagram;
console.log(new Solution().isAnagram('anagram', 'nagaram') === true)
console.log(new Solution().isAnagram('rat', 'car') === false)
console.log(new Solution().isAnagram('', '') === true)
