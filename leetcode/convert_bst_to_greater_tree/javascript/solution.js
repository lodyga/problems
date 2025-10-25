// import { TreeNode, buildTree, getTreeValues, isSameTree } from '../../../../JS/binary-tree.js';
import * as bt from '../../../../JS/binary-tree.js';


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
    * Tags: binary tree
    * @param {bt.TreeNode} root
    * @return {bt.TreeNode}
    */
   convertBST(root) {
      let total = 0;

      const dfs = (node) => {
         if (!node)
            return

         dfs(node.right);
         node.val += total;
         total = node.val;
         dfs(node.left);
      }
      dfs(root);
      return root
   };
}


const convertBST = new Solution().convertBST;
console.log(bt.isSameTree(new Solution().convertBST(bt.buildTree([4, 1, 6, 0, 2, 5, 7, null, null, null, 3, null, null, null, 8])), bt.buildTree([30, 36, 21, 36, 35, 26, 15, null, null, null, 33, null, null, null, 8])))
console.log(bt.isSameTree(new Solution().convertBST(bt.buildTree([0, null, 1])), bt.buildTree([1, null, 1])))
console.log(bt.isSameTree(new Solution().convertBST(bt.buildTree([3, 2, 4, 1])), bt.buildTree([7, 9, 4, 10])))
console.log(bt.isSameTree(new Solution().convertBST(bt.buildTree([2, 0, 3, -4, 1])), bt.buildTree([5, 6, 3, 2, 6])))