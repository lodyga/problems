import { TreeNode, buildTree, getTreeValues, isSameTree } from '../../../../JS/binary-tree.js';
// import * as from '../../../../JS/binary-tree.js';


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
    *     A: dfs, recursion, in-order traversal
    * @param {TreeNode} root
    * @return {TreeNode}
    */
   convertBST(root) {
      let total = 0;

      const dfs = (node) => {
         if (node === null)
            return null

         dfs(node.right);
         node.val += total;
         total = node.val;
         dfs(node.left);
         return node
      }
      return dfs(root);
   };
}


const convertBST = new Solution().convertBST;
console.log(isSameTree(new Solution().convertBST(buildTree([4, 1, 6, 0, 2, 5, 7, null, null, null, 3, null, null, null, 8])), buildTree([30, 36, 21, 36, 35, 26, 15, null, null, null, 33, null, null, null, 8])))
console.log(isSameTree(new Solution().convertBST(buildTree([0, null, 1])), buildTree([1, null, 1])))
console.log(isSameTree(new Solution().convertBST(buildTree([3, 2, 4, 1])), buildTree([7, 9, 4, 10])))
console.log(isSameTree(new Solution().convertBST(buildTree([2, 0, 3, -4, 1])), buildTree([5, 6, 3, 2, 6])))
