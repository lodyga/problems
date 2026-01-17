class Solution {
   /**
    * Time complexity: O(n*sqrtn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map
    *     A: top-down
    * @param {number} num
    * @return {number}
    */
   numSquares(num) {
      const getSquares = (num) => {
         const squares = [1];
         let index = 2;
         while (squares[squares.length - 1] < num) {
            squares.push(index ** 2);
            index++;
         }
         if (squares[squares.length] > num)
            squares.pop();
         return squares.reverse()
      }

      const squares = getSquares(num);
      const memo = new Map([[num, 0]]);

      const dfs = (total) => {
         if (total > num)
            return num + 1
         else if (memo.has(total))
            return memo.get(total)

         let res = num + 1;
         for (const square of squares)
            res = Math.min(res, 1 + dfs(total + square));

         memo.set(total, res)
         return res
      }
      return dfs(0)
   };

   /**
    * Time complexity: O(n*sqrtn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {number} num
    * @return {number}
    */
   numSquares(num) {
      const getSquares = (num) => {
         const squares = [1];
         let index = 2;
         while (squares[squares.length - 1] < num) {
            squares.push(index ** 2);
            index++;
         }
         if (squares[squares.length] > num)
            squares.pop();
         return squares.reverse()
      }

      const squares = getSquares(num);
      const cache = Array(num + 1).fill(num + 1);
      cache[cache.length - 1] = 0;

      for (let index = num - 1; index > -1; index--) {
         for (const square of squares) {
            if (index + square > num)
               continue
            cache[index] = Math.min(cache[index], 1 + cache[index + square]);
         }
      }
      return cache[0]
   };
}


const numSquares = new Solution().numSquares;
console.log(new Solution().numSquares(1) === 1)
console.log(new Solution().numSquares(9) === 1)
console.log(new Solution().numSquares(16) === 1)
console.log(new Solution().numSquares(2) === 2)
console.log(new Solution().numSquares(5) === 2)
console.log(new Solution().numSquares(13) === 2)
console.log(new Solution().numSquares(12) === 3)
console.log(new Solution().numSquares(7) === 4)
console.log(new Solution().numSquares(28) === 4)
console.log(new Solution().numSquares(43) === 3)
console.log(new Solution().numSquares(204) === 3)
