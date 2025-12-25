class Solution {
   /**
    * Time complexity: O(1)
    *     O(3**4)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     DS: list, string
    *     A: backtracking
    * @param {string} nums
    * @return {string[]}
    */
   restoreIpAddresses(nums) {
      if (
         nums.length < 4 ||
         nums.length > 12
      ) return []

      const ip = [];
      const ips = [];

      const backtrack = (index) => {
         if (
            index === nums.length &&
            ip.length === 4
         ) {
            ips.push(ip.join('.'));
            return
         } else if (
            index === nums.length ||
            ip.length == 4
         ) return

         // one digit number
         ip.push(nums[index]);
         backtrack(index + 1);
         ip.pop();

         // two digit number
         if (
            index + 1 < nums.length &&
            nums[index] > '0'
         ) {
            ip.push(nums.slice(index, index + 2))
            backtrack(index + 2);
            ip.pop();
         }

         // three digit number
         if (
            index + 2 < nums.length &&
            (
               nums[index] === '1' ||
               (nums[index] === '2' && nums[index + 1] < '5') ||
               (nums[index] === '2' && nums[index + 1] === '5' && nums[index + 2] <= '5')
            )
         ) {
            ip.push(nums.slice(index, index + 3))
            backtrack(index + 3);
            ip.pop();
         }
      }
      backtrack(0);
      return ips
   };
}


const restoreIpAddresses = new Solution().restoreIpAddresses;
console.log((new Solution().restoreIpAddresses('25525511135')).sort().toString() === (['255.255.11.135', '255.255.111.35']).sort().toString())
console.log((new Solution().restoreIpAddresses('0000')).sort().toString() === (['0.0.0.0']).sort().toString())
console.log((new Solution().restoreIpAddresses('101023')).sort().toString() === (['1.0.10.23', '1.0.102.3', '10.1.0.23', '10.10.2.3', '101.0.2.3']).sort().toString())
console.log((new Solution().restoreIpAddresses('000256')).sort().toString() === ([]).sort().toString())
console.log((new Solution().restoreIpAddresses('02852')).sort().toString() === (['0.2.8.52', '0.2.85.2', '0.28.5.2']).sort().toString())
