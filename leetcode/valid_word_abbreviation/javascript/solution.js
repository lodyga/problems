class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: two pointers, iteration
    * @param {string} word
    * @param {string} abbr
    * @return {boolean}
    */
   validWordAbbreviation(word, abbr) {
      let i1 = 0;
      let i2 = 0;

      const isDigit = (char) => {
         return char.match(/\d/)
      }

      while (
         i1 < word.length &&
         i2 < abbr.length
      ) {
         if (word[i1] === abbr[i2]) {
            i1++;
            i2++;
         } else if (
            isDigit(abbr[i2])
         ) {
            if (abbr[i2] === '0')
               return false

            let skip = 0;
            while (
               i2 < abbr.length &&
               isDigit(abbr[i2])
            ) {
               skip = 10 * skip + Number(abbr[i2]);
               i2++;
            }
            i1 += skip
         } else {
            return false
         }
      }
      return (
         i1 === word.length &&
         i2 === abbr.length
      )
   };
}


const validWordAbbreviation = new Solution().validWordAbbreviation;
console.log(new Solution().validWordAbbreviation('apple', 'a2le') === true)
console.log(new Solution().validWordAbbreviation('appl', 'a2le') === false)
console.log(new Solution().validWordAbbreviation('apple', 'a2e') === false)
console.log(new Solution().validWordAbbreviation('internationalization', 'i12iz4n') === true)
console.log(new Solution().validWordAbbreviation('substitution', 's010n') === false)
