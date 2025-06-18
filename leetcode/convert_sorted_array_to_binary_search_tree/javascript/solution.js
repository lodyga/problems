class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, recursion
    * @param {number[]} numbers
    * @return {TreeNode}
    */
   sortedArrayToBST(numbers) {
      function dfs(left, right) {
         if (left > right) {
            return null
         }
         const middle = (left + right) >> 1;

         let node = new TreeNode(numbers[middle]);
         node.left = dfs(left, middle - 1);
         node.right = dfs(middle + 1, right);

         return node
      }
      return getTreeValues(dfs(0, numbers.length - 1))
   };
}
const sortedArrayToBST = new Solution().sortedArrayToBST;


console.log(new Solution().sortedArrayToBST([5]), [5])
console.log(new Solution().sortedArrayToBST([1, 3]), [1, null, 3])
console.log(new Solution().sortedArrayToBST([-10, -3, 0, 5, 9]), [0, -10, 5, null, -3, null, 9])