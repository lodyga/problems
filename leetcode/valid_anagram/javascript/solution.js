class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1) | (lowercase English letters)
    * Algorithm: Hash Array Frequency Counter
    * @param {string} text1 
    * @param {string} text2 
    * @returns {boolean}
    */
   isAnagramUsingHashArray(text1, text2) {
      if (text1.length != text2.length) return false
      const frequencies = Array(26).fill(0);

      for (let index = 0; index < text1.length; index++) {
         frequencies[text1.charCodeAt(index) - 'a'.charCodeAt(0)]++;
         frequencies[text2.charCodeAt(index) - 'a'.charCodeAt(0)]--;
      }

      for (const frequency of frequencies) {
         if (frequency !== 0)
            return false
      }
      return true
   }

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1) | (lowercase English letters)
    * Algorithm: HashMap Frequency Counter
    * @param {string} text1 
    * @param {string} text2 
    * @returns {boolean}
    */
   isAnagramUsingHashMap(text1, text2) {
      if (text1.length != text2.length) return false
      const text1LetterCounter = this.counter(text1)
      const text2LetterCounter = this.counter(text2)

      for (const key of text1LetterCounter.keys()) {
         if (text1LetterCounter.get(key) != text2LetterCounter.get(key)) return false
      }
      return true
   }

   counter(text) {
      const letterCounter = new Map();
      for (const letter of text) {
         const frequency = (letterCounter.get(letter) || 0) + 1
         letterCounter.set(letter, frequency);
      }
      return letterCounter
   }

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Algorithm: Object Frequency Counter
    * @param {string} text1 
    * @param {string} text2 
    * @returns {boolean}
    */
   isAnagramUsingObject(text1, text2) {
      if (text1.length != text2.length) return false
      const text1LetterCounter = this.objectCounter(text1)
      const text2LetterCounter = this.objectCounter(text2)
      // const keys = { ...text1LetterCounter, ...text2LetterCounter };
      const keys = { ...text1LetterCounter };

      for (const key in keys) {
         if (text1LetterCounter[key] != text2LetterCounter[key]) return false
      }
      return true
   }

   objectCounter(text) {
      const letterCounter = {};
      for (const letter of text) {
         const frequency = (letterCounter[letter] || 0) + 1
         letterCounter[letter] = frequency;
      }
      return letterCounter
   }

   /**
    * Time complexity: O(nlog)
    * Auxiliary space complexity: O(n)
    * Algorithm: Sorting Comparison
    * @param {string} text1 
    * @param {string} text2 
    * @returns {boolean}
    */
   isAnagramUsingSorting(text1, text2) {
      if (text1.length != text2.length) return false
      const text1Sorted = text1.split('').sort().join('');
      const text2Sorted = text2.split('').sort().join('');
      return text1Sorted === text2Sorted
   }
}


console.log(new Solution().isAnagramUsingSorting("anagram", "nagaram"), true)
console.log(new Solution().isAnagramUsingSorting("rat", "car"), false)
console.log(new Solution().isAnagramUsingSorting("", ""), true)