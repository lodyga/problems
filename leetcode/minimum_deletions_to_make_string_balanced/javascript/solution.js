class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy
    * @param {string} s
    * @return {number}
    */
   minimumDeletions(s) {
      let bees = 0;
      let res = 0;

      for (const letter of s) {
         if (letter == "a") {
            res = Math.min(bees, res + 1)
         } else { // letter == "b"{
            bees++;
         }
   }
        return res
   };
}


const minimumDeletions = new Solution().minimumDeletions;
console.log(new Solution().minimumDeletions("aababbab") === 2)
console.log(new Solution().minimumDeletions("bbaaaaabb") === 2)
console.log(new Solution().minimumDeletions("aabbbbaa") === 2)
