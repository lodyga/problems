class Solution {
   /**
    * Time complexity: O((nm)logn(nm))
    *     n, m: grid size
    * Auxiliary space complexity: O(nm)
    * Tags:
    *     DS: array
    *     A: sorting
    * @param {number[][]} grid
    * @param {number} x
    * @return {}
    */
   minOperations(grid, x) {
      const nums = [];
      for (const row of grid) {
         for (const num of row) {
            nums.push(num);
         }
      }
      const mod = nums[0] % x;

      for (const num of nums) {
         if (num % x !== mod) {
            return -1
         }
      }

      nums.sort((a, b) => a - b);
      const median = nums[Math.floor(nums.length / 2)];
      return nums
         .map(num => Math.abs(num - median) / x)
         .reduce((sum, num) => sum + num, 0)
   };
}


const minOperations = new Solution().minOperations;
console.log(new Solution().minOperations([[2, 4], [6, 8]], 2) === 4)
console.log(new Solution().minOperations([[1, 5], [2, 3]], 1) === 5)
console.log(new Solution().minOperations([[1, 2], [3, 4]], 2) === -1)
console.log(new Solution().minOperations([[146]], 86) === 0)
console.log(new Solution().minOperations([[931, 128], [639, 712]], 73) === 12)
console.log(new Solution().minOperations([[1, 1, 10000]], 1) === 9999)
console.log(new Solution().minOperations([[503, 503, 9852, 9852, 9852, 9852, 9852, 503, 9852, 503], [9852, 9852, 9852, 9852, 503, 9852, 9852, 9852, 503, 503], [503, 503, 9852, 9852, 9852, 9852, 9852, 503, 9852, 9852], [9852, 9852, 503, 9852, 503, 9852, 503, 503, 9852, 503], [503, 503, 503, 503, 9852, 9852, 503, 503, 503, 503], [9852, 503, 9852, 9852, 9852, 9852, 503, 9852, 9852, 503], [503, 503, 9852, 9852, 503, 503, 9852, 503, 9852, 9852], [503, 9852, 503, 9852, 503, 503, 503, 503, 503, 503], [503, 503, 9852, 9852, 9852, 503, 503, 503, 9852, 9852], [9852, 9852, 9852, 9852, 503, 503, 503, 503, 503, 9852]], 9349) === 49)
