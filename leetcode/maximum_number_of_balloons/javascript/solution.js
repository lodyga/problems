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
      const LETTERS = 'ablno';
      const letterFreq = new Map(Array.from(LETTERS).map(char => [char, 0]));
      let res = text.length;

      for (const letter of text) {
         if (letterFreq.has(letter)) {
            letterFreq.set(letter, letterFreq.get(letter) + 1);
         }
      }

      for (const [letter, freq] of letterFreq.entries()) {
         if ('ol'.includes(letter)) {
            res = Math.min(res, Math.floor(freq / 2));
         } else {
            res = Math.min(res, freq);
         }
      }

      return res;
   }
}


const maxNumberOfBalloons = new Solution().maxNumberOfBalloons;
console.log(new Solution().maxNumberOfBalloons('nlaebolko') === 1)
console.log(new Solution().maxNumberOfBalloons('loonbalxballpoon') === 2)
console.log(new Solution().maxNumberOfBalloons('leetcode') === 0)
console.log(new Solution().maxNumberOfBalloons('balon') === 0)
console.log(new Solution().maxNumberOfBalloons('lloo') === 0)
