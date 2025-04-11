class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * @param {int[]} numbers 
    * @param {int} target 
    * @returns 
    */
   sum_pairs(numbers, target) {
      const uniqueNumbers = new Set();

      for (const number of numbers) {
         const complement = target - number;
         if (uniqueNumbers.has(complement)) {
            return [complement, number]
         } else {
            uniqueNumbers.add(number);
         }
      }
      return undefined
   }
}


console.log(new Solution().sum_pairs([10, 5, 2, 3, 7, 5], 10), [3, 7])
console.log(new Solution().sum_pairs([1, 4, 8, 7, 3, 15], 8), [1, 7])
console.log(new Solution().sum_pairs([1, -2, 3, 0, -6, 1], -6), [0, -6])
console.log(new Solution().sum_pairs([20, -13, 40], -7), undefined)
console.log(new Solution().sum_pairs([1, 2, 3, 4, 1, 0], 2), [1, 1])
console.log(new Solution().sum_pairs([4, -2, 3, 3, 4], 8), [4, 4])
console.log(new Solution().sum_pairs([0, 2, 0], 0), [0, 0])
console.log(new Solution().sum_pairs([5, 9, 13, -3], 10), [13, -3])