class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: hash map
    *     A: iteration
    * @param {string} text
    * @return {number}
    */
   romanToInt(text) {
      let res = 0
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
         const char = text[index];
         const nextChar = index + 1 < text.length ? text[index + 1] : '';

         if (
            index + 1 < text.length &&
            valueMap.get(char) < valueMap.get(nextChar)
         ) {
            res += -valueMap.get(char) + valueMap.get(nextChar);
            index += 2;
         } else {
            res += valueMap.get(char);
            index++;
         }
      }
      return res
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
