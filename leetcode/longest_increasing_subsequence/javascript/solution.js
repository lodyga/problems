class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags: dp, bottom-up with cache as list
    * @param {number[]} numbers
    * @return {number}
    */
   lengthOfLIS(numbers) {
      const cache = Array(numbers.length).fill(1);

      for (let right = 1; right < numbers.length; right++) {
         for (let left = 0; left < right; left++) {
            if (numbers[left] < numbers[right]) {
               cache[right] = Math.max(cache[right], 1 + cache[left])
            }
         }
      }
      return Math.max(...cache)
   };
}


console.log(new Solution().lengthOfLIS([5]) === 1)
console.log(new Solution().lengthOfLIS([5, 6]) === 2)
console.log(new Solution().lengthOfLIS([5, 4]) === 1)
console.log(new Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) === 4)
console.log(new Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]) === 4)
console.log(new Solution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) === 1)
console.log(new Solution().lengthOfLIS([4, 10, 4, 3, 8, 9]) === 3)
console.log(new Solution().lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]) === 6)