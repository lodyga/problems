class Solution {
   /**
    * Time complexity: O(1)
    *     The recursion tree is bounded by 3**4 and validation within each call is O(1).
    * Auxiliary space complexity: O(1)
    * Tags: backtracking
    * @param {string} numbers
    * @return {string[]}
    */
   restoreIpAddresses(numbers) {
      if (
         numbers.length < 4 ||
         numbers.length > 12
      ) return []

      const ip = [];
      const ipList = [];
      dfs(0);
      return ipList

      function dfs(index) {
         if (
            index === numbers.length &&
            ip.length === 4
         ) {
            ipList.push(ip.join('.'));
            return
         } else if (
            index === numbers.length ||
            ip.length >= 4
         ) return

         // one digit number
         ip.push(numbers[index]);
         dfs(index + 1);
         ip.pop();

         // two digit number
         if (
            index + 1 < numbers.length &&
            numbers[index] > '0'
         ) {
            ip.push(numbers.slice(index, index + 2))
            dfs(index + 2);
            ip.pop();
         }

         // three digit number
         if (
            index + 2 < numbers.length &&
            (
               (numbers[index] === '1') ||
               (numbers[index] === '2' && numbers[index + 1] < '5') ||
               (numbers[index] === '2' && numbers[index + 1] === '5' && numbers[index + 2] <= '5')
            )
         ) {
            ip.push(numbers.slice(index, index + 3))
            dfs(index + 3);
            ip.pop();
         }
      }
   };
}
const restoreIpAddresses = new Solution().restoreIpAddresses;


console.log(new Solution().restoreIpAddresses('25525511135'), ['255.255.11.135', '255.255.111.35'])
console.log(new Solution().restoreIpAddresses('0000'), ['0.0.0.0'])
console.log(new Solution().restoreIpAddresses('101023'), ['1.0.10.23', '1.0.102.3', '10.1.0.23', '10.10.2.3', '101.0.2.3'])
console.log(new Solution().restoreIpAddresses('000256'), [])
console.log(new Solution().restoreIpAddresses('02852'), ['0.2.8.52', '0.2.85.2', '0.28.5.2'])