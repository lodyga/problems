class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: two pointers
    * @param {number[]} numbers
    * @param {number} target
    * @return {number}
    */
   countPairs(numbers, target) {
      numbers.sort((a, b) => a - b);
      let counter = 0;
      let left = 0;
      let right = numbers.length - 1;

      while (left < right) {
         if (numbers[left] + numbers[right] < target) {
            counter += right - left;
            left++;
         } else {
            right--;
         }
      }
      return  counter
   };
}

console.log(new Solution().countPairs([1, 1, 3, 4, 5], 6) == 5)
console.log(new Solution().countPairs([-1, 1, 2, 3, 1], 2) == 3)
console.log(new Solution().countPairs([-6, 2, 5, -2, -7, -1, 3], -2) == 10)
console.log(new Solution().countPairs([6, -1, 7, 4, 2, 3], 8) == 8)
console.log(new Solution().countPairs([-5, 0, -7, -1, 9, 8, -9, 9], -14) == 1)