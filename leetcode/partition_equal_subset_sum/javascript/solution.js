class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    * @param {number[]} numbers
    * @return {boolean}
    */
   canPartition(numbers) {
      const total = numbers.reduce((sum, number) => sum + number, 0);
      if (total % 2) {
         return false
      }
      const half = total >> 1;
      const subset = new Set([0]);

      for (const number of numbers) {
         const subsetUpdate = new Set(subset);
         subsetUpdate.forEach(value => subset.add(value + number));

         if (subset.has(half)) {
            return true
         }
      }
      return false
   };
}


console.log(new Solution().canPartition([2]) === false)
console.log(new Solution().canPartition([2, 2]) === true)
console.log(new Solution().canPartition([1, 5, 11, 5]) === true)
console.log(new Solution().canPartition([14, 9, 8, 4, 3, 2]) === true)
console.log(new Solution().canPartition([1, 2, 5]) === false)
console.log(new Solution().canPartition([3, 3, 3, 4, 5]) === true)
console.log(new Solution().canPartition([1, 2, 3, 5]) === false)
console.log(new Solution().canPartition([1]) === false)
console.log(new Solution().canPartition([2, 2, 1, 1]) === true)