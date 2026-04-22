class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash set, string
    *     A: sliding window
    * @param {string} text
    * @return {number}
    */
   lengthOfLongestSubstring(text) {
      let left = 0;
      const charSet = new Set();
      let res = 0;

      for (let right = 0; right < text.length; right++) {
         const char = text[right];

         while (charSet.has(char)) {
            charSet.delete(text[left]);
            left++;
         }

         charSet.add(char);
         res = Math.max(res, right - left + 1);
      }

      return res
   };
}


const lengthOfLongestSubstring = new Solution().lengthOfLongestSubstring;
console.log(new Solution().lengthOfLongestSubstring('abcabcbb') === 3)
console.log(new Solution().lengthOfLongestSubstring('bbbbb') === 1)
console.log(new Solution().lengthOfLongestSubstring('pwwkew') === 3)
console.log(new Solution().lengthOfLongestSubstring('aabaab!bb') === 3)
console.log(new Solution().lengthOfLongestSubstring('aab') === 2)
