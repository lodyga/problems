class Solution {
   /**
    * Time complexity: O(n3)
    *     O(strs_len * m * n)
    *     strs_len: strs length
    *     m: m value
    *     n: n value
    * Auxiliary space complexity: O(n3)
    * Tags:
    *     DS: hash map
    *     A: top-down
    * @param {string[]} strs
    * @param {number} m
    * @param {number} n
    * @return {number}
    */
   findMaxForm(strs, m, n) {
      const bins = strs.map(text => [
         text.split('').filter(char => char === '0').length,
         text.split('').filter(char => char === '1').length
      ]);
      const memo = new Map();

      const dfs = (index, zeros, ones) => {
         const memoInd = `${index},${zeros},${ones}`;
         if (zeros < 0 || ones < 0) {
            return -1
         } else if (index === strs.length) {
            return 0
         } else if (memo.has(memoInd)) {
            return memo.get(memoInd)
         }

         const [z, o] = bins[index];

         const skip = dfs(index + 1, zeros, ones);
         const take = 1 + dfs(index + 1, zeros - z, ones - o);

         const res = Math.max(skip, take);
         memo.set(memoInd, res);
         return res
      }

      return dfs(0, m, n)
   };

   /**
    * Time complexity: O(n3)
    *     O(strs_len * m * n)
    *     strs_len: strs length
    *     m: m value
    *     n: n value
    * Auxiliary space complexity: O(n3)
    * Tags:
    *     DS: array
    *     A: top-down
    * @param {string[]} strs
    * @param {number} m
    * @param {number} n
    * @return {number}
    */
   findMaxForm(strs, m, n) {
      const bins = strs.map(text => [
         text.split('').filter(char => char === '0').length,
         text.split('').filter(char => char === '1').length
      ]);
      const memo = Array.from({ length: strs.length }, () =>
         Array.from({ length: m + 1 }, () => Array(n + 1).fill(-1)));

      const dfs = (index, zeros, ones) => {
         if (zeros < 0 || ones < 0) {
            return -1
         } else if (index === strs.length) {
            return 0
         } else if (memo[index][zeros][ones] !== -1) {
            return memo[index][zeros][ones]
         }

         const [z, o] = bins[index];

         const skip = dfs(index + 1, zeros, ones);
         const take = 1 + dfs(index + 1, zeros - z, ones - o);

         const res = Math.max(skip, take);
         memo[index][zeros][ones] = res;
         return res
      }

      return dfs(0, m, n)
   };

   /**
    * Time complexity: O(n3)
    *     O(strs_len * m * n)
    *     strs_len: strs length
    *     m: m value
    *     n: n value
    * Auxiliary space complexity: O(n3)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {string[]} strs
    * @param {number} m
    * @param {number} n
    * @return {number}
    */
   findMaxForm(strs, m, n) {
      const bins = strs.map(text => [
         text.split('').filter(char => char === '0').length,
         text.split('').filter(char => char === '1').length
      ]);
      const cache = Array.from({ length: strs.length + 1 }, () =>
         Array.from({ length: m + 1 }, () => Array(n + 1).fill(0)));

      for (let index = strs.length - 1; index > -1; index--) {
         for (let zeros = m; zeros > -1; zeros--) {
            for (let ones = n; ones > -1; ones--) {
               const [z, o] = bins[index];
               cache[index][zeros][ones] = cache[index + 1][zeros][ones];

               if (zeros + z <= m && ones + o <= n)
                  cache[index][zeros][ones] = Math.max(
                     cache[index][zeros][ones],
                     (1 + cache[index + 1][zeros + z][ones + o])
                  );
            }
         }
      }
      return cache[0][0][0]
   };

   /**
    * Time complexity: O(n3)
    *     O(strs_len * m * n)
    *     strs_len: strs length
    *     m: m value
    *     n: n value
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {string[]} strs
    * @param {number} m
    * @param {number} n
    * @return {number}
    */
   findMaxForm(strs, m, n) {
      const bins = strs.map(text => [
         text.split('').filter(char => char === '0').length,
         text.split('').filter(char => char === '1').length
      ]);
      let nextCache = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));

      for (let index = strs.length - 1; index > -1; index--) {
         const cache = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));
         const [z, o] = bins[index];
         
         for (let zeros = m; zeros > -1; zeros--) {
            for (let ones = n; ones > -1; ones--) {
               cache[zeros][ones] = nextCache[zeros][ones];

               if (zeros + z <= m && ones + o <= n)
                  cache[zeros][ones] = Math.max(
                     cache[zeros][ones],
                     (1 + nextCache[zeros + z][ones + o])
                  );
            }
         }
         nextCache = cache;
      }
      return nextCache[0][0]
   };
}


const findMaxForm = new Solution().findMaxForm;
console.log(new Solution().findMaxForm(['10', '0001', '111001', '1', '0'], 5, 3) === 4)
console.log(new Solution().findMaxForm(['10', '0', '1'], 1, 1) === 2)
console.log(new Solution().findMaxForm(['10', '0001', '111001', '1', '0'], 4, 3) === 3)
