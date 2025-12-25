class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *    DS: array
    *    A: two pointers
    * @param {number[]} nums
    * @return {number[]}
    */
   sortedSquares(nums) {
      const squares = Array(nums.length);
      let left = 0;
      let right = nums.length - 1;

      while (left <= right) {
         const leftNum = Math.abs(nums[left]);
         const rightNum = Math.abs(nums[right]);
         const index = (nums.length - 1 - right) + left;

         if (leftNum > rightNum) {
            squares[index] = leftNum ** 2;
            left++;
         } else {
            squares[index] = rightNum ** 2;
            right--;
         }
      }
      return squares.reverse();
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *    DS: array
    *    A: two pointers
    * @param {number[]} nums
    * @return {number[]}
    */
   sortedSquares(nums) {
      const squares = [];
      let left = 0;
      let right = nums.length - 1;

      while (left <= right) {
         const leftNum = Math.abs(nums[left]);
         const rightNum = Math.abs(nums[right]);

         if (leftNum > rightNum) {
            squares.push(leftNum ** 2);
            left++;
         } else {
            squares.push(rightNum ** 2);
            right--;
         }
      }
      return squares.reverse();
   };
}


const sortedSquares = new Solution().sortedSquares;
console.log(JSON.stringify(new Solution().sortedSquares([-4, -1, 0, 3, 10])) === JSON.stringify([0, 1, 9, 16, 100]))
console.log(JSON.stringify(new Solution().sortedSquares([-7, -3, 2, 3, 11])) === JSON.stringify([4, 9, 9, 49, 121]))
console.log(JSON.stringify(new Solution().sortedSquares([1, 2, 3])) === JSON.stringify([1, 4, 9]))
console.log(JSON.stringify(new Solution().sortedSquares([-3, -2, -1])) === JSON.stringify([1, 4, 9]))
console.log(JSON.stringify(new Solution().sortedSquares([0])) === JSON.stringify([0]))
console.log(JSON.stringify(new Solution().sortedSquares([0, 1])) === JSON.stringify([0, 1]))
console.log(JSON.stringify(new Solution().sortedSquares([-10000, -9999, -7, -5, 0, 0, 10000])) === JSON.stringify([0, 0, 25, 49, 99980001, 100000000, 100000000]))
console.log(JSON.stringify(new Solution().sortedSquares([-1, 1])) === JSON.stringify([1, 1]))
console.log(JSON.stringify(new Solution().sortedSquares([-1, 1, 1])) === JSON.stringify([1, 1, 1]))
console.log(JSON.stringify(new Solution().sortedSquares([-3, -3, -2, 1])) === JSON.stringify([1, 4, 9, 9]))
