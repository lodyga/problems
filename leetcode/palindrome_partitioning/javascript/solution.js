class Solution {
   /**
    * Time complexity: O(n2^n)
    * Auxiliary space complexity: O(n)
    *     Output: O(2^n)
    * Tags:
    *     DS: list
    *     A: DFS with backtracking
    * @param {string} text
    * @return {string[][]}
    */
   partition(text) {
      const isPalindrome = (left, right) => {
         while (left < right) {
            if (text[left] !== text[right])
               return false
            left++;
            right--;
         }
         return true
      }

      const partition = [];
      const partitionList = [];

      const backtrack = (index) => {
         if (index === text.length) {
            partitionList.push(partition.slice());
            return
         }
         for (let right = index; right < text.length; right++) {
            if (isPalindrome(index, right)) {
               partition.push(text.slice(index, right + 1));
               backtrack(right + 1);
               partition.pop();
            }
         }
      }
      backtrack(0);
      return partitionList
   };
}


const partition = new Solution().partition;
console.log(new Solution().partition('aa'), [['a', 'a'], ['aa']])
console.log(new Solution().partition('a'), [['a']])
console.log(new Solution().partition('ab'), [['a', 'b']])
console.log(new Solution().partition('aaa'), [['a', 'a', 'a'], ['a', 'aa'], ['aa', 'a'], ['aaa']])
console.log(new Solution().partition('aab'), [['a', 'a', 'b'], ['aa', 'b']])
console.log(new Solution().partition('aba'), [['a', 'b', 'a'], ['aba']])
