class Solution {
   /**
    * Time complexity: O(n3)
    *     O(word_count*avg_word_length**2)
    * Auxiliary space complexity: O(n2)
    *     O(word_count*avg_word_length)
    * Tags: dp, bottom-up with tabulation as hash map
    * @param {string[]} words
    * @return {number}
    */
   longestStrChain(words) {
      words.sort((a, b) => b.length - a.length);
      const wordChain = new Map(words.map(word => [word, 1]));
      let longestStrChainLength = 1;
      
      for (const word of words) {
         for (let index = 0; index < word.length; index++) {
            const predecessor = word.slice(0, index) + word.slice(index + 1,);
            if (wordChain.has(predecessor)) {
               wordChain.set(predecessor, Math.max(wordChain.get(predecessor), wordChain.get(word) + 1));
               longestStrChainLength = Math.max(longestStrChainLength, wordChain.get(predecessor));
            }
         }
      }
      return longestStrChainLength
   };
}
const longestStrChain = new Solution().longestStrChain;


console.log(new Solution().longestStrChain(['a', 'b', 'ba', 'bca', 'bda', 'bdca']) === 4)
console.log(new Solution().longestStrChain(['xbc', 'pcxbcf', 'xb', 'cxbc', 'pcxbc']) === 5)
console.log(new Solution().longestStrChain(['abcd', 'dbqca']) === 1)