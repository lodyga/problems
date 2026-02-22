class Solution {
   /**
    * Time complexity: O(n3)
    *     O(n2 * m)
    *     n: word count
    *     m: word length
    * Auxiliary space complexity: O(n)
    * Tags:
    *     build-in function
    * @param {string[]} words
    * @return {number}
    */
   countPrefixSuffixPairs(words) {
      const isPrefixAndSuffix = (word1, word2) => {
         return (
            word2.startsWith(word1) &&
            word2.endsWith(word1)
         )
      }

      let counter = 0;

      for (let right = 0; right < words.length; right++) {
         for (let left = 0; left < right; left++) {
            if (isPrefixAndSuffix(words[left], words[right])) {
               counter++;
            }
         }
      }

      return counter
   };

   /**
    * Time complexity: O(n3)
    *     O(n2 * m)
    *     n: word count
    *     m: word length
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: iteration
    * @param {string[]} words
    * @return {number}
    */
   countPrefixSuffixPairs(words) {
      let counter = 0;

      for (let right = 0; right < words.length; right++) {
         const word = words[right];

         for (let left = 0; left < right; left++) {
            const fix = words[left];

            if (
               fix == word.slice(0, fix.length) &&
               fix == word.slice(word.length - fix.length,)
            ) {
               counter++
            }
         }
      }

      return counter
   };
}


const countPrefixSuffixPairs = new Solution().countPrefixSuffixPairs;
console.log(new Solution().countPrefixSuffixPairs(['a', 'aba', 'ababa', 'aa']) === 4)
console.log(new Solution().countPrefixSuffixPairs(['pa', 'papa', 'ma', 'mama']) === 2)
console.log(new Solution().countPrefixSuffixPairs(['abab', 'ab']) === 0)
