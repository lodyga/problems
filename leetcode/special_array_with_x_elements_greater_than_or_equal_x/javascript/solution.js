class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: binary search
    * @param {number[]} nums
    * @return {number}
    */
   specialArray(nums) {
      let left = 1;
      let right = nums.length;
      let res = -1;

      while (left <= right) {
         const middle = (left + right) >> 1;
         const counter = nums.filter(value => value >= middle).length;
         
         if (counter === middle) {
            return middle;
         } else if (counter < middle) {
            right = middle - 1;
         } else {
            left = middle + 1;
         }
      }
      return -1
   };
}


const specialArray = new Solution().specialArray;
console.log(new Solution().specialArray([3, 5]) === 2)
console.log(new Solution().specialArray([0, 0]) === -1)
console.log(new Solution().specialArray([0, 4, 3, 0, 4]) === 3)
console.log(new Solution().specialArray([3, 6, 7, 7, 0]) === -1)
