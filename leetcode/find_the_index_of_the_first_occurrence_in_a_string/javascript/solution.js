class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: Rabin-Karp
    * @param {string} haystack
    * @param {string} needle
    * @return {int}
    */
   strStr(haystack, needle) {
      if (haystack.length < needle)
         return -1

      const BASE = 29;
      const MOD = 1e9 + 7;

      const getValue = (letter) => {
         return letter.charCodeAt(0) - 'a'.charCodeAt(0)
      }

      const getHash = (text) => {
         let value = 0;
         let power = 1;
         for (let index = 0; index < text.length; index++) {
            value = (value * BASE + getValue(text[index])) % MOD;
         }
         return value
      }

      const needleHash = getHash(needle);
      let haystackHash = getHash(haystack.slice(0, needle.length));
      const power = Math.pow(BASE, needle.length - 1) % MOD

      for (let left = 0; left < haystack.length - needle.length + 1; left++) {
         if (needleHash === haystackHash) {
            return left
         }
         else if (left < haystack.length - needle.length) {
            const right = needle.length + left;
            haystackHash -= getValue(haystack[left]) * power;
            if (haystackHash < 0) haystackHash += MOD;
            haystackHash = (haystackHash * BASE + getValue(haystack[right])) % MOD;
         }
      }
      return -1
   };
}


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(1)
    * Tags: iteration
    * @param {string} haystack
    * @param {string} needle
    * @return {int}
    */
   strStr(haystack, needle) {
      if (haystack.length < needle)
         return -1

      const compare = (start) => {
         for (let index = 0; index < needle.length; index++) {
            if (haystack[[start + index]] !== needle[index])
               return false
         }
         return true
      };

      for (let index = 0; index < haystack.length - needle.length + 1; index++) {
         if (compare(index))
            return index
      }
      return -1
   };
}


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags: iteration
    * @param {string} haystack
    * @param {string} needle
    * @return {int}
    */
   strStr(haystack, needle) {
      if (haystack.length < needle)
         return -1

      for (let index = 0; index < haystack.length - needle.length + 1; index++) {
         if (needle === haystack.slice(index, index + needle.length))
            return index
      }
      return -1
   };
}


const strStr = new Solution().strStr;
console.log(new Solution().strStr('ab', 'a') === 0)
console.log(new Solution().strStr('ab', 'b') === 1)
console.log(new Solution().strStr('abc', 'c') === 2)
console.log(new Solution().strStr('aaa', 'aaaa') === -1)
console.log(new Solution().strStr('sadbutsad', 'sad') === 0)
console.log(new Solution().strStr('leetcode', 'leeto') === -1)
console.log(new Solution().strStr('hello', 'll') === 2)
console.log(new Solution().strStr('ababcaababcaabc', 'ababcaabc') === 6)
console.log(new Solution().strStr('baabbaaaaaaabbaaaaabbabbababaabbabbbbbabbabbbbbbabababaabbbbbaaabbbbabaababababbbaabbbbaaabbaababbbaabaabbabbaaaabababaaabbabbababbabbaaabbbbabbbbabbabbaabbbaa', 'bbaaaababa') === 107)