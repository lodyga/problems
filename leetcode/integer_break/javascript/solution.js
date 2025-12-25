class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: array
    *     A: top-down
    * @param {number} nume
    * @return {number}
    */
   integerBreak(num) {
      // [number: product] maximum product for current number
      // [0: 1] When the number is partitioned (rest = 0) it is multiplied by 1
      const memo = Array(num + 1).fill(-1);
      memo[0] = 1;

      const dfs = (num, isValid) => {
         if (memo[num] !== -1) {
            return memo[num]
         }

         let res = 0;
         for (let digit = 1; digit < num + Boolean(isValid); digit++) {
            res = Math.max(res, (digit * dfs(num - digit, true)));
         }
         memo[num] = res;
         return res
      }
      return dfs(num, false)
   };
}


const integerBreak = new Solution().integerBreak;
console.log(new Solution().integerBreak(2) === 1)
console.log(new Solution().integerBreak(3) === 2)
console.log(new Solution().integerBreak(4) === 4)
console.log(new Solution().integerBreak(5) === 6)
console.log(new Solution().integerBreak(6) === 9)
console.log(new Solution().integerBreak(7) === 12)
console.log(new Solution().integerBreak(10) === 36)
console.log(new Solution().integerBreak(24) === 6561)
