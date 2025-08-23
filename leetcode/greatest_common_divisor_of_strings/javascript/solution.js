class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags: string
    * @param {string} str1
    * @param {string} str2
    * @return {string}
    */
   gcdOfStrings(str1, str2) {
      let cd = '';

      const isGdc = (text, cd) => {
         // if (text === cd.repeat(text.length / cd.length)) {
         //    return true
         // }
         // return false
         let index = 0;
         while (index < text.length) {
            if (text.slice(index, index + cd.length) !== cd) {
               return false
            }
            index += cd.length;
         }
         return true
      }

      for (let index = Math.max(str1.length, str2.length); index > 0; index--) {
         if (str1.length % index || str2.length % index) {
            continue 
         }
         cd = str1.slice(0, index);

         if (isGdc(str1, cd) && isGdc(str2, cd)) {
            return cd
         }
      }
      return ''
   };
}
const gcdOfStrings = new Solution().gcdOfStrings;


console.log(new Solution().gcdOfStrings('AA', 'A') === 'A')
console.log(new Solution().gcdOfStrings('ABCABC', 'ABC') === 'ABC')
console.log(new Solution().gcdOfStrings('ABABAB', 'ABAB') === 'AB')
console.log(new Solution().gcdOfStrings('LEFT', 'CODY') === '')
console.log(new Solution().gcdOfStrings('TAUXXTAUXXTAUXXTAUXXTAUXX', 'TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX') === 'TAUXX')