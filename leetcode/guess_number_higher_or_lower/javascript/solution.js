/** 
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * var guess = function(num) {}
 */

class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags: binary search
    * @param {number} n
    * @return {number}
    */
   guessNumber(n) {
      let left = 1;
      let right = n;

      while (left <= right) {
         const middle_number = (left + right) >> 1;
         const guessVal = this.guess(middle_number);

         if (guessVal === 0)
            return middle_number
         else if (guessVal === - 1)
            right = middle_number - 1;
         else
            left = middle_number + 1;
      }
   };

   guess(n) {
      if (n === 6)
         return 0
      else if (n > 6)
         return -1
      else
         return 1
   };
}
const guessNumber = new Solution().guessNumber;

console.log(new Solution().guessNumber(10), 6)