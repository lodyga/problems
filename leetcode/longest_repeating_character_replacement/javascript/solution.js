class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array, string
    *     A: sliding window
    * @param {string} text
    * @param {number} k
    * @return {number}
    */
   characterReplacement(text, k) {
      const window = Array(26).fill(0);
      let left = 0;
      let res = 1;
      // lazy upper bound
      let mostFreq = 0;

      for (let right = 0; right < text.length; right++) {
         const idx = text.charCodeAt(right) - 'A'.charCodeAt(0);
         window[idx] += 1;
         mostFreq = Math.max(mostFreq, window[idx]);

         while ((right - left + 1) - mostFreq > k) {
            const left_idx = text.charCodeAt(left) - 'A'.charCodeAt(0);
            window[left_idx] -= 1;
            left++;
         }

         res = Math.max(res, right - left + 1);
      }

      return res
   };
}


const characterReplacement = new Solution().characterReplacement;
console.log(new Solution().characterReplacement('ABAB', 2) === 4)
console.log(new Solution().characterReplacement('AABABBA', 1) === 4)
console.log(new Solution().characterReplacement('BAAAB', 2) === 5)
