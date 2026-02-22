class Solution {
   /**
    * Time complexity: O(1)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: math, iteration
    *     Arithmetic series
    * @param {number} days
    * @return {number}
    */
   totalMoney(days) {
      const weeks = Math.floor(days / 7);
      const lastWeekDays = days % 7;
      let wholeWeeksMoneySum = 0;

      for (let week = 1; week < weeks + 1; week++)
         wholeWeeksMoneySum += (week + (week - 1 + 7)) * 7 / 2;

      const lastWeekMoneySum = (
         (weeks + 1) +
         (weeks + lastWeekDays)
      ) * lastWeekDays / 2

      return wholeWeeksMoneySum + lastWeekMoneySum
   };
}


const totalMoney = new Solution().totalMoney;
console.log(new Solution().totalMoney(4) === 10);
console.log(new Solution().totalMoney(10) === 37);
console.log(new Solution().totalMoney(20) === 96);
