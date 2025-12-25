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
      const guess = (n) => {
         if (n === 6)
            return 0
         else if (n > 6)
            return -1
         else
            return 1
      };
      
      let left = 1;
      let right = n;

      while (left <= right) {
         const middle = left + ((right - left) >> 1)
         const guessd = guess(middle);

         if (guessd === 0) {
            return middle
         } else if (guessd === - 1) {
            right = middle - 1;
         } else {
            left = middle + 1;
         }
      }
   };
}


const guessNumber = new Solution().guessNumber;
console.log(new Solution().guessNumber(10) === 6)
