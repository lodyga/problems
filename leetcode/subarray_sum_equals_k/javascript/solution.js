class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: hash map
    * @param {number[]} numbers
    * @param {number} target
    * @return {number}
    */
   subarraySum(numbers, target) {
      const cache = new Map([[0, 1]]);
      let subarrayCounter = 0;
      let currentSum = 0;

      for (const number of numbers) {
         currentSum += number;
         if (cache.has(currentSum - target)) {
            subarrayCounter += cache.get(currentSum - target)
         }
         cache.set(currentSum, (cache.get(currentSum) || 0) + 1);
      }
      return subarrayCounter
   };
}
const subarraySum = new Solution().subarraySum;


console.log(new Solution().subarraySum([1, 1, 1], 2) === 2)
console.log(new Solution().subarraySum([1, 2, 3], 3) === 2)
console.log(new Solution().subarraySum([1], 0) === 0)
console.log(new Solution().subarraySum([-1, -1, 1], 0) === 1)
console.log(new Solution().subarraySum([1, -1, 1, 1, 1], 2) === 4)