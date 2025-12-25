import { TreeNode, buildTree, getTreeValues, isSameTree } from '../../../../JS/binary-tree.js';


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
    * @param {number} val
    * @return {TreeNode}
    */
   insertIntoBST(root, val) {
      const dfs = (node) => {
         if (node === null) {
            node = new TreeNode(val)
         } else if (node.val < val) {
            node.right = dfs(node.right);
         } else {
            node.left = dfs(node.left);
         }
         return node
      }
      return dfs(root)
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     DS: binary tree
    *     A: dfs, iteration, pre-order traversal
    * @param {TreeNode} root
    * @param {number} val
    * @return {TreeNode}
    */
   insertIntoBST2(root, val) {
      let node = root;
      while (node) {
         if (node.val < val) {
            if (node.right) {
               node = node.right;
            } else {
               node.right = new TreeNode(val);
               return root
            }
         } else {
            if (node.left) {
               node = node.left;
            } else {
               node.left = new TreeNode(val);
               return root
            }
         }
      }
      return new TreeNode(val)
   };
}


const insertIntoBST = new Solution().insertIntoBST;
console.log(isSameTree(new Solution().insertIntoBST(buildTree([5]), 6), buildTree([5, null, 6])))
console.log(isSameTree(new Solution().insertIntoBST(buildTree([]), 5), buildTree([5])))
console.log(isSameTree(new Solution().insertIntoBST(buildTree([4, 2, 7, 1, 3]), 5), buildTree([4, 2, 7, 1, 3, 5])))
console.log(isSameTree(new Solution().insertIntoBST(buildTree([40, 20, 60, 10, 30, 50, 70]), 25), buildTree([40, 20, 60, 10, 30, 50, 70, null, null, 25])))
console.log(isSameTree(new Solution().insertIntoBST(buildTree([4, 2, 7, 1, 3, null, null, null, null, null, null]), 5), buildTree([4, 2, 7, 1, 3, 5])))
