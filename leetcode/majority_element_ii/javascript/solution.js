class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: 
    * Boyer-Moore Voting Algorithm
    * @param {number[]} numbers
    * @return {number[]}
    */
   majorityElement(numbers) {
      const frequencies = new Map();
      const thresthold = parseInt(numbers.length / 3);

      for (const number of numbers) {
         frequencies.set(number, (frequencies.get(number) || 0) + 1);

         if (frequencies.size > 2) {
            for (const [number, frequency] of frequencies.entries()) {
               if (frequency === 1) {
                  frequencies.delete(number);
               } else {
                  frequencies.set(number, frequencies.get(number) - 1);
               }
            }
         }
      }
      
      const mostFrequentNumbers = [];
      for (const number of frequencies.keys()) {
         if (numbers.filter(letter => letter === number).length > thresthold) {
            mostFrequentNumbers.push(number);
         }
      }
      return mostFrequentNumbers
   };
}
const majorityElement = new Solution().majorityElement;


console.log(new Solution().majorityElement([3, 3, 4]), [3])
console.log(new Solution().majorityElement([3, 2, 3]), [3])
console.log(new Solution().majorityElement([1]), [1])
console.log(new Solution().majorityElement([1, 2]), [1, 2])
console.log(new Solution().majorityElement([3, 4, 5, 3, 4]), [3, 4])
console.log(new Solution().majorityElement([2, 2]), [2])
console.log(new Solution().majorityElement([3, 4, 5, 3]), [3])
console.log(new Solution().majorityElement([3, 4, 5]), [])