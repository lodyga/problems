class Solution {
   /**
    * Time complexity: O(n2)
    *    O(coin_length * amount)
    * Auxiliary space complexity: O(n2)
    * Tags: dp, top-down with memoization as hash map
    * @param {number} amount
    * @param {number[]} coins
    * @return {number}
    */
   change(amount, coins) {
      const memo = new Map();

      const dfs = (index, amount) => {
         if (amount === 0) {
            return 1
         } else if (
            amount < 0 ||
            index === coins.length
         ) {
            return 0
         } else if (memo.has(`${index},${amount}`)) {
            return memo.get(`${index},${amount}`)
         }

         memo.set(`${index},${amount}`, dfs(index + 1, amount))
         memo.set(
            `${index},${amount}`,
            memo.get(`${index},${amount}`) + dfs(index, amount - coins[index])
         )
         return memo.get(`${index},${amount}`)
      }

      return dfs(0, amount)
   };
}
const change = new Solution().change;


console.log(new Solution().change(10, [10]), 1)
console.log(new Solution().change(3, [2]), 0)
console.log(new Solution().change(5, [1, 2, 5]), 4)