class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags: dp, bottom-up with tabulation as list
    * @param {number[]} coins
    * @param {number} amount
    * @return {number}
    */
   coinChange(coins, amount) {
      // min number of coins needed to get target amount (equal to the index)
      // "anmount + 1" an imposbile value stays when the last element of min_coins was not modified
      const cache = Array(amount + 1).fill(amount + 1);
      cache[0] = 0;

      for (let index = 1; index <= amount; index++) {
         for (const coin of coins) {
            if (index - coin >= 0) {
               cache[index] = Math.min(cache[index], cache[index - coin] + 1);
            }
         }
      }
      return cache[amount] !== amount + 1 ? cache[amount] : - 1
   };
}


console.log(new Solution().coinChange([5], 5) === 1)
console.log(new Solution().coinChange([1, 2], 3) === 2)
console.log(new Solution().coinChange([1, 2, 5], 11) === 3)
console.log(new Solution().coinChange([2], 3) === -1)
console.log(new Solution().coinChange([2], 1) === -1)
console.log(new Solution().coinChange([1], 0) === 0)
console.log(new Solution().coinChange([2, 5, 10, 1], 27) === 4)
console.log(new Solution().coinChange([186, 419, 83, 408], 6249) === 20)