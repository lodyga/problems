class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: sliding window as hash set
    * @param {number[]} numbers
    * @param {number} windowLength
    * @return {boolean}
    */
   containsNearbyDuplicate(numbers, windowLength) {
      windowLength = windowLength < numbers.length - 1 ? windowLength : numbers.length - 1;
      const numberCount = new Set();

      for (let index = 0; index < numbers.length; index++) {
         const number = numbers[index];
         numberCount.add(number)

         if (index >= windowLength) {
            if (numberCount.size <= windowLength) {
               return true
            } else {
               const leftNumber = numbers[index - windowLength];
               numberCount.delete(leftNumber);
            }
         }
      }
      return false
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: sliding window as hash map
    * @param {number[]} numbers
    * @param {number} windowLength
    * @return {boolean}
    */
   containsNearbyDuplicate(numbers, windowLength) {
      windowLength = windowLength < numbers.length - 1 ? windowLength : numbers.length - 1;
      const numberCount = new Map();

      for (let index = 0; index < numbers.length; index++) {
         const number = numbers[index];
         const value = (numberCount.get(number) || 0) + 1
         numberCount.set(number, value);

         if (index >= windowLength) {
            if (numberCount.size <= windowLength) {
               return true
            }
            const leftNumber = numbers[index - windowLength];
            numberCount.set(leftNumber, numberCount.get(leftNumber) - 1);
            if (numberCount.get(leftNumber) === 0) {
               numberCount.delete(leftNumber);
            }
         }
      }
      return false
   };
}


console.log(new Solution().containsNearbyDuplicate([1, 2, 3, 1], 3) == true)
console.log(new Solution().containsNearbyDuplicate([7, 8, 9, 9], 3) == true)
console.log(new Solution().containsNearbyDuplicate([1, 0, 1, 1], 1) == true)
console.log(new Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) == false)
console.log(new Solution().containsNearbyDuplicate([99, 99], 2) == true)
console.log(new Solution().containsNearbyDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 9], 3) == true)