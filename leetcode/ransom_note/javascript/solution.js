class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array
    *     A: iteration
    * @param {string} ransomNote
    * @param {string} magazine
    * @return {boolean}
    */
   canConstruct(ransomNote, magazine) {
      const letters = Array(26).fill(0);
      
      for (let index = 0; index < magazine.length; index++) {
         const letterInd = magazine.charCodeAt(index) - 'a'.charCodeAt(0);
         letters[letterInd] += 1;
      }
      
      for (let index = 0; index < ransomNote.length; index++) {
         const letterInd = ransomNote.charCodeAt(index) - 'a'.charCodeAt(0);
         
         if (letters[letterInd] === 0)
            return false
         
         letters[letterInd] -= 1;
      }
      return true
   };
}


const canConstruct = new Solution().canConstruct;
console.log(new Solution().canConstruct('a', 'b') === false)
console.log(new Solution().canConstruct('aa', 'ab') === false)
console.log(new Solution().canConstruct('aa', 'aab') === true)
