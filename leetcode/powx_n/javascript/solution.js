class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(logn)
    * Tags: recursion
    * @param {number} x
    * @param {number} n
    * @return {number}
    */
   myPow(x, n) {
      if (n === 0)
         return 1
      else if (n < 0)
         return 1 / this.myPow(x, -n)
      else {
         const base = this.myPow(x, Math.floor(n / 2));
         return base * base * (n & 1 === 1 ? x : 1)
      }
   };
}


const myPow = new Solution().myPow;
console.log(new Solution().myPow(2, 10), 1024)
console.log(new Solution().myPow(2.1, 3), 9.261)
console.log(new Solution().myPow(2, -2), 0.25)
console.log(new Solution().myPow(2, -200000000), 0)
console.log(new Solution().myPow(0.00001, 2147483647), 0)
console.log(new Solution().myPow(2.00000, -2147483648), 0)