class Solution {
   /**
    * Time complexity: O(n2^n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: list
    *     A: backtracking
    * Largest → Smallest
    * @param {number[]} nums
    * @return {number[][]}
    */
   subsetsWithDup(nums) {
      const subset = [];
      const subsetList = [];
      nums.sort((a, b) => a - b);

      const backtrack = (index) => {
         if (index === nums.length) {
            subsetList.push(subset.slice());
            return
         }
         subset.push(nums[index]);
         backtrack(index + 1);
         subset.pop();
         while (
            index + 1 < nums.length &&
            nums[index] === nums[index + 1]
         ) index++;

         backtrack(index + 1);
      }
      backtrack(0);
      return subsetList
   };

   /**
    * Time complexity: O(n2^n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: list
    *     A: backtracking
    * Largest → Smallest
    * @param {number[]} nums
    * @return {number[][]}
    */
   subsetsWithDup(nums) {
      const subset = [];
      const subsetList = [];
      nums.sort((a, b) => a - b);

      const backtrack = (start) => {
         subsetList.push(subset.slice());

         for (let index = start; index < nums.length; index++) {
            if (
               index > start &&
               nums[index] === nums[index - 1]
            ) continue
            subset.push(nums[index]);
            backtrack(index + 1);
            subset.pop();
         }
      }

      backtrack(0)
      return subsetList
   };
}


const subsetsWithDup = new Solution().subsetsWithDup;
console.log(new Solution().subsetsWithDup([0]), [[], [0]])
console.log(new Solution().subsetsWithDup([5, 5]), [[], [5], [5, 5]])
console.log(new Solution().subsetsWithDup([1, 2, 2]), [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])
console.log(new Solution().subsetsWithDup([4, 4, 4, 1, 4]), [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]])
