class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash set
    *     A: iteration
    * @param {number[]} nums
    * @return {number}
    */
   longestConsecutive(nums) {
      const numSet = new Set(nums);
      let res = 0;

      for (const num of numSet) {
         if (numSet.has(num - 1)) continue
         let currNum = num;
         
         while (numSet.has(currNum)) {
            currNum++;
         }
         
         res = Math.max(res, currNum - num);
      }

      return res
   };
}


const longestConsecutive = new Solution().longestConsecutive;
console.log(new Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) === 4)
console.log(new Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) === 9)
console.log(new Solution().longestConsecutive([1, 0, 1, 2]) === 3)
console.log(new Solution().longestConsecutive([]) === 0)
