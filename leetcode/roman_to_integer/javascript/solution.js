class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: 
    * @param {string} text
    * @return {number}
    */
   romanToInt(text) {
      let number = 0
      const valueMap = new Map([
         ["I", 1],
         ["V", 5],
         ["X", 10],
         ["L", 50],
         ["C", 100],
         ["D", 500],
         ["M", 1000]
      ])

      let index = 0;
      while (index < text.length) {
         const letter = text[index];
         const nextLetter = index + 1 < text.length ? text[index + 1] : '';

         if (
            index + 1 < text.length &&
            valueMap.get(letter) < valueMap.get(nextLetter)
         ) {
            number += -valueMap.get(letter) + valueMap.get(nextLetter);
            index += 2;
         } else {
            number += valueMap.get(letter);
            index++;
         }
      }
      return number
   };
}
const romanToInt = new Solution().romanToInt;


console.log(new Solution().romanToInt('III') === 3)
console.log(new Solution().romanToInt('IV') === 4)
console.log(new Solution().romanToInt('V') === 5)
console.log(new Solution().romanToInt('VI') === 6)
console.log(new Solution().romanToInt('IX') === 9)
console.log(new Solution().romanToInt('X') === 10)
console.log(new Solution().romanToInt('XII') === 12)
console.log(new Solution().romanToInt('LVIII') === 58)
console.log(new Solution().romanToInt('MCMXCIV') === 1994)