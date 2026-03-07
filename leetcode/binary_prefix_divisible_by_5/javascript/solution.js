class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: list
    *     A: bit manipulation
    * @param {number[]} nums
    * @return {boolean[]}
    */
   prefixesDivBy5(nums) {
      let val = 0
      const res = [];

      for (const num of nums) {
         val = (val * 2 + num) % 5
         res.push(val === 0);
      }

      return res
   };
}


const prefixesDivBy5 = new Solution().prefixesDivBy5;
console.log(new Solution().prefixesDivBy5([0, 1, 1]).toString() === [true, false, false].toString())
console.log(new Solution().prefixesDivBy5([0, 1, 1, 1, 1, 1]).toString() === [true, false, false, false, true, false].toString())
console.log(new Solution().prefixesDivBy5([1, 1, 1]).toString() === [false, false, false].toString())
console.log(new Solution().prefixesDivBy5([1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1]).toString() === [false, false, true, true, true, true, true, true, true, true, true, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, true, true, false, false, false, true, true, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, true, true, true, false, false, false].toString())
