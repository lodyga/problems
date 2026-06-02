class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: sliding window
    * @param {string} text1
    * @param {string} text2
    * @param {number} maxCost
    * @return {number}
    */
   equalSubstring(text1, text2, maxCost) {
      let left = 0;
      let res = 0;

      for (let right = 0; right < text1.length; right++) {
         const cost = Math.abs(
            text1.charCodeAt(right) -
            text2.charCodeAt(right)
         );
         maxCost -= cost;

         while (maxCost < 0) {
            const cost = Math.abs(
               text1.charCodeAt(right) -
               text2.charCodeAt(right)
            );

            maxCost += cost;
            left++;
         }
         
         res = Math.max(res, right - left + 1);
      }

      return res;
   }
}


const equalSubstring = new Solution().equalSubstring;
console.log(new Solution().equalSubstring('abcd', 'bcdf', 3) === 3)
console.log(new Solution().equalSubstring('abcd', 'cdef', 3) === 1)
console.log(new Solution().equalSubstring('abcd', 'acde', 0) === 1)
