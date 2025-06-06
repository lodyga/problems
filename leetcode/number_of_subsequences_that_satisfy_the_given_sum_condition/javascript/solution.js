class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: two pointers
    * @param {number[]} numbers
    * @param {number} target
    * @return {number}
    */
   numSubseq(numbers, target) {
      numbers.sort((a, b) => a - b);
      let right = numbers.length - 1;
      let subsequenceCounter = 0;
      const mod = 10 ** 9 + 7;

      for (let left = 0; left < numbers.length; left++) {
         while (
            left <= right &&
            numbers[left] + numbers[right] > target
         ) right--;
         if (left <= right) {
            subsequenceCounter += Math.pow(2, right - left) % mod;
            subsequenceCounter %= mod;
         }
      }
      return subsequenceCounter
   };
}


class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: two pointers
    * @param {number[]} numbers
    * @param {number} target
    * @return {number}
    */
   numSubseq(numbers, target) {
      numbers.sort((a, b) => a - b);
      let subsequenceCounter = 0;
      let right = numbers.length - 1;
      const mod = 10 ** 9 + 7;
      const powersOfTwo = [1];

      for (let index = 1; index < numbers.length; index++) {
         powersOfTwo[index] = powersOfTwo[index - 1] * 2 % mod
      }

      for (let left = 0; left < numbers.length; left++) {
         while (
            left <= right &&
            numbers[left] + numbers[right] > target
         ) right--;

         if (left <= right) {
            subsequenceCounter += powersOfTwo[right - left];
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