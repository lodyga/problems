class Solution {
   /**
    * Time complexity: O(n3)
    *     O(word count**2 * avg word length)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {string[]} words
    * @return {number}
    */
   longestStrChain(words) {
      const isPredecessor = (index1, index2) => {
         const word1 = words[index1];
         const word2 = words[index2];
         if (word1.length + 1 !== word2.length)
            return false

         let skipped = false
         index1 = 0;
         index2 = 0;
         while (index1 < word1.length) {
            if (word1[index1] !== word2[index2]) {
               if (skipped) {
                  return false
               } else {
                  skipped = true;
                  index1--;
               }
            }
            index1++;
            index2++;
         }
         return true
      }

      words.sort((a, b) => a.length - b.length);
      const cache = Array(words.length).fill(1);

      for (let left = words.length - 1; left > -1; left--) {
         for (let right = left + 1; right < words.length; right++) {
            if (isPredecessor(left, right)) {
               cache[left] = Math.max(cache[left], 1 + cache[right]);
            }
         }
      }
      return Math.max(...cache)
   };

   /**
    * Time complexity: O(n3)
    *     O(word count * avg word length**2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map
    *     A: bottom-up
    * @param {string[]} words
    * @return {number}
    */
   longestStrChain(words) {
      words.sort((a, b) => b.length - a.length);
      const cache = new Map(words.map(word => [word, 1]));

      for (const word of words) {
         for (let index = 0; index < word.length; index++) {
            const predecessor = word.slice(0, index) + word.slice(index + 1,);
            if (cache.has(predecessor)) {
               const chain_len = Math.max(cache.get(predecessor), 1 + cache.get(word));
               cache.set(predecessor, chain_len);
            }
         }
      }
      return Math.max(...cache.values())
   };
}


const longestStrChain = new Solution().longestStrChain;
console.log(new Solution().longestStrChain(['a', 'b', 'ba', 'bca', 'bda', 'bdca']) === 4)
console.log(new Solution().longestStrChain(['xbc', 'pcxbcf', 'xb', 'cxbc', 'pcxbc']) === 5)
console.log(new Solution().longestStrChain(['abcd', 'dbqca']) === 1)
console.log(new Solution().longestStrChain(['qyssedya', 'pabouk', 'mjwdrbqwp', 'vylodpmwp', 'nfyqeowa', 'pu', 'paboukc', 'qssedya', 'lopmw', 'nfyqowa', 'vlodpmw', 'mwdrqwp', 'opmw', 'qsda', 'neo', 'qyssedhyac', 'pmw', 'lodpmw', 'mjwdrqwp', 'eo', 'nfqwa', 'pabuk', 'nfyqwa', 'qssdya', 'qsdya', 'qyssedhya', 'pabu', 'nqwa', 'pabqoukc', 'pbu', 'mw', 'vlodpmwp', 'x', 'xr']) === 8)
