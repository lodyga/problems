class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: hash map
    *     A: greedy
    * @param {string} text
    * @param {number} k
    * @return {boolean}
    */
   canConstruct(text, k) {
      if (text.length < k)
         return false

      const letterFreq = new Map();
      for (const letter of text)
         letterFreq.set(letter, (letterFreq.get(letter) || 0) + 1);

      let oddCounter = 0;

      for (const counter of letterFreq.values()) {
         if (counter % 2) {
            oddCounter++;

            if (oddCounter > k) {
               return false
            }
         }
      }
      return true
   };
}


const canConstruct = new Solution().canConstruct;
console.log(new Solution().canConstruct('annabelle', 2) === true)
console.log(new Solution().canConstruct('leetcode', 3) === false)
console.log(new Solution().canConstruct('true', 4) === true)
console.log(new Solution().canConstruct('cr', 7) === false)
console.log(new Solution().canConstruct('aaa', 2) === true)
console.log(new Solution().canConstruct('qlkzenwmmnpkopu', 15) == true)
