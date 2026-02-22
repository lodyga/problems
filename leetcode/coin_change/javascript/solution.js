import { Queue } from "@datastructures-js/queue";

class Solution {
   /**
    * Time complexity: O(n2)
    *     O(c*a)
    *     c: coin denominations
    *     a: ammonut size
    * Auxiliary space complexity: O(n)
    *     O(amount)
    * Tags:
    *     DS: array
    *     A: top-down
    * @param {number[]} coins
    * @param {number} amount
    * @return {number}
    */
   coinChange(coins, amount) {
      coins.sort((a, b) => b - a);
      // [amount left: min coins to get target amount left]
      const memo = Array(amount + 1).fill(-1);
      memo[amount] = 0;

      const dfs = (total) => {
         if (total > amount) {
            return amount + 1
         }
         else if (memo[total] !== -1) {
            return memo[total]
         }

         let coinCounter = amount + 1;
         for (const coin of coins) {
            coinCounter = Math.min(coinCounter, 1 + dfs(total + coin));
         }
         memo[total] = coinCounter;
         return coinCounter
      }
      const res = dfs(0);
      return res !== amount + 1 ? res : -1
   };

   /**
    * Time complexity: O(n2)
    *     O(c*a)
    *     c: coin denominations
    *     a: ammonut size
    * Auxiliary space complexity: O(n)
    *     O(amount)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {number[]} coins
    * @param {number} amount
    * @return {number}
    */
   coinChange(coins, amount) {
      // Min number of coins needed to get target amount (equal to the index).
      const cache = Array(amount + 1).fill(amount + 1);
      // No coins needed to get to 0 amount;
      cache[0] = 0;

      for (let index = 1; index <= amount; index++) {
         for (const coin of coins) {
            if (coin > index) {
               continue
            }
            cache[index] = Math.min(cache[index], 1 + cache[index - coin]);
         }
      }
      return cache[amount] !== amount + 1 ? cache[amount] : - 1
   };

   /**
    * Time complexity: O(n2)
    *     O(c*a)
    *     c: coin denominations
    *     a: ammonut size
    * Auxiliary space complexity: O(n)
    *     O(amount)
    * Tags:
    *     DS: queue
    *     A: BFS, iteration
    * @param {number[]} coins
    * @param {number} amount
    * @return {number}
    */
   coinChange(coins, amount) {
      if (amount === 0)
         return 0

      const bfs = (node) => {
         const queue = new Queue([node]);
         let level = 0;
         const visited = Array(amount + 1).fill(false);
         visited[0] = true;

         while (!queue.isEmpty()) {
            level++;
            const queueSize = queue.size();
            for (let index = 0; index < queueSize; index++) {
               node = queue.pop();

               for (const coin of coins) {
                  const total = node + coin;

                  if (total === amount) {
                     return level
                  }
                  else if (total > amount) {
                     continue
                  }
                  else if (visited[total]) {
                     continue
                  }
                  queue.push(total);
                  visited[total] = true;
               }
            }
         }
         return -1
      }
      return bfs(0)
   };
}


const coinChange = new Solution().coinChange;
console.log(new Solution().coinChange([5], 5) === 1)
console.log(new Solution().coinChange([1, 2], 3) === 2)
console.log(new Solution().coinChange([1, 2, 5], 11) === 3)
console.log(new Solution().coinChange([2], 3) === -1)
console.log(new Solution().coinChange([2], 1) === -1)
console.log(new Solution().coinChange([1], 0) === 0)
console.log(new Solution().coinChange([2, 5, 10, 1], 27) === 4)
console.log(new Solution().coinChange([186, 419, 83, 408], 6249) === 20)
