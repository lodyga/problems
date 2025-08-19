class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: iteration
    * @param {number[]} numbers
    * @return {number}
    */
   maxTurbulenceSize(numbers) {
      let prevNumber = numbers[0];
      let turbSize = 1;
      let maxTurbSize = 1;
      let assumeNextLess = true;
      let assumenextGreater = true;

      for (const number of numbers.slice(1,)) {
         if (prevNumber < number) {
            turbSize = assumenextGreater ? turbSize + 1 : 2;
            assumeNextLess = true;
            assumenextGreater = false;
         } else if (prevNumber > number) {
            turbSize = assumeNextLess ? turbSize + 1 : 2;
            assumeNextLess = false;
            assumenextGreater = true;
         } else {
            turbSize = 1;
            assumeNextLess = true;
            assumenextGreater = true;
         }
         prevNumber = number;
         maxTurbSize = Math.max(maxTurbSize, turbSize);
      }
      return maxTurbSize
   };
}
const maxTurbulenceSize = new Solution().maxTurbulenceSize;


console.log(new Solution().maxTurbulenceSize([3, 8, 4]), 3)
console.log(new Solution().maxTurbulenceSize([8, 3, 9]), 3)
console.log(new Solution().maxTurbulenceSize([1, 3, 8, 4]), 3)
console.log(new Solution().maxTurbulenceSize([9, 8, 3, 9]), 3)
console.log(new Solution().maxTurbulenceSize([3, 3]), 1)
console.log(new Solution().maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]), 5)
console.log(new Solution().maxTurbulenceSize([4, 8, 12, 16]), 2)
console.log(new Solution().maxTurbulenceSize([100]), 1)