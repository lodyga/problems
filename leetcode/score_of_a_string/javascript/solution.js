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
      let res = 0;
      for (let idx = 0; idx < text.length - 1; idx++) {
         res += Math.abs(text.charCodeAt(idx) - text.charCodeAt(idx + 1))
      }

      return res;
   }
}


const scoreOfString = new Solution().scoreOfString;
console.log(new Solution().scoreOfString('hello') === 13)
console.log(new Solution().scoreOfString('zaz') === 50)
