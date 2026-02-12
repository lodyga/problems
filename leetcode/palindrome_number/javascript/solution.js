class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     iteration
    * @param {number} num
    * @return {boolean}
    */
   isPalindrome(num) {
      if (num < 0)
         return false

      let carry = num;
      let revNum = 0;
     
      while (carry > 0) {
         revNum = revNum * 10 + carry % 10;
         carry = Math.floor(carry / 10);
      }
      
      return num === revNum
   };
}


const isPalindrome = new Solution().isPalindrome;
console.log(new Solution().isPalindrome(121) === true)
console.log(new Solution().isPalindrome(-121) === false)
console.log(new Solution().isPalindrome(10) === false)
console.log(new Solution().isPalindrome(0) === true)
