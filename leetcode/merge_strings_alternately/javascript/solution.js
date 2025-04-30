class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * @param {string} word1
    * @param {string} word2
    * @return {string}
    */
   mergeAlternately(word1, word2) {
      const letterList = [];
      let index1 = 0;
      let index2 = 0;

      while (
         index1 < word1.length &&
         index2 < word2.length
      ) {
         letterList.push(word1[index1]);
         index1++;
         letterList.push(word2[index2]);
         index2++;
      }
      while (index1 < word1.length) {
         letterList.push(word1[index1]);
         index1++;
      }
      while (index2 < word2.length) {
         letterList.push(word2[index2]);
         index2++;
      }
      return letterList.join('')
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * @param {string} word1
    * @param {string} word2
    * @return {string}
    */
   mergeAlternately(word1, word2) {
      let mergedStr = '';

      for (let index = 0; index < Math.max(word1.length, word2.length); index++) {
         mergedStr += word1[index] || '';
         mergedStr += word2[index] ?? '';
      }
      return mergedStr
   };
}


console.log(new Solution().mergeAlternately('abc', 'pqr') === 'apbqcr')
console.log(new Solution().mergeAlternately('ab', 'pqrs') === 'apbqrs')
console.log(new Solution().mergeAlternately('abcd', 'pq') === 'apbqcd')