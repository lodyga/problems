class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: list
    *     A: iteration
    * @param {number[]} nums
    * @param {number} n
    * @return {number[]}
    */
   shuffle(nums, n) {
      const res = [];

      for (let index = 0; index < n; index++) {
         res.push(nums[index]);
         res.push(nums[index + n]);
      }

      return res
   };
}


const shuffle = new Solution().shuffle;
console.log(new Solution().shuffle([2, 5, 1, 3, 4, 7], 3).toString() === [2, 3, 5, 4, 1, 7].toString())
console.log(new Solution().shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4).toString() === [1, 4, 2, 3, 3, 2, 4, 1].toString())
console.log(new Solution().shuffle([1, 1, 2, 2], 2).toString() === [1, 2, 1, 2].toString())
