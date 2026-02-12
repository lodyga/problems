class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy, two pointers, in-place
    * @param {number[]} nums
    * @return {}
    */
   nextPermutation(nums) {
      const N = nums.length;
      
      // Step 1: find pivot
      let pivot = N - 2;
      while (
         pivot > -1 &&
         nums[pivot] >= nums[pivot + 1]
      ) {
         pivot--;
      }

      // Step 2: find rightmost successor
      if (pivot > -1) {
         let index = N - 1;
         
         while (nums[pivot] >= nums[index]) {
            index--;
         }
         [nums[pivot], nums[index]] = [nums[index], nums[pivot]];
      }

      // Step 3: reverse the suffix
      let left = pivot + 1;
      let right = N - 1;

      while (left < right) {
         [nums[left], nums[right]] = [nums[right], nums[left]];
         left++;
         right--;
      }

      return nums
   };
}


const nextPermutation = new Solution().nextPermutation;
console.log(new Solution().nextPermutation([1, 2, 3, 6, 5, 4]))
console.log(new Solution().nextPermutation([1, 2, 3, 6, 5, 4]).toString() === [1, 2, 4, 3, 5, 6].toString())
console.log(new Solution().nextPermutation([1, 2, 3]).toString() === [1, 3, 2].toString())
console.log(new Solution().nextPermutation([3, 2, 1]).toString() === [1, 2, 3].toString())
console.log(new Solution().nextPermutation([1, 1, 5]).toString() === [1, 5, 1].toString())
console.log(new Solution().nextPermutation([1, 2, 3, 4]).toString() === [1, 2, 4, 3].toString())
console.log(new Solution().nextPermutation([1, 3, 2, 4]).toString() === [1, 3, 4, 2].toString())
console.log(new Solution().nextPermutation([1, 2, 4, 3]).toString() === [1, 3, 2, 4].toString())
console.log(new Solution().nextPermutation([4, 3, 2, 1]).toString() === [1, 2, 3, 4].toString())
console.log(new Solution().nextPermutation([1, 4, 3, 2]).toString() === [2, 1, 3, 4].toString())
console.log(new Solution().nextPermutation([1, 3, 4, 2]).toString() === [1, 4, 2, 3].toString())
