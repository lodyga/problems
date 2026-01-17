class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: iteration
    * @param {number} number
    * @return {boolean}
    */
   isPalindrome(number) {
      if (number < 0)
         return false

      let carry = number;
      let reversedNumber = 0;
      while (carry > 0) {
         reversedNumber = reversedNumber * 10 + carry % 10;
         carry = Math.floor(carry / 10)
      }
      return (number === reversedNumber)
   };
}


const isPalindrome = new Solution().isPalindrome;
console.log(new Solution().isPalindrome(121) === true)
console.log(new Solution().isPalindrome(-121) === false)
console.log(new Solution().isPalindrome(10) === false)
console.log(new Solution().isPalindrome(0) === true)