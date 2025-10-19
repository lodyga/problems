class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: bucket sort with hash map
    * @param {string} text
    * @return {string}
    */
   frequencySort(text) {
      const letterFrequency = new Map();
      for (const letter of text) {
         letterFrequency.set(letter, (letterFrequency.get(letter) || 0) + 1)
      }
      
      const buckets = new Map();
      for (const [key, val] of letterFrequency.entries()) {
         if (!buckets.has(val))
            buckets.set(val, new Set());
         buckets.get(val).add(key)
      }
      
      const sortedText = [];
      for (let frequency = text.length; frequency > 0; frequency--) {
         if (buckets.has(frequency))
            for (const letter of buckets.get(frequency))
               sortedText.push(letter.repeat(frequency))
      }
      return sortedText.join('')
   };
}


const frequencySort = new Solution().frequencySort;
console.log(new Solution().frequencySort('tree') === 'eetr')
console.log(new Solution().frequencySort('cccaaa') === 'cccaaa')
console.log(new Solution().frequencySort('Aabb') === 'bbAa')