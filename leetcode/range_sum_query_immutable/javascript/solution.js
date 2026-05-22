/**
 * Time complexity: 
 *     constructor: O(n)
 *     sumRange: O(1)
 * Auxiliary space complexity: O(n)
 * Tags:
 *     DS: list
 *     A: prefix sum
 */
class NumArray {
   constructor(nums) {
      this.prefixSum = [0];
      for (const num of nums)
         this.prefixSum.push(this.prefixSum[this.prefixSum.length - 1] + num);
   }

   /**
    * @param {number} left 
    * @param {number} right 
    * @returns {number}
    */
   sumRange(left, right) {
      return this.prefixSum[right + 1] - this.prefixSum[left];
   }
}


const numArray = new NumArray([-2, 0, 3, -5, 2, -1])
console.log(numArray.sumRange(0, 2))  // return (-2) + 0 + 3 = 1
console.log(numArray.sumRange(2, 5))  // return 3 + (-5) + 2 + (-1) = -1
console.log(numArray.sumRange(0, 5))  // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
