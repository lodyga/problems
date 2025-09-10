class Solution {
   /**
    * Time complexity: O(n2 * t2)
    *     n: words length
    *     t: average word length
    * Auxiliary space complexity: O(n)
    * Tags: hash set
    * @param {string[]} words
    * @return {string[]}
    */
   stringMatching(words) {
      const substringWords = []
      const wordSet = new Set(words);

      for (const pattern of wordSet) {
         for (const word of wordSet) {
            if (
               pattern === word ||
               pattern.length >= word.length
            ) continue
            else {
               if (word.includes(pattern)) {
                  substringWords.push(pattern);
                  break
               }
            }
         }
      }
      return substringWords
   };
}
const stringMatching = new Solution().stringMatching;


console.log(new Solution().stringMatching(['bb', 'cbb']), ['bb'])
console.log(new Solution().stringMatching(['bb', 'bbc']), ['bb'])
console.log(new Solution().stringMatching(['hero', 'shero']), ['hero'])
console.log(new Solution().stringMatching(['mass', 'as', 'hero', 'superhero']), ['as', 'hero'])
console.log(new Solution().stringMatching(['leetcode', 'et', 'code']), ['et', 'code'])
console.log(new Solution().stringMatching(['blue', 'green', 'bu']), [])
console.log(new Solution().stringMatching(['axicc', 'waxiccgq', 'ssvob', 'gissvobox', 'zfzcj', 'gtzfzcjyk', 'cpjj', 'mnwaxiccgqd', 'dvfoc', 'rszfzcjim', 'hxz', 'vmssvob']), ['axicc', 'waxiccgq', 'ssvob', 'zfzcj'])