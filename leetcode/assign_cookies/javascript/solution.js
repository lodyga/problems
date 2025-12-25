class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *    A: two pointers
    * @param {number[]} greedList
    * @param {number[]} cookies
    * @return {number}
    */
   findContentChildren(greedList, cookies) {
      greedList.sort((a, b) => a - b);
      cookies.sort((a, b) => a - b);
      let greedI = 0;
      let cookieI = 0;
      let counter = 0;

      while (
         greedI < greedList.length &&
         cookieI < cookies.length
      ) {
         const greed = greedList[greedI];
         const cookie = cookies[cookieI];
         
         if (greed <= cookie) {
            counter++;
            greedI++;
         }
         cookieI++;
      }
      return counter
   };
}


const findContentChildren = new Solution().findContentChildren;
console.log(new Solution().findContentChildren([1, 2, 3], [1, 1]) === 1)
console.log(new Solution().findContentChildren([1, 2], [1, 2, 3]) === 2)
console.log(new Solution().findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]) === 2)
