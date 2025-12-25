class Solution {
   /**
    * Time complexity: O(n+m)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *    A: two pointers
    * @param {string[]} words1
    * @param {string[]} words2
    * @return {boolean}
    */
   arrayStringsAreEqual(words1, words2) {
      let r1 = 0;
      let c1 = 0;
      let r2 = 0;
      let c2 = 0;

      while (
         r1 < words1.length &&
         r2 < words2.length
      ) {
         const letter1 = words1[r1][c1];
         const letter2 = words2[r2][c2];

         if (letter1 !== letter2) {
            return false
         }
         c1++;
         if (c1 === words1[r1].length) {
            c1 = 0;
            r1++;
         }
         c2++;
         if (c2 === words2[r2].length) {
            c2 = 0;
            r2++;
         }
      }
      return (
         (r1 === words1.length && c1 === 0) &&
         (r2 === words2.length && c2 === 0)
      )
   };

   /**
    * Time complexity: O(m+n)
    * Auxiliary space complexity: O(m+n)
    * Tags: 
    *    A: build-in function
    * @param {string[]} words1
    * @param {string[]} words2
    * @return {boolean}
    */
   arrayStringsAreEqual(words1, words2) {
      return words1.join('') === words2.join('')
   };
}


const arrayStringsAreEqual = new Solution().arrayStringsAreEqual;
console.log(new Solution().arrayStringsAreEqual(['ab', 'c'], ['a', 'bc']) === true)
console.log(new Solution().arrayStringsAreEqual(['a', 'cb'], ['ab', 'c']) === false)
console.log(new Solution().arrayStringsAreEqual(['abc', 'd', 'defg'], ['abcddefg']) === true)
console.log(new Solution().arrayStringsAreEqual(['abc', 'd', 'defg'], ['abcddef']) === false)
