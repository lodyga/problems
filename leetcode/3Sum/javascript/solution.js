class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags: two pointers
    * @param {number[]} numbers
    * @return {number[][]}
    */
   threeSum(numbers) {
      numbers.sort((a, b) => a - b);
      const tripletList = [];

      for (let index = 0; index < numbers.length - 2; index++) {
         const number = numbers[index];

         // Skip positive numbers
         if (number > 0) {
            break
         } else if (index && number === numbers[index - 1]) {
            // Skip same number values
            continue
         }

         let left = index + 1;
         let right = numbers.length - 1;

         while (left < right) {
            const triplet = number + numbers[left] + numbers[right];

            if (triplet === 0) {
               tripletList.push([number, numbers[left], numbers[right]]);
               left++;
               right--;
               // skip same left pointer values
               while (
                  left < right &&
                  numbers[left] === numbers[left - 1]) {
                  left++;
               }
            } else if (triplet > 0) {
               right--;
            } else {
               left++;
            }
         }
      }
      return tripletList
   };
}


console.log(new Solution().threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
console.log(new Solution().threeSum([3, 0, -2, -1, 1, 2]), [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]])
console.log(new Solution().threeSum([1, 1, -2]), [[-2, 1, 1]])
console.log(new Solution().threeSum([-1, 1, 1]), [])
console.log(new Solution().threeSum([-2, 0, 0, 2, 2]), [[-2, 0, 2]])
console.log(new Solution().threeSum([0, 0, 0]), [[0, 0, 0]])