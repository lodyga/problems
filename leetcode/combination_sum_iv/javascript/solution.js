class Solution {
   /**
    * Time complexity: O(n*t)
    *     n: numbers length
    *     t: target
    * Auxiliary space complexity: O(t)
    * Tags:
    *     DS: array
    *     A: top-down
    * @param {number[]} nums
    * @param {number} target
    * @return {number}
    */
   combinationSum4(nums, target) {
      const dfs = (total) => {
         if (total > target) {
            return 0;
         }
         else if (memo[total] !== -1) {
            return memo[total];
         }

         memo[total] = 0;

         for (const num of nums) {
            memo[total] += dfs(total + num)
         }

         //memo[total] = (
         //   nums
         //      .map(num => dfs(total + num))
         //      .reduce((total, value) => total + value, 0)
         //)

         return memo[total];
      };

      const memo = Array(target).fill(-1);
      memo.push(1);
      return dfs(0);
   }
}


class Solution {
   /**
    * Time complexity: O(n*t)
    *     n: numbers length
    *     t: target
    * Auxiliary space complexity: O(t)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {number[]} nums
    * @param {number} target
    * @return {number}
    */
   combinationSum4(nums, target) {
      const cache = Array(target + 1).fill(0);
      cache[target] = 1;

      for (let idx = target - 1; idx > -1; idx--) {
         for (const num of nums) {
            if (idx + num <= target) {
               cache[idx] += cache[idx + num]
            }
         }
      }

      return cache[0];
   }
}


const combinationSum4 = new Solution().combinationSum4;
console.log(new Solution().combinationSum4([10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500,510,520,530,540,550,560,570,580,590,600,610,620,630,640,650,660,670,680,690,700,710,720,730,740,750,760,770,780,790,800,810,820,830,840,850,860,870,880,890,900,910,920,930,940,950,960,970,980,990,111], 999) === 1)
console.log(new Solution().combinationSum4([5], 5) === 1)
console.log(new Solution().combinationSum4([2, 3], 7) === 3)
console.log(new Solution().combinationSum4([1, 2, 3], 4) === 7)
console.log(new Solution().combinationSum4([9], 3) === 0)
console.log(new Solution().combinationSum4([4, 2, 1], 32) === 39882198)
