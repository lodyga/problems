class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: bit manipulation
    * @param {number[]} numbers
    * @return {number}
    */
   singleNumber(numbers) {
      let xor = 0;
      for (const number of numbers) {
         xor ^= number
      }
      return xor
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: hash set
    * @param {number[]} numbers
    * @return {number}
    */
   singleNumber(numbers) {
      const uniqueNumbers = new Set();
      for (const number of numbers) {
         if (uniqueNumbers.has(number)) {
            uniqueNumbers.delete(number);
         } else {
            uniqueNumbers.add(number);
         }
      }
      return [...uniqueNumbers].pop()
   };
}
const singleNumber = new Solution().singleNumber;


console.log(new Solution().singleNumber([2, 2, 1]) == 1)
console.log(new Solution().singleNumber([4, 1, 2, 1, 2]) === 4)
console.log(new Solution().singleNumber([1]) === 1)