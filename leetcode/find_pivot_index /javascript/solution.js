class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *    DS: prefix sum
    * @param {number[]} nums
    * @return {number}
    */
   pivotIndex(nums) {
      let prefix = 0;
      let suffix = nums.reduce((total, num) => total + num, 0);

      for (let index = 0; index < nums.length; index++) {
         const num = nums[index];
         suffix -= num;
         
         if (prefix === suffix) {
            return index
         }
         prefix += num;
      }
      return -1
   };
}


const pivotIndex = new Solution().pivotIndex;
console.log(new Solution().pivotIndex([1, 7, 3, 6, 5, 6]) === 3)
console.log(new Solution().pivotIndex([1, 2, 3]) === -1)
console.log(new Solution().pivotIndex([2, 1, -1]) === 0)
