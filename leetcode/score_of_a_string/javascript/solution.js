class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: 
    * @param {string} word
    * @return {number}
    */
   scoreOfString(word) {
      let score = 0;

      for (let index = 1; index < word.length; index++) {
         score += Math.abs(word.charCodeAt(index - 1) - word.charCodeAt(index))
      }
      return score
   };
}


console.log(new Solution().scoreOfString('hello') === 13)
console.log(new Solution().scoreOfString('zaz') === 50)