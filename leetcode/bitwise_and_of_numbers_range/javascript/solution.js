class Solution {
   /**
    * Time complexity: O(1)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: bit manipulation
    * @param {number} left
    * @param {number} right
    * @return {number}
    */
   rangeBitwiseAnd = function (left, right) {
      let res = 0;
      let power = 1;

      for (let index = 0; index < 32; index++) {
         const bit = (left >> index) & 1;
         power *= 2;
         
         if (bit === 0)
            continue

         const remainder = left % power;
         const diff = power - remainder;

         if (right - left < diff)
            res |= 1 << index
      }

      return res
   };
}


const rangeBitwiseAnd = new Solution().rangeBitwiseAnd;
console.log(new Solution().rangeBitwiseAnd(5, 7) === 4)
console.log(new Solution().rangeBitwiseAnd(0, 0) === 0)
console.log(new Solution().rangeBitwiseAnd(1, 2) === 0)
console.log(new Solution().rangeBitwiseAnd(416, 436) === 416)
console.log(new Solution().rangeBitwiseAnd(0, 2147483647) === 0)
console.log(new Solution().rangeBitwiseAnd(2147483646, 2147483647) === 2147483646)
