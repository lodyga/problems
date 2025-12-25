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
   maxNumberOfBalloons(text) {
      const letterFrequency = new Map();

      for (const letter of text) {
         if ('balon'.includes(letter)) {
            letterFrequency.set(letter, (letterFrequency.get(letter) || 0) + 1);
         }
      }
      if (letterFrequency.size < 5)
         return 0

      let counter = text.length;
      for (const [letter, frequency] of letterFrequency.entries()) {
         if ('ol'.includes(letter)) {
            counter = Math.min(counter, frequency >> 1);
         } else {
            counter = Math.min(counter, frequency)
         }
      }
      return counter
   };
}


const maxNumberOfBalloons = new Solution().maxNumberOfBalloons;
console.log(new Solution().maxNumberOfBalloons('nlaebolko') === 1)
console.log(new Solution().maxNumberOfBalloons('loonbalxballpoon') === 2)
console.log(new Solution().maxNumberOfBalloons('leetcode') === 0)
console.log(new Solution().maxNumberOfBalloons('balon') === 0)
console.log(new Solution().maxNumberOfBalloons('lloo') === 0)
