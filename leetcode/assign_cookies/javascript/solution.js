class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: two pointers
    * @param {number[]} greedList
    * @param {number[]} cookies
    * @return {number}
    */
   findContentChildren(greedList, cookies) {
      greedList.sort((a, b) => a - b);
      let greedIndex = greedList.length - 1;
      cookies.sort((a, b) => a - b);
      let cookieIndex = cookies.length - 1;
      let contentCount = 0;

      while (
         greedIndex >= 0 &&
         cookieIndex >= 0
      ) {
         if (cookies[cookieIndex] >= greedList[greedIndex]) {
            contentCount++;
            cookieIndex--;
         }
         greedIndex--;
      }
      return contentCount
   };
}
const findContentChildren = new Solution().findContentChildren;


console.log(new Solution().findContentChildren([1, 2, 3], [1, 1]), 1)
console.log(new Solution().findContentChildren([1, 2], [1, 2, 3]), 2)
console.log(new Solution().findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]), 2)