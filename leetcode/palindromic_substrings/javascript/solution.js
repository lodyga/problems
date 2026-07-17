class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: two pointers
    * @param {string} text
    * @return {number}
    */
   countSubstrings(text) {
      const countPalindromes = (left, right) => {
         let res = 0;

         while (
            left > -1
            && right < text.length
            && text[left] === text[right]
         ) {
            res++;
            left--;
            right++;
         }

         return res;
      }

      let res = 0;

      for (let idx = 0; idx < text.length; idx++) {
         // check for odd length palindromes
         res += countPalindromes(idx, idx);
         // check for even length palindromes
         res += countPalindromes(idx, idx + 1);
      }

      return res;
   }
}


const countSubstrings = new Solution().countSubstrings;
console.log(new Solution().countSubstrings('abc') === 3)
console.log(new Solution().countSubstrings('aaa') === 6)
