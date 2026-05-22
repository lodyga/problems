class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: iteration
    * @param {string} text
    * @return {int}
    */
   lengthOfLastWord(text) {
      let res = 0;
      let idx = text.length - 1;

      while (text[idx] === ' ') {
         idx -= 1;
      }

      while (idx > -1 && text[idx] !== ' ') {
         res += 1;
         idx -= 1;
      }

      return res
   }
}


const lengthOfLastWord = new Solution().lengthOfLastWord;
console.log(new Solution().lengthOfLastWord('Hello World') === 5)
console.log(new Solution().lengthOfLastWord('   fly me   to   the moon  ') === 4)
console.log(new Solution().lengthOfLastWord('luffy is still joyboy') === 6)
console.log(new Solution().lengthOfLastWord('y') === 1)
