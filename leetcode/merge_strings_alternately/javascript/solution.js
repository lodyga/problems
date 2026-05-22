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
      const res = [];
      let idx = 0;

      while (idx < Math.min(text1.length, text2.length)) {
         res.push(text1[idx]);
         res.push(text2[idx]);
         idx++;
      }

      res.push(text1.slice(idx, ));
      res.push(text2.slice(idx, ));

      return res.join('')
   }
}


const mergeAlternately = new Solution().mergeAlternately;
console.log(new Solution().mergeAlternately('abc', 'pqr') === 'apbqcr')
console.log(new Solution().mergeAlternately('ab', 'pqrs') === 'apbqrs')
console.log(new Solution().mergeAlternately('abcd', 'pq') === 'apbqcd')
