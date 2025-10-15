class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: iteration
    * @param {string} s1
    * @param {string} s2
    * @return {boolean}
    */
   areAlmostEqual(s1, s2) {
      let isChanged = null;
      let changeIndex = 0;
      
      for (let index = 0; index < s1.length; index++) {
         if (s1[index] === s2[index])
            continue
         else if (isChanged === null) {
            isChanged = true;
            changeIndex = index;
         } else if (isChanged === true) {
            isChanged = false;
            if (
               s1[changeIndex] !== s2[index] ||
               s1[index] !== s2[changeIndex]
            )
               return false
         } else if (isChanged === false)
            return false
      }
      return (isChanged === null || isChanged === false)
   };
}


const areAlmostEqual = new Solution().areAlmostEqual;
console.log(new Solution().areAlmostEqual('bank', 'kanb') === true)
console.log(new Solution().areAlmostEqual('attack', 'defend') === false)
console.log(new Solution().areAlmostEqual('kelb', 'kelb') === true)
console.log(new Solution().areAlmostEqual('aa', 'ac') === false)