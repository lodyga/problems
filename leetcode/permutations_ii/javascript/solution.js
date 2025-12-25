class Solution {
   /**
    * Time complexity: O(n!)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: hash set
    *     A: backtracking
    * @param {number[]} nums
    * @return {number[][]}
    */
   permuteUnique(nums) {
      const permutationSet = new Set();

      const dfs = (left) => {
         if (left === nums.length - 1) {
            permutationSet.add(JSON.stringify(nums));
            return
         }

         for (let right = left; right < nums.length; right++) {
            [nums[left], nums[right]] = [nums[right], nums[left]];
            dfs(left + 1);
            [nums[left], nums[right]] = [nums[right], nums[left]];
         }
      }
      dfs(0)
      return [...permutationSet].map(JSON.parse)
   };

   /**
    * Time complexity: O(n!)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: hash set
    *     A: backtracking
    * @param {number[]} nums
    * @return {number[][]}
    */
   permuteUnique(nums) {
      const permutations = [];

      const dfs = (left) => {
         if (left === nums.length - 1) {
            permutations.push(nums.slice());
            return
         }

         const uniqueLevelValue = new Set();
         for (let right = left; right < nums.length; right++) {
            if (uniqueLevelValue.has(nums[right]))
               continue
            else
               uniqueLevelValue.add(nums[right]);

            [nums[left], nums[right]] = [nums[right], nums[left]];
            dfs(left + 1);
            [nums[left], nums[right]] = [nums[right], nums[left]];
         }
      }
      dfs(0)
      return permutations
   };

   /**
    * Time complexity: O(n!)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: hash set
    *     A: backtracking
    * @param {number[]} nums
    * @return {number[][]}
    */
   permuteUnique(nums) {
      const permutation = [];
      const permutations = [];
      const numFrequency = new Map();
      for (const number of nums) {
         numFrequency.set(number, (numFrequency.get(number) || 0) + 1);
      }

      const dfs = (left) => {
         if (permutation.length === nums.length) {
            permutations.push(permutation.slice());
            return
         }
         for (const number of numFrequency.keys()) {
            if (numFrequency.get(number)) {
               permutation.push(number);
               numFrequency.set(number, numFrequency.get(number) - 1);
               dfs();
               permutation.pop();
               numFrequency.set(number, numFrequency.get(number) + 1);
            }
         }
      }
      dfs()
      return permutations
   };
}



const permuteUnique = new Solution().permuteUnique;
console.log(JSON.stringify((new Solution().permuteUnique([1, 2])).sort()) === JSON.stringify([[1, 2], [2, 1]].sort()))
console.log(JSON.stringify(new Solution().permuteUnique([1, 2, 3]).sort()) === JSON.stringify([[1, 3, 2], [1, 2, 3], [2, 1, 3], [3, 2, 1], [3, 1, 2], [2, 3, 1]].sort()))
console.log(JSON.stringify(new Solution().permuteUnique([1]).sort()) === JSON.stringify([[1]].sort()))
console.log(JSON.stringify(new Solution().permuteUnique([1, 1, 2]).sort()) === JSON.stringify([[1, 2, 1], [2, 1, 1], [1, 1, 2]].sort()))
console.log(JSON.stringify((new Solution().permuteUnique([2, 2, 1, 1])).sort()) === JSON.stringify(([[1, 1, 2, 2], [1, 2, 1, 2], [1, 2, 2, 1], [2, 1, 1, 2], [2, 1, 2, 1], [2, 2, 1, 1]]).sort()))
