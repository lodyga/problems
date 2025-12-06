class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     A: binary search
    * @param {number[]} nums
    * @return {number}
    */
   findMin(nums) {
      let left = 0;
      let right = nums.length - 1;
      let minNum = nums[0];

      while (left <= right) {
         // early exit
         if (nums[left] < nums[right]) {
            return Math.min(nums[left], minNum)
         }

         const middle = (left + right) >> 1;
         const middleNum = nums[middle];
         minNum = Math.min(minNum, middleNum);

         if (middleNum < nums[right]) {
            right = middle - 1;
         } else {
            left = middle + 1;
         }
      }
      return minNum
   };
}


const findMin = new Solution().findMin;
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
