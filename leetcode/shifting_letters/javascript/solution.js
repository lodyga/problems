class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: prefix sum
    * @param {string} text
    * @param {number[]} shifts
    * @return {string}
    */
   shiftingLetters(text, shifts) {
      const shiftLetter = (letter, shift) => {
         const letterIndex = letter.charCodeAt(0) - 'a'.charCodeAt(0);
         const shiftedIndex = letterIndex + shift;
         return String.fromCharCode(shiftedIndex % 26 + 'a'.charCodeAt(0))
      }

      const letters = Array.from(text);
      let shift = 0;

      for (let index = text.length - 1; index > -1; index--) {
         const letter = text[index];
         shift += shifts[index];
         letters[index] = shiftLetter(letter, shift);
      }
      return letters.join('')
   };
}


const shiftingLetters = new Solution().shiftingLetters;
console.log(new Solution().shiftingLetters('abc', [3, 5, 9]) === 'rpl')
console.log(new Solution().shiftingLetters('aaa', [1, 2, 3]) === 'gfd')