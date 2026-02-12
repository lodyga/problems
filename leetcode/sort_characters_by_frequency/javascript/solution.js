class Solution {
   /**
    * Time complexity: O(n)
    *     O(62): uppercase + lowercase + digits.
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map
    *     A: sorting, counting sort
    * @param {string} text
    * @return {string}
    */
   frequencySort(text) {
      const letterFreq = new Map();
      const buckets = new Map();
      const res = [];

      for (const letter of text) {
         letterFreq.set(letter, (letterFreq.get(letter) || 0) + 1);
      }


      for (const [letter, freq] of letterFreq.entries()) {
         if (!buckets.has(freq)) {
            buckets.set(freq, []);
         }
         buckets.get(freq).push(letter);
      }

      const freqs = [...buckets.keys()].sort((a, b) => b - a);

      for (const freq of freqs) {
         for (const letter of buckets.get(freq)) {
            res.push(letter.repeat(freq));
         }
      }
      return res.join('')
   };
   
   /**
    * Time complexity: O(n)
    *     O(62): uppercase + lowercase + digits.
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map
    *     A: sorting, bucket sort
    * @param {string} text
    * @return {string}
    */
   frequencySort(text) {
      const letterFreq = new Map();
      const buckets = new Map();
      const res = [];

      for (const letter of text) {
         letterFreq.set(letter, (letterFreq.get(letter) || 0) + 1);
      }


      for (const [letter, freq] of letterFreq.entries()) {
         if (!buckets.has(freq)) {
            buckets.set(freq, []);
         }
         buckets.get(freq).push(letter);
      }

      for (let freq = text.length; freq > 0; freq--) {
         if (buckets.has(freq)) {
            for (const letter of buckets.get(freq)) {
               res.push(letter.repeat(freq));
            }
         }
      }
      return res.join('')
   };
}


const frequencySort = new Solution().frequencySort;
console.log(new Solution().frequencySort('tree') === 'eetr')
console.log(new Solution().frequencySort('cccaaa') === 'cccaaa')
console.log(new Solution().frequencySort('Aabb') === 'bbAa')
