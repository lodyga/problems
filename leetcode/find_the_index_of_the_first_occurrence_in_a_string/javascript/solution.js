class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: iteration
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

   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: iteration
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

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: Rabin-Karp, rolling hash
    * @param {string} haystack
    * @param {string} needle
    * @return {int}
    */
   strStr(haystack, needle) {
      if (haystack.length < needle) {
         return -1
      } else if (haystack.length === needle.length) {
         return needle === haystack ? 0 : -1
      }

      const BASE = 29;
      const MOD = 1e9 + 7;
      let needleHash = 0;

      for (let index = 0; index < needle.length; index++) {
         const val = needle.charCodeAt(index) - 'a'.charCodeAt(0);
         needleHash = (needleHash * BASE + val) % MOD;
      }

      const POWER = Math.pow(BASE, needle.length - 1) % MOD;
      let substrHash = 0;
      let left = 0;

      for (let right = 0; right < haystack.length; right++) {
         const val = haystack.charCodeAt(right) - 'a'.charCodeAt(0);
         substrHash = (substrHash * BASE + val) % MOD;

         if (right < needle.length - 1) {
            continue
         } else if (substrHash == needleHash) {
            return left
         }

         const leftVal = haystack.charCodeAt(left) - 'a'.charCodeAt(0);
         substrHash = (substrHash - leftVal * POWER) % MOD;
         if (substrHash < 0)
            substrHash += MOD;
         left++;
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
console.log(new Solution().strStr('fourscoreandsevenyearsagoourfathersbroughtforthuponthiscontinentanewnation', 'ourfathersbroughtforthuponthiscontinentanewnation') === 25)
