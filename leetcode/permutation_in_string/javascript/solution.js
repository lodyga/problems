class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
         Since word1 and word2 consist of lowercase English letters
    * Tags: sliding window as hash map
    * @param {string} word1
    * @param {string} word2
    * @return {boolean}
    */
   checkInclusion(word1, word2) {
      let left = 0;
      // sliding window
      const letterFrequency = new Map();
      const pattern = new Map();

      for (const letter of word1) {
         pattern.set(letter, (pattern.get(letter) || 0) + 1);
      }
      // `need` keeps track of how many characters in `pattern` are still needed to match frequencies in `window`
      let need = pattern.size;

      for (let right = 0; right < word2.length; right++) {
         const letter = word2[right];
         if (pattern.has(letter)) {
            letterFrequency.set(letter, (letterFrequency.get(letter) || 0) + 1);
            if (letterFrequency.get(letter) === pattern.get(letter)) {
               need--;
            }

            if (right - left + 1 === word1.length) {
               if (need === 0)
                  return true

               const leftLetter = word2[left];
               if (letterFrequency.get(leftLetter) === pattern.get(leftLetter)) {
                  need++;
               }
               letterFrequency.set(leftLetter, (letterFrequency.get(leftLetter)) - 1);
               left++;
            }
         } else {
            need = pattern.size;
            letterFrequency.clear()
            left = right + 1;
         }
      }
      return false
   };
}
const checkInclusion = new Solution().checkInclusion;


console.log(new Solution().checkInclusion('ab', 'cba'), true)
console.log(new Solution().checkInclusion('ab', 'eidbaooo'), true)
console.log(new Solution().checkInclusion('ab', 'eidboaoo'), false)
console.log(new Solution().checkInclusion('ccc', 'cbac'), false)
console.log(new Solution().checkInclusion('ab', 'a'), false)
console.log(new Solution().checkInclusion('abcdxabcde', 'abcdeabcdx'), true)
console.log(new Solution().checkInclusion('adc', 'dcda'), true)
console.log(new Solution().checkInclusion('hello', 'ooolleoooleh'), false)
console.log(new Solution().checkInclusion('mart', 'karma'), false)
console.log(new Solution().checkInclusion('abc', 'ccccbbbbaaaa'), false)