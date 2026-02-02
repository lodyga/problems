class Solution {
   /**
    * Time complexity: O(n4)
    *     O(n2 * t2)
    *     n: word count
    *     t: average word length
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: iteration
    * @param {string[]} words
    * @return {string[]}
    */
   stringMatching(words) {
      const res = [];

      for (const pattern of words) {
         for (const word of words) {
            if (
               pattern.length < word.length &&
               word.includes(pattern)
            ) {
               res.push(pattern);
               break
            }
         }
      }
      return res
   };

   /**
    * Time complexity: O(n2 * t)
    *     n: words length
    *     t: average word length
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: Rabin-Karp, rolling hash, sliding window
    * @param {string[]} words
    * @return {string[]}
    */
   stringMatching(words) {
      const isSubstring = (word, text) => {
         if (text.length <= word.length)
            return false

         const BASE = 29;
         const MOD = 10 ** 9 + 7  // Large prime to avoid overflow.
         let wordHash = 0;

         for (let index = 0; index < word.length; index++) {
            const letterVal = word.charCodeAt(index) - 'a'.charCodeAt(0);
            wordHash = (wordHash * BASE + letterVal) % MOD
         }

         //const POWER = BASE ** (word.length - 1);
         let POWER = 1
         for (let index = 1; index < word.length; index++)
            POWER = (POWER * BASE) % MOD;
         let subHash = 0;
         let left = 0;

         for (let right = 0; right < text.length; right++) {
            const letter = text[right];
            const letterVal = text.charCodeAt(right) - 'a'.charCodeAt(0);
            subHash = (subHash * BASE + letterVal) % MOD;

            if (right < word.length - 1)
               continue

            if (subHash === wordHash)
               return true

            const leftLetter = text[left];
            const leftLetterVal = leftLetter.charCodeAt(0) - 'a'.charCodeAt(0);
            subHash -= leftLetterVal * POWER;
            if (subHash < 0)
               subHash += MOD;
            left += 1

         }
         return false
      }

      const res = [];
      for (const substr of words) {
         for (const word of words) {
            if (isSubstring(substr, word)) {
               res.push(substr);
               break
            }
         }
      }

      return res
   };
}


const stringMatching = new Solution().stringMatching;
console.log(new Solution().stringMatching(['bb', 'cbb']).sort().toString() === ['bb'].sort().toString())
console.log(new Solution().stringMatching(['bb', 'bbc']).sort().toString() === ['bb'].sort().toString())
console.log(new Solution().stringMatching(['hero', 'shero']).sort().toString() === ['hero'].sort().toString())
console.log(new Solution().stringMatching(['mass', 'as', 'hero', 'superhero']).sort().toString() === ['as', 'hero'].sort().toString())
console.log(new Solution().stringMatching(['leetcode', 'et', 'code']).sort().toString() === ['et', 'code'].sort().toString())
console.log(new Solution().stringMatching(['blue', 'green', 'bu']).sort().toString() === [].sort().toString())
console.log(new Solution().stringMatching(['axicc', 'waxiccgq', 'ssvob', 'gissvobox', 'zfzcj', 'gtzfzcjyk', 'cpjj', 'mnwaxiccgqd', 'dvfoc', 'rszfzcjim', 'hxz', 'vmssvob']).sort().toString() === ['axicc', 'waxiccgq', 'ssvob', 'zfzcj'].sort().toString())
