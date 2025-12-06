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
      let counter = 0;
      let index = text.length - 1;

      while (text[index] === ' ')
         index -= 1;

      while (index > -1) {
         const letter = text[index];
         if (letter === ' ')
            return counter
         else {
            counter += 1;
            index -= 1;
         }
      }
      return counter
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: build-in function
    * @param {string} text
    * @return {int}
    */
   lengthOfLastWord(text) {
      return text
         .trim()
         .split(' ')
         .filter(word => word.length)
         .reverse()[0]
         .length
   };
}


const lengthOfLastWord = new Solution().lengthOfLastWord;
console.log(new Solution().lengthOfLastWord('Hello World') === 5)
console.log(new Solution().lengthOfLastWord('   fly me   to   the moon  ') === 4)
console.log(new Solution().lengthOfLastWord('luffy is still joyboy') === 6)
