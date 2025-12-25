class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     A: greedy, Boyer-Moore Voting
    * @param {number[]} nums
    * @return {number}
    */
   majorityElement(nums) {
      let major = 0;
      let frequency = 0;

      for (const num of nums) {
         if (frequency === 0) {
            major = num;
            frequency = 1;
         } else {
            frequency += num === major ? 1 : -1
         }
      }
      return major
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: hash map
    * @param {number[]} nums
    * @return {number}
    */
   majorityElement(nums) {
      const numberFrequency = new Map();
      let mostFrequentNumber = null;
      let mostFrequency = 0;

      for (const number of nums) {
         numberFrequency.set(number, (numberFrequency.get(number) || 0) + 1);
         if (numberFrequency.get(number) > mostFrequency) {
            mostFrequentNumber = number;
            mostFrequency = numberFrequency.get(number)
         }
      }
      return mostFrequentNumber
   };
}


const majorityElement = new Solution().majorityElement;
console.log(new Solution().majorityElement([3, 2, 3]) === 3)
console.log(new Solution().majorityElement([3, 3, 4]) === 3)
console.log(new Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]) === 2)
