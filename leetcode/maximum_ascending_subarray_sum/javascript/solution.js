class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: iteration
    * @param {number[]} nums
    * @return {number}
    */
   maxAscendingSum(nums) {
      let prevNum = nums[0] - 1;
      let currSum = 0;
      let maxSum = 0;

      for (const num of nums) {
         if (prevNum >= num)
            currSum = 0;

         currSum += num;
         maxSum = Math.max(maxSum, currSum);
         prevNum = num;
      }
      return maxSum
   };
}


const maxAscendingSum = new Solution().maxAscendingSum;
console.log(new Solution().maxAscendingSum([10, 20, 30, 5, 10, 50]) === 65)
console.log(new Solution().maxAscendingSum([10, 20, 30, 40, 50]) === 150)
console.log(new Solution().maxAscendingSum([12, 17, 15, 13, 10, 11, 12]) === 33)
