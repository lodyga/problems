class Solution {
   /**
    * Time complexity: O(nlogn)
    *     n: product list length
    *     s: search word length
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: two pointers, sorting
    * @param {string[]} products
    * @param {string} searchWord
    * @return {string[][]}
    */
   suggestedProducts(products, searchWord) {
      products.sort();
      const res = [];
      let left = 0;
      let right = products.length - 1;

      for (let index = 0; index < searchWord.length; index++) {
         const searchLetter = searchWord[index];

         while (
            (left <= right) &&
            (
               (products[left].length <= index) ||
               searchLetter !== products[left][index]
            )
         ) left++;

         while (
            (left <= right) &&
            (
               products[right].length <= index ||
               searchLetter !== products[right][index]
            )
         ) right--;

         res.push(products.slice(left, Math.min(left + 3, right + 1)));
      }

      return res
   };
}


const suggestedProducts = new Solution().suggestedProducts;
console.log(new Solution().suggestedProducts(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse").toString() === [["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "monitor"], ["mouse", "mousepad"], ["mouse", "mousepad"], ["mouse", "mousepad"]].toString())
console.log(new Solution().suggestedProducts(["havana"], "havana").toString() === [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]].toString())
console.log(new Solution().suggestedProducts(["havana"], "tatiana").toString() === [[], [], [], [], [], [], []].toString())
