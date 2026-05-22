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
      let res = 0;

      for (let right = 0; right < text.length; right++) {
         const letter = text[right];
         vowelWindow += VOWELS.includes(letter);

         if (right >= k - 1) {
            res = Math.max(res, vowelWindow);
            vowelWindow -= VOWELS.includes(text[right - k + 1])
         }
      }

      return res;
   }
}


const maxVowels = new Solution().maxVowels;
console.log(new Solution().maxVowels('abciiidef', 3) === 3)
console.log(new Solution().maxVowels('aeiou', 2) === 2)
console.log(new Solution().maxVowels('leetcode', 3) === 2)
