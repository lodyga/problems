class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     A: binary search, sorting
    * @param {number[]} nums
    * @param {number} target
    * @return {number}
    */
   numSubseq(nums, target) {
      const MOD = 10 ** 9 + 7
      let counter = 0;
      nums.sort((a, b) => a - b);

      const getPowerOfTwo = [1];
      for (let index = 1; index < nums.length; index++) {
         getPowerOfTwo[index] = getPowerOfTwo[index - 1] * 2 % MOD;
      }

      // const PowerOfTwo = new Map([[0, 1]])
      // const getPowerOfTwo = (index) => {
      //    if (PowerOfTwo.has(index)) {
      //       return PowerOfTwo.get(index)
      //    }
      //    const power = 2 * getPowerOfTwo(index - 1) % MOD;
      //    PowerOfTwo[index] = power;
      //    return power
      // }


      for (let index = 0; index < nums.length; index++) {
         const num = nums[index];
         if (nums[index] * 2 > target)
            break

         // Default value for maxLeft must be index in case of
         // maxLeft = middle won't trigger
         let maxLeft = index;
         let left = index + 1;
         let right = nums.length - 1;

         while (left <= right) {
            const middle = (left + right) >> 1;
            const middleNum = nums[middle];

            if (num + middleNum > target) {
               right = middle - 1;
            } else {
               maxLeft = middle;
               left = middle + 1;
            }
         }
         // counter = (counter + getPowerOfTwo(maxLeft - index)) % MOD;
         counter = (counter + getPowerOfTwo[maxLeft - index]) % MOD;
      }
      return counter
   };

   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: two pointers
    * @param {number[]} nums
    * @param {number} target
    * @return {number}
    */
   numSubseq(nums, target) {
      nums.sort((a, b) => a - b);
      let right = nums.length - 1;
      let subsequenceCounter = 0;
      const mod = 10 ** 9 + 7;

      for (let left = 0; left < nums.length; left++) {
         while (
            left <= right &&
            nums[left] + nums[right] > target
         ) right--;
         if (left <= right) {
            subsequenceCounter += Math.pow(2, right - left) % mod;
            subsequenceCounter %= mod;
         }
      }
      return subsequenceCounter
   };
}


const numSubseq = new Solution().numSubseq;
console.log(new Solution().numSubseq([3, 5, 6, 7], 9) === 4)
console.log(new Solution().numSubseq([3, 3, 6, 8], 10) === 6)
console.log(new Solution().numSubseq([2, 3, 3, 4, 6, 7], 12) === 61)
console.log(new Solution().numSubseq([7, 10, 7, 3, 7, 5, 4], 12) === 56)
console.log(new Solution().numSubseq([14, 4, 6, 6, 20, 8, 5, 6, 8, 12, 6, 10, 14, 9, 17, 16, 9, 7, 14, 11, 14, 15, 13, 11, 10, 18, 13, 17, 17, 14, 17, 7, 9, 5, 10, 13, 8, 5, 18, 20, 7, 5, 5, 15, 19, 14], 22) === 272187084)
console.log(new Solution().numSubseq([9, 25, 9, 28, 24, 12, 17, 8, 28, 7, 21, 25, 10, 2, 16, 19, 12, 13, 15, 28, 14, 12, 24, 9, 6, 7, 2, 15, 19, 13, 30, 30, 23, 19, 11, 3, 17, 2, 14, 20, 22, 30, 12, 1, 11, 2, 2, 20, 20, 27, 15, 9, 10, 4, 12, 30, 13, 5, 2, 11, 29, 5, 3, 13, 22, 5, 16, 19, 7, 19, 11, 16, 11, 25, 29, 21, 29, 3, 2, 9, 20, 15, 9], 32) === 91931447)
