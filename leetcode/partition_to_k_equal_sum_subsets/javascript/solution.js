class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    * @param {number[]} numbers
    * @param {number} k
    * @return {boolean}
    */
   canPartitionKSubsets(numbers, k) {
      const TOTAL = numbers.reduce((total, value) => total + value, 0)
      if ((TOTAL / k) % 1 !== 0)
         return false

      const partitionSum = TOTAL / k;
      numbers.sort((a, b) => (b - a));
      const partitionsSize = Array(k).fill(0);

      const dfs = (numberIndex, partitionIndex) => {
         
         const number = numbers[numberIndex];

         partitionsSize[partitionIndex] += number;
         dfs(numberIndex + 1, partitionIndex)

         partitionsSize[partitionIndex] -= number;
         dfs(numberIndex + 1, partitionIndex + 1)
      };

      return dfs(0, 0);

      // return numbers
   };
}


console.log(new Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4) === true)
console.log(new Solution().canPartitionKSubsets([1, 2, 3, 4], 3) === false)
console.log(new Solution().canPartitionKSubsets([3, 9, 4, 5, 8, 8, 7, 9, 3, 6, 2, 10, 10, 4, 10, 2], 10) === false)
console.log(new Solution().canPartitionKSubsets([4, 5, 9, 3, 10, 2, 10, 7, 10, 8, 5, 9, 4, 6, 4, 9], 5) === true)
console.log(new Solution().canPartitionKSubsets([10, 1, 10, 9, 6, 1, 9, 5, 9, 10, 7, 8, 5, 2, 10, 8], 11) === false)


console.log(new Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4) ,true)
console.log(new Solution().canPartitionKSubsets([1, 2, 3, 4], 3) ,false)
console.log(new Solution().canPartitionKSubsets([3, 9, 4, 5, 8, 8, 7, 9, 3, 6, 2, 10, 10, 4, 10, 2], 10) ,false)
console.log(new Solution().canPartitionKSubsets([4, 5, 9, 3, 10, 2, 10, 7, 10, 8, 5, 9, 4, 6, 4, 9], 5) ,true)
console.log(new Solution().canPartitionKSubsets([10, 1, 10, 9, 6, 1, 9, 5, 9, 10, 7, 8, 5, 2, 10, 8], 11) ,false)