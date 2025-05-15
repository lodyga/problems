class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: sliding window as hash set
    * @param {string} word
    * @return {number}
    */
   lengthOfLongestSubstring(word) {
      let left = 0;
      const window = new Set();
      let longestSubstring = 1;

      for (let right = 0; right < word.length; right++) {
         const letter = word[right];

         while (window.has(letter)) {
            window.delete(word[left]);
            left++;
         }

         window.add(letter);
         longestSubstring = Math.max(longestSubstring, right - left + 1);
         
      }
      return longestSubstring
   };
}


console.log(new Solution().lengthOfLongestSubstring('abcabcbb'), 3)
console.log(new Solution().lengthOfLongestSubstring('bbbbb'), 1)
console.log(new Solution().lengthOfLongestSubstring('pwwkew'), 3)
console.log(new Solution().lengthOfLongestSubstring('aabaab!bb'), 3)
console.log(new Solution().lengthOfLongestSubstring('aab'), 2)