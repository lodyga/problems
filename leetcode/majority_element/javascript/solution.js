class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy, voting
    * @param {number[]} nums
    * @return {number}
    */
   majorityElement(nums) {
      let majorVal = 0;
      let majorFreq = 0;

      for (const num of nums) {
         if (majorFreq === 0) {
            majorVal = num;
            majorFreq = 1;
         } else {
            majorFreq += num === majorVal ? 1 : -1
         }
      }

      return majorVal;
   }
}


const majorityElement = new Solution().majorityElement;
console.log(new Solution().majorityElement([3, 2, 3]) === 3)
console.log(new Solution().majorityElement([3, 3, 4]) === 3)
console.log(new Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]) === 2)
