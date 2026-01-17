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
      const combinationList = [];
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

      const backtrack = (index) => {
         if (index === digits.length) {
            combinationList.push(combination.join(''));
            return
         }

         const digit = digits[index];
         for (const letter of digitToLetter.get(digit)) {
            combination.push(letter);
            backtrack(index + 1);
            combination.pop();
         }
      }
      backtrack(0);
      return combinationList
   };
}


const letterCombinations = new Solution().letterCombinations;
print(Solution().letterCombinations('2') == ['a', 'b', 'c'])
print(Solution().letterCombinations('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])
