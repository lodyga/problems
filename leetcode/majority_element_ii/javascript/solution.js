class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: hash map
    *     A: iteration
    * Boyer-Moore Voting Algorithm
    * @param {number[]} nums
    * @return {number[]}
    */
   majorityElement(nums) {
      const numFreq = new Map();

      for (const num of nums) {
         numFreq.set(num, (numFreq.get(num) || 0) + 1);

         if (numFreq.size === 3) {
            for (const [num, freq] of numFreq.entries()) {
               numFreq.set(num, numFreq.get(num) - 1);
               if (freq === 0) {
                  numFreq.delete(num);
               }
            }
         }
      }

      const res = [];
      for (const num of numFreq.keys()) {
         if (nums.filter(letter => letter === num).length / nums.length > 1 / 3) {
            res.push(num);
         }
      }
      return res
   };
}


const majorityElement = new Solution().majorityElement;
console.log(new Solution().majorityElement([3, 3, 4]).toString() === [3].toString())
console.log(new Solution().majorityElement([3, 2, 3]).toString() === [3].toString())
console.log(new Solution().majorityElement([1]).toString() === [1].toString())
console.log(new Solution().majorityElement([1, 2]).toString() === [1, 2].toString())
console.log(new Solution().majorityElement([3, 4, 5, 3, 4]).toString() === [3, 4].toString())
console.log(new Solution().majorityElement([2, 2]).toString() === [2].toString())
console.log(new Solution().majorityElement([3, 4, 5, 3]).toString() === [3].toString())
console.log(new Solution().majorityElement([3, 4, 5]).toString() === [].toString())
console.log(new Solution().majorityElement([1, 2, 3, 4]).toString() === [].toString())
