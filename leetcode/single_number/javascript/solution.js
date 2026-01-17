class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
          A: bit manipulation
    * @param {number[]} nums
    * @return {number}
    */
   singleNumber(nums) {
      let xor = 0;
      for (const num of nums) {
         xor ^= num;
      }
      return xor
   };
}


const singleNumber = new Solution().singleNumber;
console.log(new Solution().singleNumber([2, 2, 1]) == 1)
console.log(new Solution().singleNumber([4, 1, 2, 1, 2]) === 4)
console.log(new Solution().singleNumber([1]) === 1)
