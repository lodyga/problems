class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: two pointers
    * @param {string} text1
    * @param {string} text2
    * @return {string}
    */
   mergeAlternately(text1, text2) {
      const text = [];

      for (let index = 0; index < Math.max(text1.length, text2.length); index++) {
         const letter1 = text1[index] || '';
         const letter2 = text2[index] ?? '';
         text.push(letter1);
         text.push(letter2);
      }
      return text.join('')
   };
}


const mergeAlternately = new Solution().mergeAlternately;
console.log(new Solution().mergeAlternately('abc', 'pqr') === 'apbqcr')
console.log(new Solution().mergeAlternately('ab', 'pqrs') === 'apbqrs')
console.log(new Solution().mergeAlternately('abcd', 'pq') === 'apbqcd')
