class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash set
    *     A: iteration
    * @param {number[]} nums 
    * @param {number} target 
    * @returns {number[]}
    */
   sum_pairs(nums, target) {
      const numSet = new Set();
      for (const num of nums) {
         const complement = target - num;
         if (numSet.has(complement)) {
            return [complement, num]
         } else {
            numSet.add(num);
         }
      }
      return []
   };
}


const sum_pairs = new Solution().sum_pairs;
console.log(new Solution().sum_pairs([10, 5, 2, 3, 7, 5], 10), [3, 7])
console.log(new Solution().sum_pairs([1, 4, 8, 7, 3, 15], 8), [1, 7])
console.log(new Solution().sum_pairs([1, -2, 3, 0, -6, 1], -6), [0, -6])
console.log(new Solution().sum_pairs([20, -13, 40], -7), [])
console.log(new Solution().sum_pairs([1, 2, 3, 4, 1, 0], 2), [1, 1])
console.log(new Solution().sum_pairs([4, -2, 3, 3, 4], 8), [4, 4])
console.log(new Solution().sum_pairs([0, 2, 0], 0), [0, 0])
console.log(new Solution().sum_pairs([5, 9, 13, -3], 10), [13, -3])
