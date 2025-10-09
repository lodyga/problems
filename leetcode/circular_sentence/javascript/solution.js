class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: iteration
    * @param {string} sentence
    * @return {boolean}
    */
   isCircularSentence(sentence) {
      let lastLetter = sentence[sentence.length - 1];
      let wasSpace = true;
      for (const letter of sentence) {
         if (wasSpace) {
            if (letter !== lastLetter)
               return false
            wasSpace = false;
         } else if (letter === ' ') {
            wasSpace = true;
            continue
         }
         lastLetter = letter;
      }
      return true
   };
}


const isCircularSentence = new Solution().isCircularSentence;
console.log(new Solution().isCircularSentence('leetcode exercises sound delightful') === true)
console.log(new Solution().isCircularSentence('eetcode') === true)
console.log(new Solution().isCircularSentence('Leetcode is cool') === false)
console.log(new Solution().isCircularSentence("leetcode") === false)