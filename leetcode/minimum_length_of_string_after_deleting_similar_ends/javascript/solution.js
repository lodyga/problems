class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy, two pointers
    * @param {string} s
    * @return {number}
    */
   minimumLength(s) {
      let left = 0;
      let right = s.length - 1;

      while (left < right && s[left] === s[right]) {
         const char = s[left];

         while (left <= right && s[left] === char) {
            left++;
         }

         while (left <= right && s[right] === char) {
            right--;
         }
      }

      return right - left + 1
   };
}


const minimumLength = new Solution().minimumLength;
console.log(new Solution().minimumLength("a") === 1)
console.log(new Solution().minimumLength("aa") === 0)
console.log(new Solution().minimumLength("aabaaa") === 1)
console.log(new Solution().minimumLength("ca") === 2)
console.log(new Solution().minimumLength("cabaabac") === 0)
console.log(new Solution().minimumLength("aabccabba") === 3)
console.log(new Solution().minimumLength("abbbbbbbbbbbbbbbbbbba") === 0)
