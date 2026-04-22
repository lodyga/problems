class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {number} n
    * @return {}
    */
   knightDialer(n) {
      const MOD = 10 ** 9 + 7;
      let prevCache = Array(10).fill(1);

      for (let _ = 1; _ < n; _++) {
         const cache = Array(10);
         cache[0] = (prevCache[4] + prevCache[6]) % MOD;

         // corner
         cache[1] = (prevCache[6] + prevCache[8]) % MOD;
         cache[3] = (prevCache[4] + prevCache[8]) % MOD;
         cache[7] = (prevCache[2] + prevCache[6]) % MOD;
         cache[9] = (prevCache[2] + prevCache[4]) % MOD;

         // edge
         cache[2] = (prevCache[7] + prevCache[9]) % MOD;
         cache[8] = (prevCache[1] + prevCache[3]) % MOD;

         // edge with 0
         cache[4] = (prevCache[3] + prevCache[9] + prevCache[0]) % MOD;
         cache[6] = (prevCache[1] + prevCache[7] + prevCache[0]) % MOD;

         prevCache = cache
      }

      return prevCache.reduce((sum, num) => sum + num, 0) % MOD
   };
}


const knightDialer = new Solution().knightDialer;
console.log(new Solution().knightDialer(1) === 10)
console.log(new Solution().knightDialer(2) === 20)
console.log(new Solution().knightDialer(3) === 46)
console.log(new Solution().knightDialer(3131) === 136006598)
