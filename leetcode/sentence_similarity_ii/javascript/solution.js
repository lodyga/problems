class DSU {
   constructor(n, sentence) {
      this.size = Array(n).fill(1);
      this.parent = Array.from({ length: n }, (_, index) => index);
      this.word1Set = new Set(sentence);
      this.wordIndex = new Map();
      this.index = 0
   };

   _getIndex(word) {
      if (!this.wordIndex.has(word)) {
         this.wordIndex.set(word, this.index);
         this.index++;
      }

      return this.wordIndex[word]
   };

   find(u) {
      if (this.parent[u] !== u) {
         this.parent[u] = this.parent[this.parent[u]];
         u = this.parent[u];
      }

      return u
   }

   union(word1, word2) {
      const u = this._getIndex(word1);
      const v = this._getIndex(word2);
      let pu = this.find(u);
      let pv = this.find(v);

      if (pu === pv) {
         return
      } else if (this.word1Set.has(word1)) {
      } else if (
         this.size[pv] > this.size[pu] ||
         this.word1Set.has(word2)
      ) {
         [pu, pv] = [pv, pu];
      }

      this.size[pu] += this.size[pv];
      this.parent[pv] = this.parent[pu];
      return
   }
}

class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map, list, string
    *     A: DSU
    *     Model: graph
    * @param {string[]} sentence1
    * @param {string[]} sentence2
    * @param {string[][]} sentence2
    * @return {boolean}
    */
   areSentencesSimilarTwo(sentence1, sentence2, similarPairs) {
      if (sentence1.length !== sentence2.length) {
         return false
      }

      const dsu = new DSU(similarPairs.length * 2, sentence1);

      for (let index = 0; index < similarPairs.length; index++) {
         const word1 = similarPairs[index][0];
         const word2 = similarPairs[index][1];
         dsu.union(word1, word2);
      }

      for (let index = 0; index < similarPairs.length; index++) {
         const word1 = sentence1[index];
         const word2 = sentence2[index];

         if (word1 === word2) {
            continue
         } else if (
            !dsu.wordIndex.has(word1) ||
            !dsu.wordIndex.has(word2)
         ) {
            return false
         }

         const i1 = dsu.wordIndex[word1];
         const i2 = dsu.wordIndex[word2];

         if (dsu.parent[i1] !== dsu.parent[dsu.parent[i2]]) {
            return false
         }
      }

      return true
   };
}


const areSentencesSimilarTwo = new Solution().areSentencesSimilarTwo;
console.log(new Solution().areSentencesSimilarTwo(['great', 'acting', 'skills'], ['fine', 'drama', 'talent'], [['great', 'good'], ['fine', 'good'], ['drama', 'acting'], ['skills', 'talent']]) === true)
console.log(new Solution().areSentencesSimilarTwo(['I', 'love', 'leetcode'], ['I', 'love', 'onepiece'], [['manga', 'onepiece'], ['platform', 'anime'], ['leetcode', 'platform'], ['anime', 'manga']]) === true)
console.log(new Solution().areSentencesSimilarTwo(['I', 'love', 'leetcode'], ['I', 'love', 'onepiece'], [['manga', 'hunterXhunter'], ['platform', 'anime'], ['leetcode', 'platform'], ['anime', 'manga']]) === false)
