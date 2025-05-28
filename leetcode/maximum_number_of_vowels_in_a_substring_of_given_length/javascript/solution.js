class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: sliding window
    * @param {string} text
    * @param {number} k
    * @return {number}
    */
   maxVowels(text, k) {
      let left = 0;
      let maxVowelCount = 0;
      let windowVovelCount = 0;
      const vovels = 'aeiou'

      for (let right = 0; right < text.length; right++) {
         const letter = text[right];
         windowVovelCount += vovels.includes(letter) ? 1 : 0;

         if (right - left + 1 === k) {
            maxVowelCount = Math.max(maxVowelCount, windowVovelCount);
            const leftLetter = text[left];
            windowVovelCount -= vovels.includes(leftLetter) ? 1 : 0;
            left++;
         }
      }
      return maxVowelCount
   };
}


console.log(new Solution().maxVowels('abciiidef', 3) === 3)
console.log(new Solution().maxVowels('aeiou', 2) === 2)
console.log(new Solution().maxVowels('leetcode', 3) === 2)