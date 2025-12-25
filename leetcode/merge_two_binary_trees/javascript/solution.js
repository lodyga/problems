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
    * @param {TreeNode} root1
    * @param {TreeNode} root2
    * @return {TreeNode}
    */
   mergeTrees(root1, root2) {
      const dfs = (node1, node2) => {
         if (node1 === null && node2 === null) {
            return null
         } else if (node1 === null || node2 === null) {
            return node1 || node2
         }
         const node = new TreeNode(node1.val + node2.val);
         node.left = dfs(node1.left, node2.left)
         node.right = dfs(node1.right, node2.right)
         return node
      }
      return dfs(root1, root2)
   };
}


const mergeTrees = new Solution().mergeTrees;
console.log(isSameTree(new Solution().mergeTrees(buildTree([1]), buildTree([1, 2])), buildTree([2, 2])))
console.log(isSameTree(new Solution().mergeTrees(buildTree([1, 3, 2, 5]), buildTree([2, 1, 3, null, 4, null, 7])), buildTree([3, 4, 5, 5, 4, null, 7])))
