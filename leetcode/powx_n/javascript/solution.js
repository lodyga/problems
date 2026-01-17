class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(logn)
    * Tags:
    *     A: recursion
    * @param {number} x
    * @param {number} n
    * @return {number}
    */
   static myPow(x, n) {
      if (n === 0) {
         return 1
      } else if (n === 1) {
         return x
      } else if (n < 0)
         return 1 / myPow(x, -n)
      else {  // n > 1
         const base = myPow(x, Math.floor(n / 2));
         return base * base * (n % 2 ? x : 1)
      }
   };
}


const myPow = Solution.myPow;
console.log(myPow(2, 10) === 1024)
console.log(myPow(2, 3) === 8)
console.log(myPow(2, -2) === 0.25)
console.log(myPow(2, -200000000) === 0)
console.log(myPow(0.00001, 2147483647) === 0)
console.log(myPow(2.00000, -2147483648) === 0)
console.log(myPow(0.44528, 0) === 1)
