class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     DS: array
    *     A: sliding window
    * @param {string} text
    * @param {number} k
    * @return {number}
    */
   characterReplacement(text, k) {
      const window = Array(26).fill(0);
      let left = 0;
      let longest = 1;
      // lazy upper bound
      let mostFrequent = 0;  

      for (let right = 0; right < text.length; right++) {
         const index = text.charCodeAt(right) - 'A'.charCodeAt(0);
         window[index] += 1;
         mostFrequent = Math.max(mostFrequent, window[index]);

         while ((right - left + 1) - mostFrequent > k) {
            const left_index = text.charCodeAt(left) - 'A'.charCodeAt(0);
            window[left_index] -= 1;
            left++;
         }
         longest = Math.max(longest, right - left + 1);
      }
      return longest
   };
}


const characterReplacement = new Solution().characterReplacement;
console.log(new Solution().characterReplacement('ABAB', 2) === 4)
console.log(new Solution().characterReplacement('AABABBA', 1) === 4)
