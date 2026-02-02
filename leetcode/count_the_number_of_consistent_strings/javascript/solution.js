class Solution {
   /**
    * Time complexity: O(n·m)
    *     O(n·m·26)
    *     n: words length
    *     m: average word length
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: iteration
    * @param {string} allowed
    * @param {string[]} words
    * @return {number}
    */
   countConsistentStrings(allowed, words) {
      let counter = words.length;

      for (const word of words) {
         for (const letter of word) {
            if (!allowed.includes(letter)) {
               counter--;
               break
            }
         }
      }

      return counter
   };

   /**
    * Time complexity: O(n·m)
    *     O(n·m)
    *     n: words length
    *     m: average word length
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: iteration
    * @param {string} allowed
    * @param {string[]} words
    * @return {number}
    */
   countConsistentStrings(allowed, words) {
      let counter = words.length;
      const allSet = new Set(allowed);

      for (const word of words) {
         for (const letter of word) {
            if (!allSet.has(letter)) {
               counter--;
               break
            }
         }
      }

      return counter
   };

   /**
    * Time complexity: O(n·m)
    *     O(n·m)
    *     n: words length
    *     m: average word length
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: bit manipulation
    * @param {string} allowed
    * @param {string[]} words
    * @return {number}
    */
   countConsistentStrings(allowed, words) {
      const getMask = (word) => {
         let mask = 0;
         for (let index = 0; index < word.length; index++) {
            const shift = word.charCodeAt(index) - 'a'.charCodeAt(0);
            const bit = 1 << shift;
            mask |= bit;
         }
         return mask
      }

      const bitMask = getMask(allowed);
      let counter = words.length;

      for (const word of words) {
         for (let index = 0; index < word.length; index++) {
            const shift = word.charCodeAt(index) - 'a'.charCodeAt(0);
            const bit = 1 << shift;

            if ((bit & bitMask) === 0) {
               counter--;
               break
            }
         }
      }

      return counter
   };
}


const countConsistentStrings = new Solution().countConsistentStrings;
console.log(new Solution().countConsistentStrings('ab', ['ad', 'bd', 'aaab', 'baa', 'badab']) === 2)
console.log(new Solution().countConsistentStrings('abc', ['a', 'b', 'c', 'ab', 'ac', 'bc', 'abc']) === 7)
console.log(new Solution().countConsistentStrings('cad', ['cc', 'acd', 'b', 'ba', 'bac', 'bad', 'ac', 'd']) === 4)
