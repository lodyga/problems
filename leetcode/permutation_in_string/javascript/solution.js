class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
          DS: array
    *     A: sliding window 
    * @param {string} word
    * @param {string} text
    * @return {boolean}
    */
   checkInclusion(word, text) {
      const window = Array(26).fill(0);
      let left = 0;
      let idx = 0;

      for (const letter of word) {
         idx = letter.charCodeAt(0) - 'a'.charCodeAt(0);
         window[idx]--;
      }

      for (let right = 0; right < text.length; right++) {
         const letter = text[right];
         idx = letter.charCodeAt(0) - 'a'.charCodeAt(0);
         window[idx]++;

         if ((right - left + 1) < word.length) {
            continue
         } else if (!window.some(val => val)) {
            return true
         }

         const leftLetter = text[left];
         idx = leftLetter.charCodeAt(0) - 'a'.charCodeAt(0);
         window[idx]--;
         left++;
      }

      return false
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
          DS: hash map
    *     A: sliding window 
    * @param {string} word
    * @param {string} text
    * @return {boolean}
    */
   checkInclusion(word, text) {
      const pattern = new Map();
      let left = 0;

      for (const letter of word) {
         pattern.set(letter, (pattern.get(letter) || 0) - 1);
      }

      for (let right = 0; right < text.length; right++) {
         const letter = text[right];
         pattern.set(letter, (pattern.get(letter) || 0) + 1);

         if (pattern.get(letter) === 0) {
            pattern.delete(letter);
         }

         if (right + 1 < word.length) {
            continue
         }

         else if (pattern.size === 0) {
            return true
         }

         const leftLetter = text[left];
         pattern.set(leftLetter, (pattern.get(leftLetter) || 0) - 1);
         if (pattern.get(leftLetter) === 0) {
            pattern.delete(leftLetter);
         }
         left++;
      }

      return false
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
          DS: hash map
    *     A: sliding window 
    * @param {string} word
    * @param {string} text
    * @return {boolean}
    */
   checkInclusion(word, text) {
      let left = 0;
      // sliding window
      const letterFreq = new Map();
      const pattern = new Map();

      for (const letter of word) {
         pattern.set(letter, (pattern.get(letter) || 0) + 1);
      }
      // `need` keeps track of how many characters in `pattern` are still needed to match frequencies in `window`
      let need = pattern.size;

      for (let right = 0; right < text.length; right++) {
         const letter = text[right];
         if (pattern.has(letter)) {
            letterFreq.set(letter, (letterFreq.get(letter) || 0) + 1);
            if (letterFreq.get(letter) === pattern.get(letter)) {
               need--;
            }

            if (right - left + 1 === word.length) {
               if (need === 0)
                  return true

               const leftLetter = text[left];
               if (letterFreq.get(leftLetter) === pattern.get(leftLetter)) {
                  need++;
               }
               letterFreq.set(leftLetter, (letterFreq.get(leftLetter)) - 1);
               left++;
            }
         } else {
            need = pattern.size;
            letterFreq.clear()
            left = right + 1;
         }
      }
      return false
   };
}


const checkInclusion = new Solution().checkInclusion;
console.log(new Solution().checkInclusion('ab', 'cba') === true)
console.log(new Solution().checkInclusion('ab', 'eidbaooo') === true)
console.log(new Solution().checkInclusion('ab', 'eidboaoo') === false)
console.log(new Solution().checkInclusion('ccc', 'cbac') === false)
console.log(new Solution().checkInclusion('ab', 'a') === false)
console.log(new Solution().checkInclusion('abcdxabcde', 'abcdeabcdx') === true)
console.log(new Solution().checkInclusion('adc', 'dcda') === true)
console.log(new Solution().checkInclusion('hello', 'ooolleoooleh') === false)
console.log(new Solution().checkInclusion('mart', 'karma') === false)
console.log(new Solution().checkInclusion('abc', 'ccccbbbbaaaa') === false)
