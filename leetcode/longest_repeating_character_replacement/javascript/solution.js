class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: sliding window as hash map
    * @param {string} word
    * @param {number} joker
    * @return {number}
    */
   characterReplacement(word, joker) {
      const window = new Map();
      let left = 0;
      let longest = 0;
      let mostFrequent = 0;  // lazy upper bound

      for (let right = 0; right < word.length; right++) {
         const letter = word[right];
         window.set(letter, (window.get(letter) || 0) + 1);
         mostFrequent = Math.max(mostFrequent, window.get(letter));

         while ((right - left + 1) - mostFrequent > joker) {
            const leftLetter = word[left];
            window.set(leftLetter, window.get(leftLetter) - 1);
            left++;
         }
         longest = Math.max(longest, right - left + 1);
      }
      return longest
   };
}


console.log(new Solution().characterReplacement('ABAB', 2), 4)
console.log(new Solution().characterReplacement('AABAB BA', 1), 4)