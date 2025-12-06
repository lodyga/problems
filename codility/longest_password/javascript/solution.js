class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * @param {string} passwords
    * @return {number}
    */
   longestPassword(passwords) {
      const hasEvenLetters = (word) => {
         let counter = 0;
         for (const char of word) {
            if (
               (char >= 'a' && char <= 'z') ||
               (char >= 'A' && char <= 'Z')
            ) counter++;
         }
         return counter % 2 === 0
      };

      const hasOddDigits = (word) => {
         let counter = 0;
         for (const char of word) {
            if (char >= '0' && char <= '9')
               counter++;
         }
         return counter % 2 === 1
      };

      const isAlnum = (word) => {
         let counter = 0;
         for (const char of word) {
            if (
               (char >= 'a' && char <= 'z') ||
               (char >= 'A' && char <= 'Z') ||
               (char >= '0' && char <= '9')
            ) counter++;
         }
         return counter === word.length
      };

      let passwordLength = -1;
      for (const password of passwords.split(' ')) {
         if (
            isAlnum(password) &&
            hasEvenLetters(password) &&
            hasOddDigits(password)
         ) {
            passwordLength = Math.max(passwordLength, password.length);
         }
      }
      return passwordLength
   };
}


const longestPassword = new Solution().longestPassword;
console.log(new Solution().longestPassword("test 5 a0A pass007 ?xy1") === 7);
