class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * @param {number[]} numbers
    * @return {boolean}
    */
   containsDuplicate(numbers) {
      const uniqueNumbers = new Set();
      for (const number of numbers) {
         if (uniqueNumbers.has(number)) {
            return true
         } else {
            uniqueNumbers.add(number);
         }
      }
      return false
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: One-liner
    * @param {number[]} numbers
    * @return {boolean}
   */
   containsDuplicate(numbers) {
      return numbers.length !== (new Set(numbers)).size
   }
}


console.log(new Solution().containsDuplicate([1, 2, 3, 1]), true)
console.log(new Solution().containsDuplicate([1, 2, 3]), false)
console.log(new Solution().containsDuplicate([1, 2, 3, 4]), false)
console.log(new Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), true)