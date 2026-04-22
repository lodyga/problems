class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array
    *     A: sliding window
    * @param {string} s
    * @return {number}
    */
   numberOfSubstrings(s) {
      let left = 0;
      let res = 0;
      // ['a' counter, 'b' counter, 'c' counter]
      const window = [0, 0, 0];

      for (const char of s) {
         const idx = char.charCodeAt(0) - 'a'.charCodeAt(0);
         window[idx]++;

         if (!window.every(counter => counter)) {
            continue
         }

         while (left < s.length && window[s[left].charCodeAt(0) - 'a'.charCodeAt(0)] > 1) {
            window[s[left].charCodeAt(0) - 'a'.charCodeAt(0)]--
            left++;
         }

         res += left + 1;
      }

      return res
   };
}


const numberOfSubstrings = new Solution().numberOfSubstrings;
console.log(new Solution().numberOfSubstrings('abcabc') === 10)
console.log(new Solution().numberOfSubstrings('aaacb') === 3)
console.log(new Solution().numberOfSubstrings('abc') === 1)
