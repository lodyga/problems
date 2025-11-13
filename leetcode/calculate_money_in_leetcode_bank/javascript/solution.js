class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(1)
    * Tags: iteration
    * @param {number} days
    * @return {number}
    */
   totalMoney(days) {
      const weeks = parseInt(days / 7);
      const left = days % 7;
      let total = 0;

      for (let week = 0; week < weeks; week++)
         total += ((1 + 7 + 2 * week) * 7 / 2)
      
      const lastWeek = weeks + 1;
      total += (lastWeek + (lastWeek + left - 1)) * left / 2

      return total
   };
}


const totalMoney = new Solution().totalMoney;
console.log(new Solution().totalMoney(4) === 10);
console.log(new Solution().totalMoney(10) === 37);
console.log(new Solution().totalMoney(20) === 96);
