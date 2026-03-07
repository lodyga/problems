class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: hash set
    * @param {string} text
    * @return {string[]}
    */
   findRepeatedDnaSequences(text) {
      const dnaSet = new Set();
      const repeated = new Set();

      for (let right = 9; right < text.length; right++) {
         const window = text.slice(right - 9, right + 1);

         if (dnaSet.has(window)) {
            repeated.add(window);
         } else {
            dnaSet.add(window);
         }
      }

      return Array.from(repeated)
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: hash set
    * @param {string} text
    * @return {string[]}
    */
   findRepeatedDnaSequences(text) {
      if (text.length < 10) {
         return []
      }

      const val = new Map([['A', 0], ['C', 1], ['G', 2], ['T', 3]]);
      const mask = (1 << 20) - 1  // keep last 20 bits

      let rollingHash = 0;
      const seen = new Set();
      const repeated = new Set();

      for (let index = 0; index < text.length; index++) {
         rollingHash = (rollingHash << 2 | val.get(text[index])) & mask;

         if (index >= 9) {
            if (seen.has(rollingHash)) {
               repeated.add(text.slice(index - 9, index + 1));
            } else {
               seen.add(rollingHash);
            }
         }
      }
      
      return Array.from(repeated);
   };
}


const findRepeatedDnaSequences = new Solution().findRepeatedDnaSequences;
console.log(new Solution().findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT').sort().toString() === ['AAAAACCCCC', 'CCCCCAAAAA'].sort().toString());
console.log(new Solution().findRepeatedDnaSequences('AAAAAAAAAAAAA').sort().toString() === ['AAAAAAAAAA'].sort().toString());
console.log(new Solution().findRepeatedDnaSequences('A').sort().toString() === [].sort().toString());
