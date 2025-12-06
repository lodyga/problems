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
         while (
            left > -1 &&
            right < text.length &&
            text[left] === text[right]
         ) {
            conuter++;
            left--;
            right++;
         }
      }

      let conuter = 0;
      for (let index = 0; index < text.length; index++) {
         // check for odd length palindromes
         countPalindromes(index, index);
         // check for even length palindromes
         countPalindromes(index, index + 1);
      }
      return conuter;
   };
}


const countSubstrings = new Solution().countSubstrings;
console.log(new Solution().countSubstrings('abc') === 3)
console.log(new Solution().countSubstrings('aaa') === 6)
