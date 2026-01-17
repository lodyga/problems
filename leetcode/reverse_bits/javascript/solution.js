class Solution {
   /**
    * Time complexity: O(1)
    *     O(32)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: bit manipulation
    * @param {number} n
    * @return {number}
    */
   reverseBits(n) {
      let res = 0
      for (let index = 0; index < 32; index++) {
         const bit = (n >> index) & 1;
         if (bit) res += bit << (31 - index) 
      }
      return res
   };
}


const reverseBits = new Solution().reverseBits;
console.log(new Solution().reverseBits(43261596) === 964176192)
console.log(new Solution().reverseBits(2147483644) === 1073741822)
