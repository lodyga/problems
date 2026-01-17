class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash set
    *     A: sliding window
    * @param {string} text
    * @return {number}
    */
   lengthOfLongestSubstring(text) {
      let left = 0;
      const windowLetters = new Set();
      let substringLenght = 0;

      for (let right = 0; right < text.length; right++) {
         const letter = text[right];

         while (windowLetters.has(letter)) {
            const leftLetter = text[left];
            windowLetters.delete(leftLetter);
            left++;
         }
         windowLetters.add(letter);
         substringLenght = Math.max(substringLenght, right - left + 1);
         
      }
      return substringLenght
   };
}


const lengthOfLongestSubstring = new Solution().lengthOfLongestSubstring;
console.log(new Solution().lengthOfLongestSubstring('abcabcbb') === 3)
console.log(new Solution().lengthOfLongestSubstring('bbbbb') === 1)
console.log(new Solution().lengthOfLongestSubstring('pwwkew') === 3)
console.log(new Solution().lengthOfLongestSubstring('aabaab!bb') === 3)
console.log(new Solution().lengthOfLongestSubstring('aab') === 2)
