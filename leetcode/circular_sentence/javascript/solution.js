class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: two pointers
    * @param {string} sentence
    * @return {boolean}
    */
   isCircularSentence(sentence) {
      const N = sentence.length;

      for (let index = 1; index < N - 1; index++) {
         if (
            sentence[index] === ' ' &&
            sentence[index - 1] !== sentence[index + 1]
         ) return false
      }
      return sentence[0] === sentence[N - 1];
   };
}


const isCircularSentence = new Solution().isCircularSentence;
console.log(new Solution().isCircularSentence('leetcode exercises sound delightful') === true)
console.log(new Solution().isCircularSentence('eetcode') === true)
console.log(new Solution().isCircularSentence('Leetcode is cool') === false)
console.log(new Solution().isCircularSentence('leetcode') === false)
console.log(new Solution().isCircularSentence('MuFoevIXCZzrpXeRmTssj lYSW U jM') === false)
