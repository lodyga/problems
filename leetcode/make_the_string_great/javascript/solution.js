class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * @param {string} word
    * @return {string}
    */
   makeGood(word) {
      const letterStack = [];

      for (const letter of word) {
         if (
            letterStack.length &&
            letter !== letterStack[letterStack.length - 1] &&
            letter.toLowerCase() === letterStack[letterStack.length - 1].toLowerCase()
         ) {
            letterStack.pop();
         } else {
            letterStack.push(letter);
         }

      }
      return letterStack.join('');
   };
}
const makeGood = new Solution().makeGood;


console.log(new Solution().makeGood('s') === 's')
console.log(new Solution().makeGood('Mc') === 'Mc')
console.log(new Solution().makeGood('Pp') === '')
console.log(new Solution().makeGood('abBAcC') === '')
console.log(new Solution().makeGood('leEeetcode') === 'leetcode')