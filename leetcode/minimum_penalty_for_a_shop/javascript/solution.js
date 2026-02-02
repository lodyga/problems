class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy, prefix sum
    * @param {string} customers
    * @return {number}
    */
   bestClosingTime(customers) {
      // 'Y' postfix sum - 'N' prefix sum
      let penalty = customers.split('').filter(val => val === 'Y').length;
      let minPenalty = penalty;
      let closingHour = 0

      for (let hour = 0; hour < customers.length; hour++) {
         const customer = customers[hour];
         penalty += customer === 'Y' ? -1 : 1;

         if (penalty < minPenalty) {
            minPenalty = penalty;;
            closingHour = hour + 1;
         }
      }

      return closingHour
   };
}


const bestClosingTime = new Solution().bestClosingTime;
console.log(new Solution().bestClosingTime('YYNY') === 2)
console.log(new Solution().bestClosingTime('NNNNN') === 0)
console.log(new Solution().bestClosingTime('YYYY') === 4)
