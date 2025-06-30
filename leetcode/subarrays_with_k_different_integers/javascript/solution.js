class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: sliding window
    * @param {number[]} numbers
    * @param {number} uniqueNumebrCounter
    * @return {number}
    */
   subarraysWithKDistinct(numbers, uniqueNumebrCounter) {
      const window = new Map();
      let left = 0;
      let middle = 0;
      let substringCounter = 0;

      for (const number of numbers) {
         window.set(number, (window.get(number) || 0) + 1);

         while (window.size > uniqueNumebrCounter) {
            const middleNumber = numbers[middle];
            window.set(middleNumber, window.get(middleNumber) - 1);

            if (window.get(middleNumber) === 0) {
               window.delete(middleNumber);
            }
            middle++;
            left = middle;
         }

         let middleNumber = numbers[middle];
         while (window.get(middleNumber) > 1) {
            window.set(middleNumber, window.get(middleNumber) - 1);
            middle++;
            middleNumber = numbers[middle];
         }

         if (window.size === uniqueNumebrCounter) {
            substringCounter += middle - left + 1;
         }
      }
      return substringCounter
   };
}


console.log(new Solution().subarraysWithKDistinct([1, 2, 1, 2, 3], 2) === 7)
console.log(new Solution().subarraysWithKDistinct([1, 2, 1, 3, 4], 3) === 3)