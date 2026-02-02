class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: bit manipulation, brute-force
    * @param {number} n
    * @param {number} x
    * @return {number}
    */
   minEnd(n, x) {
      let num = BigInt(x);

      for (let index = 1; index < n; index++) {
         num = num + BigInt(1);
         num |= BigInt(x);
      }
      return Number(num)
   };
}


const minEnd = new Solution().minEnd;
console.log(new Solution().minEnd(3, 4) === 6)
console.log(new Solution().minEnd(2, 7) === 15)
console.log(new Solution().minEnd(3, 5) === 13)
console.log(new Solution().minEnd(69735293, 5563569) === 142821814265)
console.log(new Solution().minEnd(42076787, 25326514) === 172363546550)
