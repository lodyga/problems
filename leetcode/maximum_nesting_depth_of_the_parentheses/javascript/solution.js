class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: iteration
    * @param {string} text
    * @return {number}
    */
   maxDepth(text) {
      let depth = 0;
      let res = 0;

      for (const chr of text) {
         if (chr === '(') {
            depth++;
            res = Math.max(res, depth);
         } 
         else if (chr === ')') {
            depth--;
         }
      }

      return res;
   }
}


const maxDepth = new Solution().maxDepth;
console.log(new Solution().maxDepth('(1+(2*3)+((8)/4))+1') === 3)
console.log(new Solution().maxDepth('(1)+((2))+(((3)))') === 3)
console.log(new Solution().maxDepth('()(())((()()))') === 3)
