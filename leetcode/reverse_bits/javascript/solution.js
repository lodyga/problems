class Solution {
   /**
    * Time complexity: O(1)
    * Auxiliary space complexity: O(1)
    * Tags: bit manipulation
    * @param {number} n
    * @return {number}
    */
   reverseBits(n) {
      const shortBin = n.toString(2)
      const leadingZeros = '0'.repeat(32 - shortBin.length);
      return parseInt((leadingZeros + shortBin).split('').reverse().join(''), 2)
   };
}
const reverseBits = new Solution().reverseBits;


console.log(new Solution().reverseBits(43261596) === 964176192)
console.log(new Solution().reverseBits(2147483644) === 1073741822)