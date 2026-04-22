class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array
    *     A: iteration
    * @param {string} s
    * @param {string} t
    * @return {string}
    */
   findTheDifference(s, t) {
      const sFreq = Array(26).fill(0);

      for (const char of s) {
         const idx = char.charCodeAt(0) - 'a'.charCodeAt(0);
         sFreq[idx]++;
      }

      for (const char of t) {
         const idx = char.charCodeAt(0) - 'a'.charCodeAt(0);
         sFreq[idx]--

         if (sFreq[idx] < 0)
            return char
      }

      return ''
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array
    *     A: iteration
    * @param {string} s
    * @param {string} t
    * @return {string}
    */
   findTheDifference(s, t) {
      let xor = 0;

      for (let idx = 0; idx < s.length; idx++) {
         xor ^= s.charCodeAt(idx) - 'a'.charCodeAt(0);
      }

      for (let idx = 0; idx < t.length; idx++) {
         xor ^= t.charCodeAt(idx) - 'a'.charCodeAt(0);
      }

      return String.fromCharCode(xor + 'a'.codePointAt(0))
   };
}


const findTheDifference = new Solution().findTheDifference;
console.log(new Solution().findTheDifference('abcd', 'abcde') === 'e')
console.log(new Solution().findTheDifference('', 'y') === 'y')
console.log(new Solution().findTheDifference('a', 'aa') === 'a')
