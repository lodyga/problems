class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: array
    *     A: two pointers
    * @param {number[]} nums
    * @return {number[]}
    */
   rearrangeArray(nums) {
      nums.sort((a, b) => a - b);
      const res = [...nums];

      const mid = nums.length >> 1;
      let index = 0;
      let left = 0;
      let right = 0;

      if (nums.length % 2) {
         res[0] = nums[mid];
         left = mid - 1;
         right = mid + 1;
         index += 1
      } else {
         left = mid - 1;
         right = mid;
      }

      while (right < nums.length) {
         res[index] = nums[left];
         index += 1;
         res[index] = nums[right];
         index += 1;
         left -= 1;
         right += 1;
      }
      return res
   };

   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: list
    *     A: two pointers
    * @param {number[]} nums
    * @return {number[]}
    */
   rearrangeArray(nums) {
      nums.sort((a, b) => a - b);
      const res = [];

      const mid = nums.length >> 1;
      let left = 0;
      let right = 0;

      if (nums.length % 2) {
         res.push(nums[mid]);
         left = mid - 1;
         right = mid + 1;
      } else {
         left = mid - 1;
         right = mid;

      }

      while (right < nums.length) {
         res.push(nums[left]);
         res.push(nums[right]);
         left -= 1;
         right += 1;
      }
      return res
   };
}


const rearrangeArray = new Solution().rearrangeArray;
console.log(JSON.stringify(new Solution().rearrangeArray([1, 2, 3, 4, 5])) === JSON.stringify([3, 2, 4, 1, 5]))
console.log(JSON.stringify(new Solution().rearrangeArray([1, 2, 3, 4])) === JSON.stringify([2, 3, 1, 4]))
console.log(JSON.stringify(new Solution().rearrangeArray([6, 2, 0, 9, 7])) === JSON.stringify([6, 2, 7, 0, 9]))
console.log(JSON.stringify(new Solution().rearrangeArray([1, 3, 2])) === JSON.stringify([2, 1, 3]))
console.log(JSON.stringify(new Solution().rearrangeArray([15, 7, 13, 6, 3, 11, 14, 1, 20])) === JSON.stringify([11, 7, 13, 6, 14, 3, 15, 1, 20]))
