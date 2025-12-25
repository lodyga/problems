class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     A: binary search
    * @param {number} coins
    * @return {number}
    */
   arrangeCoins(coins) {
      let left = 1;
      let right = coins;

      while (left <= right) {
         const middle = left + ((right - left) >> 1)
         const coinCount = parseInt((1 + middle) * middle / 2);

         if (coins === coinCount) {
            return middle
         } else if (coinCount > coins) {
            right = middle - 1;
         } else {
            left = middle + 1;
         }
      }
      return right
   };
}


const arrangeCoins = new Solution().arrangeCoins;
console.log(new Solution().arrangeCoins(1) === 1)
console.log(new Solution().arrangeCoins(2) === 1)
console.log(new Solution().arrangeCoins(3) === 2)
console.log(new Solution().arrangeCoins(4) === 2)
console.log(new Solution().arrangeCoins(5) === 2)
console.log(new Solution().arrangeCoins(6) === 3)
console.log(new Solution().arrangeCoins(8) === 3)
console.log(new Solution().arrangeCoins(1804289383) === 60070)
