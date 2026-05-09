class Solution {
   /**
    * Time complexity: O(n4^n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: list
    *     A: DFS with backtracking
    * @param {string} digits
    * @return {string[]}
    */
   letterCombinations(digits) {
      const combination = [];
      const res = [];
      const digitToLetter = new Map([
         ['2', 'abc'],
         ['3', 'def'],
         ['4', 'ghi'],
         ['5', 'jkl'],
         ['6', 'mno'],
         ['7', 'pqrs'],
         ['8', 'tuv'],
         ['9', 'wxyz']
      ]);

      const backtrack = (idx) => {
         if (idx === digits.length) {
            res.push(combination.join(''));
            return
         }

         for (const letter of digitToLetter.get(digits[idx])) {
            combination.push(letter);
            backtrack(idx + 1);
            combination.pop();
         }
      }

      backtrack(0);
      return res
   }
}


const letterCombinations = new Solution().letterCombinations;
console.log(new Solution().letterCombinations('2').toString() === ['a', 'b', 'c'].toString())
console.log(new Solution().letterCombinations('23').toString() === ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'].toString())
