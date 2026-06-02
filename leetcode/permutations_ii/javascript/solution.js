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

      const backtrack = (start) => {
         if (start === nums.length - 1) {
            permutationSet.add(JSON.stringify(nums));
            return;
         }

         for (let idx = start; idx < nums.length; idx++) {
            [nums[start], nums[idx]] = [nums[idx], nums[start]];
            backtrack(start + 1);
            [nums[start], nums[idx]] = [nums[idx], nums[start]];
         }
      }

      backtrack(0);
      return [...permutationSet].map(JSON.parse);
   }
}


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
      const permutation = [];
      const res = [];
      const numFreq = new Map();
      
      for (const num of nums) {
         numFreq.set(num, (numFreq.get(num) || 0) + 1);
      }

      const backtrack = () => {
         if (permutation.length === nums.length) {
            res.push(permutation.slice());
            return;
         }

         for (const num of numFreq.keys()) {
            if (numFreq.get(num)) {
               permutation.push(num);
               numFreq.set(num, numFreq.get(num) - 1);
               backtrack();
               numFreq.set(num, numFreq.get(num) + 1);
               permutation.pop();
            }
         }
      }

      backtrack();
      return res;
   }
}



const permuteUnique = new Solution().permuteUnique;
console.log(JSON.stringify((new Solution().permuteUnique([1, 2])).sort()) === JSON.stringify([[1, 2], [2, 1]].sort()))
console.log(JSON.stringify(new Solution().permuteUnique([1, 2, 3]).sort()) === JSON.stringify([[1, 3, 2], [1, 2, 3], [2, 1, 3], [3, 2, 1], [3, 1, 2], [2, 3, 1]].sort()))
console.log(JSON.stringify(new Solution().permuteUnique([1]).sort()) === JSON.stringify([[1]].sort()))
console.log(JSON.stringify(new Solution().permuteUnique([1, 1, 2]).sort()) === JSON.stringify([[1, 2, 1], [2, 1, 1], [1, 1, 2]].sort()))
console.log(JSON.stringify((new Solution().permuteUnique([2, 2, 1, 1])).sort()) === JSON.stringify(([[1, 1, 2, 2], [1, 2, 1, 2], [1, 2, 2, 1], [2, 1, 1, 2], [2, 1, 2, 1], [2, 2, 1, 1]]).sort()))
