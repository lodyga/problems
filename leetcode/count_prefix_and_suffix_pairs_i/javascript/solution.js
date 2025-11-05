class Solution {
   /**
    * Time complexity: O(n3)
    *     O(n2 * m)
    *     n: word count
    *     m: word length
    * Auxiliary space complexity: O(1)
    * Tags: build-in function
    * @param {string[]} words
    * @return {number}
    */
   countPrefixSuffixPairs(words) {
      const isPrefixAndSuffix = (word1, word2) => {
         return (
            word2.startsWith(word1) &&
            word2.endsWith(word1)
            // word2.slice(0, word1.length) === word1 &&
            // word2.slice(word2.length - word1.length, word2.length) === word1
         )
      }

      let counter = 0;
      for (let i = 0; i < words.length; i++)
         for (let j = i + 1; j < words.length; j++)
            if (isPrefixAndSuffix(words[i], words[j]))
               counter += 1
      return counter
   };
}


const countPrefixSuffixPairs = new Solution().countPrefixSuffixPairs;
console.log(new Solution().countPrefixSuffixPairs(['a', 'aba', 'ababa', 'aa']) === 4)
console.log(new Solution().countPrefixSuffixPairs(['pa', 'papa', 'ma', 'mama']) === 2)
console.log(new Solution().countPrefixSuffixPairs(['abab', 'ab']) === 0)
