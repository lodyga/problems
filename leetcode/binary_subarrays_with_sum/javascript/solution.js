class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: sliding window
    * @param {number[]} numbers
    * @param {number} goal
    * @return {number}
    */
   numSubarraysWithSum(numbers, goal) {
      let left = 0;
      let middle = 0;
      let subarrayCounter = 0;

      for (let right = 0; right < numbers.length; right++) {
         goal -= numbers[right];

         while (
            middle < right &&
            goal < 0
         ) {
            goal += numbers[middle];
            middle++;
            left = middle;
         }
         
         if (goal === 0) {
            while (
               middle < right &&
               numbers[middle] === 0
            ) {
               middle++;
            }
            subarrayCounter += (middle - left + 1);
         }
      }
      return subarrayCounter
   };
}
const numSubarraysWithSum = new Solution().numSubarraysWithSum;


console.log(new Solution().numSubarraysWithSum([0, 1, 1, 0], 2), 4)
console.log(new Solution().numSubarraysWithSum([0, 1, 1, 0, 1], 2), 5)
console.log(new Solution().numSubarraysWithSum([1, 0, 1, 0, 1], 2), 4)
console.log(new Solution().numSubarraysWithSum([0, 0, 1], 0), 3)
console.log(new Solution().numSubarraysWithSum([0, 0, 0, 0, 0], 0), 15)
console.log(new Solution().numSubarraysWithSum([0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 0), 27)