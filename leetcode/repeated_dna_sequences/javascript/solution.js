class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: hash set
    * @param {string} text
    * @return {string[]}
    */
   findRepeatedDnaSequences(text) {
      const dnaSet = new Set();
      const dupliactes = new Set();

      for (let right = 9; right < text.length; right++) {
         const window = text.slice(right - 9, right + 1);
         if (dnaSet.has(window))
            dupliactes.add(window);
         else
            dnaSet.add(window)
      }
      return Array.from(dupliactes)
   };
}


const findRepeatedDnaSequences = new Solution().findRepeatedDnaSequences;
console.log(new Solution().findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'), ['AAAAACCCCC', 'CCCCCAAAAA']);
console.log(new Solution().findRepeatedDnaSequences('AAAAAAAAAAAAA'), ['AAAAAAAAAA']);
console.log(new Solution().findRepeatedDnaSequences('A'), []);
