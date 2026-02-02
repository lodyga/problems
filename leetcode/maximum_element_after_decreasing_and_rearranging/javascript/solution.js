class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: greedy, sorting
    * @param {number[]} nums
    * @return {number}
    */
   maximumElementAfterDecrementingAndRearranging(nums) {
      nums.sort((a, b) => a - b);
      let maxNum = 0;

      for (const num of nums)
         if (num > maxNum)
            maxNum++;

      return maxNum
   };
}


const maximumElementAfterDecrementingAndRearranging = new Solution().maximumElementAfterDecrementingAndRearranging;
console.log(new Solution().maximumElementAfterDecrementingAndRearranging([2, 2, 1, 2, 1]) === 2)
console.log(new Solution().maximumElementAfterDecrementingAndRearranging([100, 1, 1000]) === 3)
console.log(new Solution().maximumElementAfterDecrementingAndRearranging([1, 2, 3, 4, 5]) === 5)
console.log(new Solution().maximumElementAfterDecrementingAndRearranging([73, 98, 9]) === 3)
console.log(new Solution().maximumElementAfterDecrementingAndRearranging([5, 3, 3, 1]) === 4)
