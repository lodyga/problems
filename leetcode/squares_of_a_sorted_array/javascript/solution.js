class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: two pointers
    * @param {number[]} numbers
    * @return {number[]}
    */
   sortedSquares(numbers) {
      const squares = [];
      let left = 0;
      let right = numbers.length - 1;

      while (left <= right) {
         if (Math.abs(numbers[left]) > Math.abs(numbers[right])) {
            squares.push(numbers[left] ** 2);
            left++;
         } else {
            squares.push(numbers[right] ** 2);
            right--;
         }
      }
      return squares.reverse();
   };
}


const sortedSquares = new Solution().sortedSquares;
console.log(new Solution().sortedSquares([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])
console.log(new Solution().sortedSquares([-7, -3, 2, 3, 11]), [4, 9, 9, 49, 121])
console.log(new Solution().sortedSquares([1, 2, 3]), [1, 4, 9])
console.log(new Solution().sortedSquares([-3, -2, -1]), [1, 4, 9])
console.log(new Solution().sortedSquares([0]), [0])
console.log(new Solution().sortedSquares([0, 1]), [0, 1])
console.log(new Solution().sortedSquares([-10000, -9999, -7, -5, 0, 0, 10000]), [0, 0, 25, 49, 99980001, 100000000, 100000000])
console.log(new Solution().sortedSquares([-1, 1]), [1, 1])
console.log(new Solution().sortedSquares([-1, 1, 1]), [1, 1, 1])
console.log(new Solution().sortedSquares([-3, -3, -2, 1]), [1, 4, 9, 9])