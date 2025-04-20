class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * @param {string} passwords
    * @return {number}
    */
   longestPassword(passwords) {
      let passwordLength = 0;

      for (const password of passwords.split(' ')) {
         if (
            this.isAlnum(password) &&
            this.hasEvenLetters(password) &&
            this.hasOddDigits(password) &&
            password.length > passwordLength
         ) {
            passwordLength = password.length;
         }
      }
      return passwordLength
   };

   isAlnum(password) {
      return password.match(/\W/) === null
   };

   hasEvenLetters(password) {
      const passwordMatch = password.match(/[a-zA-Z]/ig);
      const numberOfLetters = passwordMatch === null ? 0 : passwordMatch.length;
      return numberOfLetters % 2 === 0
   };

   hasOddDigits(password) {
      const passwordMatch = password.match(/\d/g);
      const numberOfDigits = passwordMatch === null ? 0 : passwordMatch.length;
      return numberOfDigits % 2 === 1
   };
}


console.log(new Solution().longestPassword("test 5 a0A pass007 ?xy1"), 7)