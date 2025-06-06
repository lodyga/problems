class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: two pointers
    * @param {number[]} numbers
    * @param {number} k
    * @return {number[]}
    */
   rotate(numbers, k) {
      k %= numbers.length;
      reverseInplace(0, numbers.length - 1);
      reverseInplace(0, k - 1);
      reverseInplace(k, numbers.length - 1);
      return numbers

      function reverseInplace(left, right) {
         while (left < right) {
            [numbers[left], numbers[right]] = [numbers[right], numbers[left]];
            left++;
            right--;
         }
      }
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: build-in function
    * @param {number[]} numbers
    * @param {number} k
    * @return {number[]}
    */
   rotate(numbers, k) {
      const index = numbers.length - k;
      return [...numbers.slice(index,), ...numbers.slice(0, index + 1)]
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: iteration
    * @param {number[]} numbers
    * @param {number} k
    * @return {number[]}
    */
   rotate(numbers, k) {
      const numberCopy = Array(numbers.length);

      for (let left = 0; left < numbers.length; left++) {
         const right = (left + k) % numbers.length;
         numberCopy[right] = numbers[left];
      }
      
      numbers = numberCopy;
      return numbers
   };
}


console.log(new Solution().rotate([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])
console.log(new Solution().rotate([1, 2, 3], 2), [2, 3, 1])
console.log(new Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3), [5, 6, 7, 1, 2, 3, 4])
console.log(new Solution().rotate([1, 2, 3, 4, 5, 6], 1), [6, 1, 2, 3, 4, 5])
console.log(new Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3), [5, 6, 7, 1, 2, 3, 4])
console.log(new Solution().rotate([-1, -100, 3, 99], 2), [3, 99, -1, -100])
console.log(new Solution().rotate([-1], 2), [-1])
console.log(new Solution().rotate([1, 2], 3), [2, 1])
console.log(new Solution().rotate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], 38), [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])