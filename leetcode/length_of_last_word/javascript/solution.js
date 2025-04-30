class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * @param {string} text
    * @return {int}
    */
   lengthOfLastWord(text) {
      return text
         .trim()
         .split(' ')
         .filter(word => word.length)
         .reverse()[0]
         .length
   };
}


console.log(new Solution().lengthOfLastWord('Hello World') === 5)
console.log(new Solution().lengthOfLastWord('   fly me   to   the moon  ') === 4)
console.log(new Solution().lengthOfLastWord('luffy is still joyboy') === 6)