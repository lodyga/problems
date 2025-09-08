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
    * Tags: binary tree, recursion
    * @param {TreeNode} root
    * @param {TreeNode} p
    * @param {TreeNode} p
    * @return {TreeNode}
    */
   lowestCommonAncestor(root, p, q) {
      if (p.val < root.val && q.val < root.val) {
         return lowestCommonAncestor(root.left, p, q)
      } else if (p.val > root.val && q.val > root.val) {
         return lowestCommonAncestor(root.right, p, q)
      } else {
         return root
      }
   };
}


class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags: binary tree, iteration
    * @param {TreeNode} root
    * @param {TreeNode} p
    * @param {TreeNode} p
    * @return {TreeNode}
    */
   lowestCommonAncestor(root, p, q) {
      let node = root;
      while (node) {
         if (p.val < node.val && q.val < node.val) {
            node = node.left   
         } else if (p.val > node.val && q.val > node.val) {
            node = node.right
         } else {
            return node
         }
      }
   };
}
const lowestCommonAncestor = new Solution().lowestCommonAncestor;


console.log((new Solution().lowestCommonAncestor(buildTree([2, 1]), buildTree([2]), buildTree([1]))).val,  2)
console.log((new Solution().lowestCommonAncestor(buildTree([6, 2, 8, 0, 4, 7, 9, null, null, 3, 5]), buildTree([2]), buildTree([8]))).val, 6)
console.log((new Solution().lowestCommonAncestor(buildTree([6, 2, 8, 0, 4, 7, 9, null, null, 3, 5]), buildTree([2]), buildTree([4]))).val, 2)
console.log((new Solution().lowestCommonAncestor(buildTree([6, 2, 8, 0, 4, 7, 9, null, null, 3, 5]), buildTree([3]), buildTree([5]))).val, 4)