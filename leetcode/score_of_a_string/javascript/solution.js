class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: iteration
    * @param {string} text
    * @return {number}
    */
   scoreOfString(text) {
      let score = 0;
      for (let index = 0; index < text.length - 1; index++) {
         score += Math.abs(text.charCodeAt(index) - text.charCodeAt(index + 1))
      }
      return score
   };
}


const scoreOfString = new Solution().scoreOfString;
console.log(new Solution().scoreOfString('hello') === 13)
console.log(new Solution().scoreOfString('zaz') === 50)
