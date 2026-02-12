class Solution {
   /**
    * Time complexity: O(n + s)
    *     n: text length
    *     s: shifts length
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array, string
    *     A: prefix sum
    * @param {string} text
    * @param {number[][]} shifts
    * @return {string}
    */
   shiftingLetters(text, shifts) {
      const A = 'a'.charCodeAt(0);
      const letterVals = text.split('').map(letter => letter.charCodeAt(0) - A);
      const suffix = Array(text.length).fill(0);
      let shift = 0;

      for (let index = 0; index < shifts.length; index++) {
         const [start, end, direction] = shifts[index];
         suffix[end] += direction ? 1 : -1;

         if (start) {
            suffix[start - 1] += direction ? -1 : 1;
         }
      }

      for (let index = text.length - 1; index > -1; index--) {
         shift += suffix[index];
         letterVals[index] += shift;
      }

      return letterVals
         .map(val => String.fromCharCode(((val % 26) + 26) % 26 + A))
         .join('');

   };
}


const shiftingLetters = new Solution().shiftingLetters;
console.log(new Solution().shiftingLetters('abc', [[0, 1, 0], [1, 2, 1], [0, 2, 1]]) === 'ace')
console.log(new Solution().shiftingLetters('dztz', [[0, 0, 0], [1, 1, 1]]) === 'catz')
