class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: string
    *     A: iteration
    * @param {string[]} sentence1
    * @param {string[]} sentence2
    * @param {string[][]} sentence2
    * @return {boolean}
    */
   areSentencesSimilar(sentence1, sentence2, similarPairs) {
      if (sentence1.length !== sentence2.length) {
         return false
      }

      const similarWord = new Map(similarPairs);

      for (let index = 0; index < sentence1.length; index++) {
         const word1 = sentence1[index];
         const word2 = sentence2[index];

         if (word1 === word2) {
            continue
         } else if (
            (similarWord.get(word1) === word2) ||
            (similarWord.get(word2) === word1)
         ) continue

         return false
      }

      return true
   };
}


const areSentencesSimilar = new Solution().areSentencesSimilar;
console.log(new Solution().areSentencesSimilar(['great', 'acting', 'skills'], ['fine', 'drama', 'talent'], [['great', 'fine'], ['drama', 'acting'], ['skills', 'talent']]) === true)
console.log(new Solution().areSentencesSimilar(['great'], ['great'], []) === true)
console.log(new Solution().areSentencesSimilar(['great'], ['doubleplus', 'good'], [['great', 'doubleplus']]) === false)
