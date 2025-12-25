class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     DS: array
    *     A: two pointers, in-place method
    * @param {number[]} nums
    * @param {number} k
    * @return {number[]}
    */
   rotate(nums, k) {
      const _reverse = (left, right) => {
         while (left < right) {
            [nums[left], nums[right]] = [nums[right], nums[left]];
            left++;
            right--;
         }
      };
      k %= nums.length;
      _reverse(0, nums.length - k - 1);
      _reverse(nums.length - k, nums.length - 1);
      _reverse(0, nums.length - 1);
      return nums
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *    DS: list
    *    A: build-in function
    * @param {number[]} nums
    * @param {number} k
    * @return {number[]}
    */
   rotate2(nums, k) {
      const pivot = nums.length - k % nums.length;
      return [...nums.slice(pivot,), ...nums.slice(0, pivot)]
   };
}


const rotate = new Solution().rotate;
console.log(JSON.stringify(new Solution().rotate([1, 2, 3, 4, 5], 2)) === JSON.stringify([4, 5, 1, 2, 3]))
console.log(JSON.stringify(new Solution().rotate([1, 2, 3], 2)) === JSON.stringify([2, 3, 1]))
console.log(JSON.stringify(new Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)) === JSON.stringify([5, 6, 7, 1, 2, 3, 4]))
console.log(JSON.stringify(new Solution().rotate([1, 2, 3, 4, 5, 6], 1)) === JSON.stringify([6, 1, 2, 3, 4, 5]))
console.log(JSON.stringify(new Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)) === JSON.stringify([5, 6, 7, 1, 2, 3, 4]))
console.log(JSON.stringify(new Solution().rotate([-1, -100, 3, 99], 2)) === JSON.stringify([3, 99, -1, -100]))
console.log(JSON.stringify(new Solution().rotate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], 38)) === JSON.stringify([17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
