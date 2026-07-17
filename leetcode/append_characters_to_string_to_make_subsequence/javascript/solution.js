class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: two pointers, iteration
    * @param {string} text1
    * @param {string} text2
    * @return {number}
    */
   appendCharacters(text1, text2) {
      let idx2 = 0;
      const text2Len = text2.length;

      for (const letter of text1) {
         if (idx2 === text2Len) {
            return 0;
         }
         else if (letter === text2[idx2]) {
            idx2 += 1;
         }
      }

      return text2Len - idx2;
   }
}


const appendCharacters = new Solution().appendCharacters;
console.log(new Solution().appendCharacters('coaching', 'coding') === 4)
console.log(new Solution().appendCharacters('abcde', 'a') === 0)
console.log(new Solution().appendCharacters('z', 'abcde') === 5)
console.log(new Solution().appendCharacters('a', 'a') === 0)
