class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: bit manipulation, bottom-up
    * @param {number} num
    * @return {number[]}
    */
   countBits(num) {
      const res = [0];

      while (true) {
         const resLen = res.length;
         
         for (let idx = 0; idx < resLen; idx++) {
            if (res.length === num + 1) {
               return res;
            }

            res.push(res[idx] + 1);
         }
      }
   }
}


class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(1)
    * Tags:
    *    DS: array
    *    A: bit manipulation
    * @param {number} num
    * @return {number[]}
    */
   countBits(num) {
      const countSetBits = (num) => {
         let res = 0;

         while (num) {
            res += num & 1;
            num = num >> 1;
         }

         return res;
      }

      const bitsArray = Array(num + 1).fill(0);

      for (let idx = 1; idx <= num; idx++) {
         bitsArray[idx] = countSetBits(idx);
      }

      return bitsArray;

   }
}


const countBits = new Solution().countBits;
console.log(new Solution().countBits(0).toString() === [0].toString())
console.log(new Solution().countBits(2).toString() === [0, 1, 1].toString())
console.log(new Solution().countBits(5).toString() === [0, 1, 1, 2, 1, 2].toString())
console.log(new Solution().countBits(8).toString() === [0, 1, 1, 2, 1, 2, 2, 3, 1].toString())
