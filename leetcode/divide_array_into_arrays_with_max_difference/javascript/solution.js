class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: sorting
    * @param {number[]} nums
    * @param {number} k
    * @return {number[]}
    */
   divideArray(nums, k) {
      nums.sort((a, b) => a - b);
      const res = [];

      for (let index = 0; index < nums.length; index += 3) {
         if (nums[index + 2] - nums[index] > k) {
            return []
         }
      }

      return Array.from({ length: nums.length / 3 }, (_, k) => nums.slice(3 * k, 3 * k + 3));
   };

   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: sorting
    * @param {number[]} nums
    * @param {number} k
    * @return {number[]}
    */
   divideArray(nums, k) {
      nums.sort((a, b) => a - b);
      const res = [];

      for (let index = 0; index < nums.length; index += 3) {
         if (nums[index + 2] - nums[index] > k) {
            return []
         } else {
            res.push(nums.slice(index, index + 3));
         }
      }

      return res;
   };
}

const divideArray = new Solution().divideArray;
console.log(new Solution().divideArray([1, 3, 4, 8, 7, 9, 3, 5, 1], 2).toString() === [[1, 1, 3], [3, 4, 5], [7, 8, 9]].toString())
console.log(new Solution().divideArray([2, 4, 2, 2, 5, 2], 2).toString() === [].toString())
console.log(new Solution().divideArray([4, 2, 9, 8, 2, 12, 7, 12, 10, 5, 8, 5, 5, 7, 9, 2, 5, 11], 14).toString() === [[2, 2, 2], [4, 5, 5], [5, 5, 7], [7, 8, 8], [9, 9, 10], [11, 12, 12]].toString())
