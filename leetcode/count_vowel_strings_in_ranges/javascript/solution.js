class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: prefix sum
    * @param {string[]} words
    * @param {number[]=} queries
    * @return {number[]}
    */
   vowelStrings(words, queries) {
      const vowels = 'aeoiu';
      const areEdgesVowels = (word) => {
         return vowels.includes(word[0]) && vowels.includes(word[word.length - 1])
      }

      const prefixSum = Array(words.length + 1).fill(0);
      for (let index = 0; index < words.length; index++) {
         prefixSum[index + 1] = prefixSum[index] + areEdgesVowels(words[index])
      }

      const response = Array(queries.length);
      for (let index = 0; index < queries.length; index++) {
         const [start, stop] = queries[index];
         response[index] = prefixSum[stop + 1] - prefixSum[start]
      }
      
      return response
   };
}


const vowelStrings = new Solution().vowelStrings;
console.log(new Solution().vowelStrings(['a', 'e', 'i'], [[0, 2], [0, 1], [2, 2]]), [3, 2, 1])
console.log(new Solution().vowelStrings(['aba', 'bcb', 'ece', 'aa', 'e'], [[0, 2], [1, 4], [1, 1]]), [2, 3, 0])