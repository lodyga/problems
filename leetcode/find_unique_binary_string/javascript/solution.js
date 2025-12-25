class Solution {
   /**
    * Time complexity: O(n2^n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: list, hash set
    *     A: backtracking
    * @param {string[]} nums
    * @return {string}
    */
   findDifferentBinaryString(nums) {
      const num = [];
      const numSet = new Set(nums);

      const backtrack = (index) => {
         if (num.length === nums[0].length) {
            const missing = num.join('');
            return numSet.has(missing) ? '' : missing
         }

         for (const digit of '01') {
            num.push(digit);
            const missing = backtrack(index + 1);
            if (missing) {
               return missing
            }
            num.pop();
         }
      }
      return backtrack(0)
   };
}


const findDifferentBinaryString = new Solution().findDifferentBinaryString;
console.log(new Solution().findDifferentBinaryString(['0']) === '1')
console.log(new Solution().findDifferentBinaryString(['01', '10']) === '00')
console.log(new Solution().findDifferentBinaryString(['00', '01']) === '10')
console.log(new Solution().findDifferentBinaryString(['111', '011', '001']) === '000')
