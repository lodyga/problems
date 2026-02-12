class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: iteration
    * @param {string} text1
    * @param {string} text2
    * @return {boolean}
    */
   areAlmostEqual(text1, text2) {
      let swapPair = [];
      let isSwapped = false;

      for (let index = 0; index < text1.length; index++) {
         const c1 = text1[index];
         const c2 = text2[index];

         if (c1 === c2)
            continue

         if (isSwapped)
            return false

         if (swapPair.length) {
            if (swapPair.toString() !== [c2, c1].toString())
               return false

            swapPair = [];
            isSwapped = true;
         } else {
            swapPair = [c1, c2];
         }

      }
      return swapPair.length === 0
   };
}


const areAlmostEqual = new Solution().areAlmostEqual;
console.log(new Solution().areAlmostEqual('bank', 'kanb') === true)
console.log(new Solution().areAlmostEqual('attack', 'defend') === false)
console.log(new Solution().areAlmostEqual('kelb', 'kelb') === true)
console.log(new Solution().areAlmostEqual('aa', 'ac') === false)
