class Solution {
   /**
    * Time complexity: O(n2)
    *     O(n*s)
    *     n: nums length
    *     s: nums sum
    * Auxiliary space complexity: O(n)
    *     O(s)
    * Tags:
    *     DS: bottom-up, hash set
    *     A: bottom-up
    * @param {number[]} nums
    * @return {boolean}
    */
   canPartition(nums) {
      const total = nums.reduce((total, value) => total + value, 0);
      if (total % 2) {
         return false
      }
      const half = total >> 1;
      const numSet = new Set();

      for (const num of nums) {
         const numSetUpdate = new Set([...numSet].map(value => value + num));
         numSetUpdate.add(num);
         numSetUpdate.forEach(value => numSet.add(value));
         if (numSet.has(half)) {
            return true
         }
      }
      return false
   };
}


const canPartition = new Solution().canPartition;
console.log(new Solution().canPartition([2]) === false)
console.log(new Solution().canPartition([2, 2]) === true)
console.log(new Solution().canPartition([1, 5, 11, 5]) === true)
console.log(new Solution().canPartition([14, 9, 8, 4, 3, 2]) === true)
console.log(new Solution().canPartition([1, 2, 5]) === false)
console.log(new Solution().canPartition([3, 3, 3, 4, 5]) === true)
console.log(new Solution().canPartition([1, 2, 3, 5]) === false)
console.log(new Solution().canPartition([1]) === false)
console.log(new Solution().canPartition([2, 2, 1, 1]) === true)
console.log(new Solution().canPartition([100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 99, 97]) === false)
