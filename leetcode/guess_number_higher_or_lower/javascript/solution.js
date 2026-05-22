class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: binary search
    * @param {number} n
    * @return {number}
    */
   guessNumber(n) {
      let left = 1;
      let right = n;

      while (left <= right) {
         const mid = left + ((right - left) >> 1)
         const guessd = guess(mid);

         if (guessd === 0) {
            return mid;
         } else if (guessd === - 1) {
            right = mid - 1;
         } else {
            left = mid + 1;
         }
      }
   }
}


const guessNumber = new Solution().guessNumber;
console.log(new Solution().guessNumber(10) === 6)
