class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: hash map
    * @param {string} text
    * @return {number}
    */
   maxNumberOfBalloons(text) {
      const letterFrequency = new Map();
      let balloonCount = text.length;
      const letters = 'balon';

      for (const letter of text) {
         if (letters.includes(letter)) {
            letterFrequency.set(letter, (letterFrequency.get(letter) || 0) + 1);
         }
      }

      for (const letter of letters) {
         if (!letterFrequency.has(letter))
            return 0
      }

      for (const [key, val] of letterFrequency.entries()) {
         if ('ol'.includes(key)) {
            balloonCount = Math.min(balloonCount, val / 2 | 0);
         } else {
            balloonCount = Math.min(balloonCount, val)
         }
      }
      return balloonCount
   };
}
const maxNumberOfBalloons = new Solution().maxNumberOfBalloons;


console.log(new Solution().maxNumberOfBalloons('nlaebolko'), 1)
console.log(new Solution().maxNumberOfBalloons('loonbalxballpoon'), 2)
console.log(new Solution().maxNumberOfBalloons('leetcode'), 0)
console.log(new Solution().maxNumberOfBalloons('balon'), 0)
console.log(new Solution().maxNumberOfBalloons('lloo'), 0)