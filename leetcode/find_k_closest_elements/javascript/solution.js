class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: two pointers
    * @param {number[]} numbers
    * @param {number} k
    * @param {number} target
    * @return {number[]}
    */
   findClosestElements(numbers, k, target) {
      let left = 0;
      let right = numbers.length - 1;

      while (right - left + 1 > k) {
         if (target - numbers[left] <= numbers[right] - target) {
            right--;
         } else {
            left++;
         }
      }
      return numbers.slice(left, right + 1)
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: deque
    * @param {number[]} numbers
    * @param {number} k
    * @param {number} target
    * @return {number[]}
    */
   findClosestElements(numbers, k, target) {
      while (numbers.length > k) {
         if (target - numbers[0] <= numbers[numbers.length - 1] - target) {
            numbers.pop();
         } else {
            numbers.shift();
         }
      }
      return numbers
   };
}


console.log(new Solution().findClosestElements([1, 2, 3, 4, 5], 4, 3), [1, 2, 3, 4])
console.log(new Solution().findClosestElements([1, 1, 2, 3, 4, 5], 4, -1), [1, 1, 2, 3])
console.log(new Solution().findClosestElements([0, 1, 2, 2, 2, 3, 6, 8, 8, 9], 5, 9), [3, 6, 8, 8, 9])