class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space compl
    * Tags:
    *     DS: hash set
    *     A: iteration
    * @param {number[]} nums
    * @return {number}
    */
   longestConsecutive(nums) {
      const numSet = new Set(nums);
      let maxLength = 0;

      for (const num of numSet) {
         if (numSet.has(num - 1)) {
            continue
         }
         let index = 0;
         while (numSet.has(num + index)) {
            index++;
            maxLength = Math.max(maxLength, index);
         }
      }
      return maxLength
   };
}


const longestConsecutive = new Solution().longestConsecutive;
console.log(new Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) === 4)
console.log(new Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) === 9)
console.log(new Solution().longestConsecutive([1, 0, 1, 2]) === 3)
console.log(new Solution().longestConsecutive([]) === 0)
