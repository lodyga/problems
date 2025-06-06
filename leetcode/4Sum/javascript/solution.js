class Solution {
   /**
    * Time complexity: O(n3)
    * Auxiliary space complexity: O(n)
    * Tags: two pointers
    * @param {number[]} numbers
    * @param {number} target
    * @return {}
    */
   fourSum(numbers, target) {
      numbers.sort((a, b) => a - b);
      const quadrupletList = [];

      for (let index1 = 0; index1 < numbers.length - 3; index1++) {
         if (numbers[index1 - 1] === numbers[index1])
            continue

         for (let index2 = index1 + 1; index2 < numbers.length - 2; index2++) {
            if (index2 > index1 + 1 && numbers[index2 - 1] === numbers[index2])
               continue

            let left = index2 + 1;
            let right = numbers.length - 1;

            while (left < right) {
               const quadruplet = (
                  numbers[index1] +
                  numbers[index2] +
                  numbers[left] +
                  numbers[right]
               )
               if (quadruplet === target) {
                  quadrupletList.push([
                     numbers[index1],
                     numbers[index2],
                     numbers[left],
                     numbers[right]]
                  )
                  left++;
                  right--;
                  while (left < right && numbers[left - 1] === numbers[left])
                     left++;
               } else if (quadruplet < target)
                  left++;
               else
                  right--;
            }
         }
      }
      return quadrupletList
   };
}
const fourSum = new Solution().fourSum;


console.log(new Solution().fourSum([1, 0, -1, 0, -2, 2], 0), [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])
console.log(new Solution().fourSum([2, 2, 2, 2, 2], 8), [[2, 2, 2, 2]])
console.log(new Solution().fourSum([0, 0, 0, 0], 0), [[0, 0, 0, 0]])
console.log(new Solution().fourSum([1, -2, -5, -4, -3, 3, 3, 5], -11), [[-5, -4, -3, 1]])