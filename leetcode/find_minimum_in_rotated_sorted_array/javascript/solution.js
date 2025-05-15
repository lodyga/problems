class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags: binary search
    * @param {number[]} numbers
    * @return {number}
    */
   findMin(numbers) {
      let left = 0;
      let right = numbers.length - 1;
      let minNumber = numbers[0];

      while (left <= right) {
         // early exit
         if (numbers[left] < numbers[right]) {
            return Math.min(numbers[left], minNumber)
         }

         const middle = (left + right) / 2 | 0;
         const middleNumber = numbers[middle];
         minNumber = Math.min(minNumber, middleNumber);

         if (middleNumber < numbers[right]) {
            right = middle - 1;
         } else {
            left = middle + 1;
         }
      }
      return minNumber
   };
}


console.log(new Solution().findMin([1, 2, 3, 4]) === 1)
console.log(new Solution().findMin([4, 1, 2, 3]) === 1)
console.log(new Solution().findMin([2, 3, 4, 1]) === 1)
console.log(new Solution().findMin([3, 4, 1, 2]) === 1)
console.log(new Solution().findMin([4, 5, 1, 2, 3]) === 1)
console.log(new Solution().findMin([5, 1, 2, 3, 4]) === 1)
console.log(new Solution().findMin([1, 2, 3, 4, 5]) === 1)
console.log(new Solution().findMin([2, 3, 4, 5, 1]) === 1)
console.log(new Solution().findMin([3, 4, 5, 1, 2]) === 1)
console.log(new Solution().findMin([4, 5, 6, 7, 0, 1, 2]) === 0)
console.log(new Solution().findMin([11, 13, 15, 17]) === 11)
console.log(new Solution().findMin([1]) === 1)
console.log(new Solution().findMin([3, 1, 2]) === 1)