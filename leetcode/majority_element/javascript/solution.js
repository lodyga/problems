class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Boyer-Moore Voting Algorithm
    * @param {number[]} numbers
    * @return {number}
    */
   majorityElement(numbers) {
      let major = null;
      let frequency = 0;

      for (const number of numbers) {
         if (frequency === 0) {
            major = number;
            frequency = 1;
         } else {
            frequency += number === major ? 1 : -1
         }
      }
      return major
   };
}
const majorityElement = new Solution().majorityElement;


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: hash map
    * @param {number[]} numbers
    * @return {number}
    */
   majorityElement(numbers) {
      const numberFrequency = new Map();
      let mostFrequentNumber = null;
      let mostFrequency = 0;

      for (const number of numbers) {
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


console.log(new Solution().majorityElement([3, 2, 3]), 3)
console.log(new Solution().majorityElement([3, 3, 4]), 3)
console.log(new Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)