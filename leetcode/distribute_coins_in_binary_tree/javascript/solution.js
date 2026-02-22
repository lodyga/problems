import { TreeNode, buildTree, getTreeValues } from '../../../../JS/binary-tree.js';


/**
 * class TreeNode {
 *    constructor(val = null, left = null, right = null) {
 *       this.val = val
 *       this.left = left
 *       this.right = right
 *    };
 * }
 */


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: binary tree
    *     A: dfs, recursion, post-order traversal
    * @param {TreeNode} root
    * @return {number}
    */
   distributeCoins(root) {
      let res = 0;

      const dfs = (node) => {
         if (node == null) {
            return 0
         }

         const left = dfs(node.left);
         const right = dfs(node.right);
         res += Math.abs(left) + Math.abs(right);
         return (node.val - 1) + left + right
      };

      dfs(root)
      return res
   };
}


const distributeCoins = new Solution().distributeCoins;
console.log(new Solution().distributeCoins(buildTree([1])) === 0)
console.log(new Solution().distributeCoins(buildTree([2, 0])) === 1)
console.log(new Solution().distributeCoins(buildTree([0, 2])) === 1)
console.log(new Solution().distributeCoins(buildTree([3, 0, 0])) === 2)
console.log(new Solution().distributeCoins(buildTree([0, 3, 0])) === 3)
console.log(new Solution().distributeCoins(buildTree([1, 0, 0, null, 3])) === 4)
console.log(new Solution().distributeCoins(buildTree([4, 0, 0, 0])) === 4)
