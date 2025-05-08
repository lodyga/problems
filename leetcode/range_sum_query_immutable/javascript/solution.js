/**
 * Time complexity: 
 *    constructor: O(n)
 *    sumRange: O(1)
 * Auxiliary space complexity: O(n)
 * Tags: prefix sum
 */
class NumArray {
   constructor(numbers) {
      this.values = Array(numbers.length).fill(0);
      for (let index = 1; index <= numbers.length; index++) {
         this.values[index] = this.values[index - 1] + numbers[index - 1]
      }
   }

   /**
    * 
    * @param {number} left 
    * @param {number} right 
    * @returns {number}
    */
   sumRange(left, right) {
      return this.values[right + 1] - this.values[left]
   };
}


const numArray = new NumArray([-2, 0, 3, -5, 2, -1])
console.log(numArray.sumRange(0, 2))  // return (-2) + 0 + 3 = 1
console.log(numArray.sumRange(2, 5))  // return 3 + (-5) + 2 + (-1) = -1
console.log(numArray.sumRange(0, 5))  // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3