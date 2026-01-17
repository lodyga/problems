class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: list
    *     A: bit manipulation, bottom-up
    * @param {number} num
    * @return {number[]}
    */
   countBits(num) {
      const res = [0];

      while (true) {
         const res_length = res.length;
         for (let index = 0; index < res_length; index++) {
            if (res.length == num + 1)
               return res
            res.push(res[index] + 1);
         }
      }
   };

   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(1)
    * Tags:
    *    A: bit manipulation
    * @param {number} num
    * @return {number[]}
    */
   countBits(num) {
      const bitsArray = Array(num + 1).fill(0);

      for (let index = 1; index <= num; index++) {
         bitsArray[index] = countSetBits(index);
      }

      return bitsArray

      function countSetBits(num) {
         let setBitCounter = 0;

         while (num) {
            setBitCounter += num & 1;
            num = num >> 1;
         }
         return setBitCounter
      }
   };
}


const countBits = new Solution().countBits;
console.log(new Solution().countBits(0).toString() === [0].toString())
console.log(new Solution().countBits(2).toString() === [0, 1, 1].toString())
console.log(new Solution().countBits(5).toString() === [0, 1, 1, 2, 1, 2].toString())
console.log(new Solution().countBits(8).toString() === [0, 1, 1, 2, 1, 2, 2, 3, 1].toString())
