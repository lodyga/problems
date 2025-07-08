class Solution {
   /**
    * Time complexity: O(n)
    *     O(min(n+m))
    * Auxiliary space complexity: O(1)
    * Tags: iteration, two pointers
    * @param {string} text1
    * @param {string} text2
    * @return {number}
    */
   appendCharacters(text1, text2) {
      let index1 = 0;
      let index2 = 0;

      while (
         index1 < text1.length &&
         index2 < text2.length
      ) {
         if (text1[index1] === text2[index2]) {
            index2++;
         }
         index1++;
      }
      return text2.length - index2
   };
}
const appendCharacters = new Solution().appendCharacters;


console.log(new Solution().appendCharacters('coaching', 'coding') === 4)
console.log(new Solution().appendCharacters('abcde', 'a') === 0)
console.log(new Solution().appendCharacters('z', 'abcde') === 5)
console.log(new Solution().appendCharacters('a', 'a') === 0)