class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     DS: string
    *     A: sliding window
    * @param {string} text
    * @param {number} k
    * @return {number}
    */
   maxVowels(text, k) {
      const VOWELS = 'aeiou';
      let vowelWindow = 0;
      let left = 0;
      let vowelCounter = 0;

      for (let right = 0; right < text.length; right++) {
         const letter = text[right];
         vowelWindow += VOWELS.includes(letter);

         if (right + 1 < k) {
            continue
         }
         vowelCounter = Math.max(vowelCounter, vowelWindow);
         const leftLetter = text[left];
         vowelWindow -= VOWELS.includes(leftLetter)
         left++;
      }
      return vowelCounter
   };
}


const maxVowels = new Solution().maxVowels;
console.log(new Solution().maxVowels('abciiidef', 3) === 3)
console.log(new Solution().maxVowels('aeiou', 2) === 2)
console.log(new Solution().maxVowels('leetcode', 3) === 2)
