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
    *     A: dfs, recursion, pre-order traversal
    * @param {TreeNode} root 
    * @returns {number}
    */
   rob(root) {
      const dfs = (node) => {
         if (node === null) {
            return [0, 0]
         }
         const leftNode = dfs(node.left);
         const rightNode = dfs(node.right);
         const takeNode = node.val + leftNode[1] + rightNode[1];
         const skipNode = Math.max(...leftNode) + Math.max(...rightNode);
         return [takeNode, skipNode]
      }
      return Math.max(...dfs(root))
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: binary tree
    *     A: dfs, recursion, pre-order traversal
    * @param {TreeNode} root 
    * @returns {number}
    */
   rob(root) {
      const memo = new Map([[null, 0]]);

      const dfs = (node) => {
         if (memo.has(node)) {
            return memo.get(node)
         }
         // Skip node and `rob` chldren.
         const skip = dfs(node.left) + dfs(node.right);

         // Rob node but skip children layer.
         const leftGrand = node.left ? dfs(node.left.left) + dfs(node.left.right) : 0;
         const rightGrand = node.right ? dfs(node.right.left) + dfs(node.right.right) : 0;
         const take = node.val + leftGrand + rightGrand;
         memo.set(node, Math.max(take, skip));
         return memo.get(node)
      }
      return dfs(root)
   };
}


const rob = new Solution().rob;
console.log(new Solution().rob(buildTree([3, 2, 3, null, 3, null, 1])) === 7)
console.log(new Solution().rob(buildTree([3, 4, 5, 1, 3, null, 1])) === 9)
console.log(new Solution().rob(buildTree([4, 1, null, 2, null, 3])) === 7)
console.log(new Solution().rob(buildTree([79, 99, 77, null, null, null, 69, null, 60, 53, null, 73, 11, null, null, null, 62, 27, 62, null, null, 98, 50, null, null, 90, 48, 82, null, null, null, 55, 64, null, null, 73, 56, 6, 47, null, 93, null, null, 75, 44, 30, 82, null, null, null, null, null, null, 57, 36, 89, 42, null, null, 76, 10, null, null, null, null, null, 32, 4, 18, null, null, 1, 7, null, null, 42, 64, null, null, 39, 76, null, null, 6, null, 66, 8, 96, 91, 38, 38, null, null, null, null, 74, 42, null, null, null, 10, 40, 5, null, null, null, null, 28, 8, 24, 47, null, null, null, 17, 36, 50, 19, 63, 33, 89, null, null, null, null, null, null, null, null, 94, 72, null, null, 79, 25, null, null, 51, null, 70, 84, 43, null, 64, 35, null, null, null, null, 40, 78, null, null, 35, 42, 98, 96, null, null, 82, 26, null, null, null, null, 48, 91, null, null, 35, 93, 86, 42, null, null, null, null, 0, 61, null, null, 67, null, 53, 48, null, null, 82, 30, null, 97, null, null, null, 1, null, null])) === 3038)
