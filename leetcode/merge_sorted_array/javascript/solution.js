class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: two pointers, in-place method
    * @param {number[]} numbers1
    * @param {number} m
    * @param {number[]} numbers2
    * @param {number} n
    * @return {number[]}
    */
   merge(numbers1, m, numbers2, n) {
      let right1 = m - 1;
      let right2 = n - 1;
      let index = m + n - 1;

      while (
         right1 != -1 &&
         right2 != -1
      ) {
         if (numbers1[right1] > numbers2[right2]) {
            numbers1[index] = numbers1[right1];
            right1--;
         } else {
            numbers1[index] = numbers2[right2];
            right2--;
         }
         index--;
      }
      while (right2 != -1) {
         numbers1[index] = numbers2[right2];
         right2--;
         index--;
      }
      return numbers1
   };
}


console.log(new Solution().merge([1], 1, [], 0), [1])
console.log(new Solution().merge([0], 0, [1], 1), [1])
console.log(new Solution().merge([2, 0], 1, [1], 1), [1, 2])
console.log(new Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3), [1, 2, 2, 3, 5, 6])
console.log(new Solution().merge([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3), [-1, 0, 0, 1, 2, 2, 3, 3, 3])
console.log(new Solution().merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3), [1, 2, 3, 4, 5, 6])