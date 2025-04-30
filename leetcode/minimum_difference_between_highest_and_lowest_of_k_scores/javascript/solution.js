class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * @param {number[]} numbers
    * @param {number} k
    * @return {number}
    */
   minimumDifference(numbers, k) {
      if (k === 1) 
         return 0

      numbers.sort((a, b) => a - b);
      let minDiff = Infinity;

      for (let index = 0; index < numbers.length - k + 1; index++) {
         minDiff = Math.min(minDiff, numbers[index + k - 1] - numbers[index])
      }
      return minDiff
   };
}


console.log(new Solution().minimumDifference([90], 1), 0)
console.log(new Solution().minimumDifference([9, 4, 1, 7], 2), 2)
console.log(new Solution().minimumDifference([87063, 61094, 44530, 21297, 95857, 93551, 9918], 6), 74560)