class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags: binary search
    * @param {number[]} numbers
    * @return {number}
    */
   singleNonDuplicate(numbers) {
      let left = 0
      let right = numbers.length - 1

      while (left < right) {
         const middle = (left + right) >> 1;
         const isPortionOdd = (middle - left) % 2;

         if (
            numbers[middle - 1] != numbers[middle] &&
            numbers[middle] != numbers[middle + 1]
         ) return numbers[middle]
         else if (isPortionOdd && numbers[middle - 1] === numbers[middle])
            left = middle + 1
         else if (isPortionOdd && numbers[middle] === numbers[middle + 1])
            right = middle - 1
         else if (!isPortionOdd && numbers[middle - 1] === numbers[middle])
            right = middle - 2
         else if (!isPortionOdd && numbers[middle] === numbers[middle + 1])
            left = middle + 2
      }
      return numbers[left]
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: slick
    * @param {number[]} numbers
    * @return {number}
    */
   singleNonDuplicate(numbers) {
      let xorr = 0;
      
      for (const number of numbers)
         xorr ^= number
      return xorr
   };
}
const singleNonDuplicate = new Solution().singleNonDuplicate;


console.log(new Solution().singleNonDuplicate([1]) === 1)
console.log(new Solution().singleNonDuplicate([1, 2, 2]) === 1)
console.log(new Solution().singleNonDuplicate([1, 1, 2]) === 2)
console.log(new Solution().singleNonDuplicate([1, 1, 2, 3, 3]) === 2)
console.log(new Solution().singleNonDuplicate([1, 1, 2, 2, 3, 4, 4]) === 3)
console.log(new Solution().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]) === 10)
console.log(new Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) === 2)
console.log(new Solution().singleNonDuplicate([1, 1, 2, 2, 3, 3, 4, 5, 5]) === 4)
console.log(new Solution().singleNonDuplicate([1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7]) === 4)