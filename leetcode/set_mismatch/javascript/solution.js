class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: bit manipulation, negative marking
    * @param {number[]} nums
    * @return {number[]}
    */
   findErrorNums(nums) {
      let res = [];
      const numsCopy = nums.slice();

      // Find duplicate value.
      for (let num of nums) {
         if (numsCopy[Math.abs(num) - 1] < 0) {
            res.push(num);
            break
         }

         numsCopy[num - 1] *= -1;
      }

      // Find missing value.
      let xor = res[0];

      for (let index = 0; index < nums.length; index++) {
         xor ^= (index + 1) ^ nums[index];
      }

      res.push(xor)
      return res
   };

   /**
    * """
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash set
    * @param {number[]} nums
    * @return {number[]}
    */
   findErrorNums(nums) {
      const numSet = new Set();
      let duplicate;
      
      for (const number of nums) {
         if (numSet.has(number))
            duplicate = number;
         else
            numSet.add(number);
      }

      let missing;
      for (let number = 1; number <= nums.length; number++) {
         if (!numSet.has(number)) {
            missing = number
            break
         }
      }

      return [duplicate, missing]
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map
    * @param {number[]} nums
    * @return {number[]}
    */
   findErrorNums(nums) {
      const numFreq = new Map(nums.map((_, index) => [index + 1, 0]));

      for (const number of nums) {
         numFreq.set(number, (numFreq.get(number) || 0) + 1);
      }
      
      let duplicate;
      let missing;
      
      for (const [number, frequency] of numFreq.entries()) {
         if (frequency === 0) {
            missing = number
         } else if (frequency === 2) {
            duplicate = number
         }
      }
      return [duplicate, missing]
   };
}


const findErrorNums = new Solution().findErrorNums;
console.log(new Solution().findErrorNums([1, 2, 2, 4]).toString() == [2, 3].toString())
console.log(new Solution().findErrorNums([1, 1]).toString() == [1, 2].toString())
console.log(new Solution().findErrorNums([2, 2]).toString() == [2, 1].toString())
console.log(new Solution().findErrorNums([2, 3, 2]).toString() == [2, 1].toString())
