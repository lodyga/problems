class Solution {
   /**
    * Time complexity: O(n2^n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash set, list
    *     A: backtracking
    * @param {string[]} nums
    * @return {string}
    */
   findDifferentBinaryString(nums) {
      const N = nums[0].length;
      const binSet = new Set(nums);
      const binary = [];

      const backtrack = (idx) => {
         if (binary.length === N) {
            const missing = binary.join('');
            return binSet.has(missing) ? '' : missing
         }

         for (const chr of '01') {
            binary.push(chr);
            const missing = backtrack(idx + 1);
            
            if (missing) {
               return missing;
            }
            
            binary.pop();
         }
      }

      return backtrack(0);
   }
}


const findDifferentBinaryString = new Solution().findDifferentBinaryString;
console.log(new Solution().findDifferentBinaryString(['0']) === '1')
console.log(new Solution().findDifferentBinaryString(['01', '10']) === '00')
console.log(new Solution().findDifferentBinaryString(['00', '01']) === '10')
console.log(new Solution().findDifferentBinaryString(['111', '011', '001']) === '000')
