class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * @param {string[]}
    * @return {number}
    */
   numUniqueEmails(emials) {
      const cleanEmails = new Set();

      for (const emial of emials) {
         const [raw_name, domain] = emial.split('@');
         const name = [];

         for (const letter of raw_name) {

            if (letter === '.')
               continue
            else if (letter === '+')
               break
            else {
               name.push(letter);
            }
         }

         cleanEmails.add(name.join('') + '@' + domain);
      }
      return cleanEmails.size
   };
}
const numUniqueEmails = new Solution().numUniqueEmails;


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: regex
    * @param {string[]}
    * @return {number}
    */
   numUniqueEmails = function (emails) {
      const clean_emails = new Set();

      for (const email of emails) {
         let [name, domain] = email.split('@');

         // remove "." from the name
         name = name.replace(/\./g, '');

         // remove all after "+" in the name
         name = name.match(/(\w+)(\+?)/)[1]

         clean_emails.add(name + '@' + domain);
      }

      return clean_emails.size
   };
}
const numUniqueEmails = new Solution().numUniqueEmails;


console.log(new Solution().numUniqueEmails(['test.email+alex@leetcode.com', 'test.e.mail+bob.cathy@leetcode.com', 'testemail+david@lee.tcode.com']), 2)
console.log(new Solution().numUniqueEmails(['a@leetcode.com', 'b@leetcode.com', 'c@leetcode.com']), 3)