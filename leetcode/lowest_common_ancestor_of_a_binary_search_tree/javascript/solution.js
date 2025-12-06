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
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(logn)
    * Tags: 
    *     DS: binary tree
    *     A: dfs, recursion, pre-order traversal
    * @param {TreeNode} root
    * @param {TreeNode} p
    * @param {TreeNode} q
    * @return {TreeNode}
    */
   lowestCommonAncestor(root, p, q) {
      const dfs = (node) => {
         if (node === null) {
            return
         }
         else if (
            (p.val < node.val && node.val < q.val) ||
            (q.val < node.val && node.val < p.val)
         ) {
            return node
         }
         else if (
            node.val > p.val &&
            node.val > q.val
         ) {
            return dfs(node.left)
         }
         else if (
            node.val < p.val &&
            node.val < q.val
         ) {
            return dfs(node.right)
         } else {  // node in (p, q)
            return node
         }
      }
      return dfs(root)
   };

   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags: 
    *     DS: binary tree
    *     A: dfs, iteration, pre-order traversal
    * @param {TreeNode} root
    * @param {TreeNode} p
    * @param {TreeNode} q
    * @return {TreeNode}
    */
   lowestCommonAncestor(root, p, q) {
      let node = root;
      while (node) {
         if (
            node.val > p.val &&
            node.val > q.val
         ) {
            node = node.left
         } else if (
            node.val < p.val &&
            node.val < q.val
         ) {
            node = node.right
         } else {
            return node
         }
      }
   };
}


const lowestCommonAncestor = new Solution().lowestCommonAncestor;
console.log(getTreeValues(new Solution().lowestCommonAncestor(buildTree([2, 1]), buildTree([2]), buildTree([1])))[0] === 2)
console.log(getTreeValues(new Solution().lowestCommonAncestor(buildTree([6, 2, 8, 0, 4, 7, 9, null, null, 3, 5]), buildTree([2]), buildTree([8])))[0] === 6)
console.log(getTreeValues(new Solution().lowestCommonAncestor(buildTree([6, 2, 8, 0, 4, 7, 9, null, null, 3, 5]), buildTree([2]), buildTree([4])))[0] === 2)
console.log(getTreeValues(new Solution().lowestCommonAncestor(buildTree([6, 2, 8, 0, 4, 7, 9, null, null, 3, 5]), buildTree([3]), buildTree([5])))[0] === 4)
