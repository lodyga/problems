class Solution {
   /**
    * Time complexity: O(1)
         O(32)
    * Auxiliary space complexity: O(1)
    * Tags: bit manipulation
    * @param {number} num
    * @return {number}
    */
   hammingWeight(num) {
      let res = 0;

      while (num) {
         res += num & 1;
         num = num >> 1;
      }

      return res;
   }
}


class Solution {
   /**
    * Time complexity: O(1)
         O(32)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: bit manipulation
    * @param {number} num
    * @return {number}
    */
   hammingWeight(num) {
      let res = 0;

      while (num) {
         res += num % 2;
         num = Math.floor(num / 2);
      }

      return res;
   }
}


class Solution {
   /**
    * Time complexity: O(1)
         O(32)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: bit manipulation, bit mask
    * @param {number} num
    * @return {number}
    */
   hammingWeight(num) {
      let res = 0;
      let mask = 1;

      for (let idx = 0; idx < 32; idx++) {
         if (num & mask) {
            res++;
         }

         mask <<= 1;
      }

      return res;
   }
}


class Solution {
   /**
    * Time complexity: O(1)
         O(32)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: bit manipulation, built-in function
    * @param {number} num
    * @return {number}
    */
   hammingWeight(num) {
      return (
         num.toString(2)
            .split('')
            .filter(digit => digit === '1')
            .length
      );
   }
}


const hammingWeight = new Solution().hammingWeight;
console.log(new Solution().hammingWeight(0) === 0)
console.log(new Solution().hammingWeight(1) === 1)
console.log(new Solution().hammingWeight(2) === 1)
console.log(new Solution().hammingWeight(3) === 2)
console.log(new Solution().hammingWeight(4) === 1)
console.log(new Solution().hammingWeight(11) === 3)
console.log(new Solution().hammingWeight(128) === 1)
console.log(new Solution().hammingWeight(2147483645) === 30)
