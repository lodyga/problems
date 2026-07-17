class Solution2 {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: string
    *     A: iteration
    * @param {string} text
    * @return {number}
    */
   countGoodSubstrings(text) {
      let res = 0;

      for (let idx = 0; idx < text.length - 2; idx++) {
         const char1 = text[idx];
         const char2 = text[idx + 1];
         const char3 = text[idx + 2];

         if (
            char1 !== char2
            && char1 !== char3
            && char2 !== char3
         ) {
            res++;
         }
      }

      return res;
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: string
    *     A: hash set, iteration
    * @param {string} text
    * @return {number}
    */
   countGoodSubstrings(text) {
      let res = 0;

      for (let index = 0; index < text.length - 2; index++) {
         if (new Set(text.slice(index, index + 3)).size === 3) {
            res++;
         }
      }
      
      return res;
   }
}

const countGoodSubstrings = new Solution().countGoodSubstrings;
console.log(new Solution().countGoodSubstrings('xyzzaz') == 1)
console.log(new Solution().countGoodSubstrings('aababcabc') == 4)
console.log(new Solution().countGoodSubstrings('x') == 0)
