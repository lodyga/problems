class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: string
    *     A: iteration
    * @param {string} text1
    * @param {string} text2
    * @return {string}
    */
   gcdOfStrings(text1, text2) {

      const isGdc = (text, subText) => {
         if (text.length % subText.length) {
            return false;
         }

         for (let idx = 0; idx < text.length; idx++)
            if (text[idx] !== subText[idx % subText.length]) {
               return false;
            }

         return true;
      };

      const minLen = Math.min(text1.length, text2.length);

      for (let currLen = minLen; currLen > 0; currLen--) {
         if (text1.length % currLen || text2.length % currLen) {
            continue;
         } else if (
            isGdc(text2, text2.slice(0, currLen))
            && isGdc(text1, text2.slice(0, currLen))
         ) {
            return text2.slice(0, currLen);
         }
      }

      return '';
   }
}


const gcdOfStrings = new Solution().gcdOfStrings;
console.log(new Solution().gcdOfStrings('AA', 'A') === 'A')
console.log(new Solution().gcdOfStrings('ABCABC', 'ABC') === 'ABC')
console.log(new Solution().gcdOfStrings('ABABAB', 'ABAB') === 'AB')
console.log(new Solution().gcdOfStrings('ABABABAB', 'ABAB') === 'ABAB')
console.log(new Solution().gcdOfStrings('LEFT', 'CODY') === '')
console.log(new Solution().gcdOfStrings('TAUXXTAUXXTAUXXTAUXXTAUXX', 'TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX') === 'TAUXX')
