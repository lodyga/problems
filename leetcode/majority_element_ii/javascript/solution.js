class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map
    *     A: iteration
    * @param {number[]} nums
    * @return {number[]}
    */
   majorityElement(nums) {
      const numFreq = new Map();
      const res = [];

      for (const num of nums) {
         numFreq.set(num, (numFreq.get(num) || 0) + 1);
      }

      for (const [num, freq] of numFreq.entries()) {
         if (freq > nums.length / 3) {
            res.push(num);
         }
      }

      return res;
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: hash map
    *     A: iteration, voting
    * @param {number[]} nums
    * @return {number[]}
    */
   majorityElement(nums) {
      const numFreq = new Map();
      const res = [];

      for (const num of nums) {
         numFreq.set(num, (numFreq.get(num) || 0) + 1);

         if (numFreq.size > 2) {
            for (const [numF, freq] of numFreq.entries()) {
               if (freq === 1) {
                  numFreq.delete(numF);
               }
               else {
                  numFreq.set(numF, numFreq.get(num) - 1);
               }

            }
         }
      }

      for (const numF of numFreq.keys()) {
         if (nums.filter(num => num === numF).length > nums.length / 3) {
            res.push(numF);
         }
      }

      return res;
   }
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
