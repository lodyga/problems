class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array
    *     A: iteration
    * @param {number[]} nums
    * @return {number[]}
    */
   getConcatenation(nums) {
      const res = Array(nums.length * 2).fill(0);

      for (let idx = 0; idx < nums.length; idx++) {
         res[idx] = nums[idx];
         res[idx + nums.length] = nums[idx];
      }
    
      return res;
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array
    *     A: built-in function
    * @param {number[]} nums
    * @return {number[]}
    */
   getConcatenation(nums) {
      return [...nums, ...nums];
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: array
    *     A: built-in function
    * @param {number[]} nums
    * @return {number[]}
    */
   getConcatenation(nums) {
      nums.push(...nums.slice())
      return nums;
   }
}


const getConcatenation = new Solution().getConcatenation;
console.log(new Solution().getConcatenation([1, 2, 1]))
console.log(JSON.stringify(new Solution().getConcatenation([1, 2, 1])) === JSON.stringify([1, 2, 1, 1, 2, 1]))
console.log(JSON.stringify(new Solution().getConcatenation([1, 3, 2, 1])) === JSON.stringify([1, 3, 2, 1, 1, 3, 2, 1]))
