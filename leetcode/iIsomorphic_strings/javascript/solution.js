class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: hash map
    *     A: iteration
    * @param {string} text1
    * @param {string} text2
    * @return {boolean}
    */
   isIsomorphic(text1, text2) {
      if (text1.length !== text2.length) {
         return false
      }

      const isIso = (text1, text2) => {
         const letterMap = new Map();
         for (let index = 0; index < text1.length; index++) {
            const letter1 = text1[index];
            const letter2 = text2[index];
   
            if (letterMap.has(letter1)) {
               if (letterMap.get(letter1) !== letter2) {
                  return false
               }
            } else {
               letterMap.set(letter1, letter2);
            }
         }
         return true
      }
      return isIso(text1, text2) && isIso(text2, text1)
   };
}


const isIsomorphic = new Solution().isIsomorphic;
console.log(new Solution().isIsomorphic('egg', 'add') === true)
console.log(new Solution().isIsomorphic('foo', 'bar') === false)
console.log(new Solution().isIsomorphic('paper', 'title') === true)
console.log(new Solution().isIsomorphic('badc', 'baba') === false)
