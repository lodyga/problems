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
         if (text.length % subText.length)
            return false

         for (let index = 0; index < text.length; index++)
            if (text[index] !== subText[index % subText.length])
               return false
         return true
      }

      for (let nextLen = Math.min(text1.length, text2.length); nextLen > 0; nextLen--) {
         if (text1.length % nextLen || text2.length % nextLen) {
            continue
         } else if (
            isGdc(text2, text2.slice(0, nextLen)) &&
            isGdc(text1, text2.slice(0, nextLen))
         ) {
            return text2.slice(0, nextLen)
         }
      }
      return ''
   };
}


const gcdOfStrings = new Solution().gcdOfStrings;
console.log(new Solution().gcdOfStrings('AA', 'A') === 'A')
console.log(new Solution().gcdOfStrings('ABCABC', 'ABC') === 'ABC')
console.log(new Solution().gcdOfStrings('ABABAB', 'ABAB') === 'AB')
console.log(new Solution().gcdOfStrings('ABABABAB', 'ABAB') === 'ABAB')
console.log(new Solution().gcdOfStrings('LEFT', 'CODY') === '')
console.log(new Solution().gcdOfStrings('TAUXXTAUXXTAUXXTAUXXTAUXX', 'TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX') === 'TAUXX')
