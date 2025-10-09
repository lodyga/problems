class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: iteration
    * @param {string} ransomNote
    * @param {string} magazine
    * @return {boolean}
    */
   canConstruct(ransomNote, magazine) {
      const letters = Array(26).fill(0);
      for (const letter of magazine) 
         letters[letter.charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
      for (const letter of ransomNote) {
         const index = letter.charCodeAt(0) - 'a'.charCodeAt(0)
         if (letters[index] === 0)
            return false
         letters[index] -= 1;
      }
      return true
   };
}


const canConstruct = new Solution().canConstruct;
console.log(new Solution().canConstruct('a', 'b') === false)
console.log(new Solution().canConstruct('aa', 'ab') === false)
console.log(new Solution().canConstruct('aa', 'aab') === true)