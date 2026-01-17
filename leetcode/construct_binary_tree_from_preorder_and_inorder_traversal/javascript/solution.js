// import { TreeNode, bt.buildTree, getTreeValues, isSameTree } from '../../../../JS/binary-tree.js';
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
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: binary tree
    *     A: dfs, recursion, in-order traversal, pre-order traversal
    * @param {number[]} preorder
    * @param {number[]} inorder
    * @return {bt.TreeNode}
    */
   static buildTree(preorder, inorder) {
      if (
         preorder.length === 0 ||
         preorder.length === 1 && preorder[0] === null
      )
         return null

      const nodeValue = preorder[0];
      const nodeIndex = inorder.indexOf(nodeValue);
      const node = new bt.TreeNode(nodeValue);
      node.left = buildTree(
         preorder.slice(1, nodeIndex + 1), 
         inorder.slice(0, nodeIndex));
      node.right = buildTree(
         preorder.slice(nodeIndex + 1,), 
         inorder.slice(nodeIndex + 1,));
      return node
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: binary tree
    *     A: dfs, recursion, in-order traversal, pre-order traversal
    * @param {number[]} preorder
    * @param {number[]} inorder
    * @return {bt.TreeNode}
    */
   static buildTree(preorder, inorder) {
      const inorderIndex = new Map(inorder.map((value, index) => [value, index]));

      const dfs = (preStart, preEnd, inStart, inEnd) => {
         if (
            preStart > preEnd ||
            inStart > inEnd ||
            // Leetcode tests never have None in input.
            preStart === preEnd && preorder[preStart] === null
         )
            return null

         const nodeValue = preorder[preStart];
         const nodeIndex = inorderIndex.get(nodeValue);
         const leftSubtreeSize = nodeIndex - inStart;
         const node = new bt.TreeNode(nodeValue);
         node.left = dfs(
            preStart + 1, preStart + leftSubtreeSize,
            inStart, nodeIndex - 1)
         node.right = dfs(
            preStart + 1 + leftSubtreeSize, preEnd,
            nodeIndex + 1, inEnd)
         return node
      };
      return dfs(0, preorder.length - 1, 0, inorder.length - 1)
   };
}


// static method
const buildTree = Solution.buildTree;
console.log(bt.isSameTree(buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]), bt.buildTree([3, 9, 20, null, null, 15, 7])))
console.log(bt.isSameTree(buildTree([-1], [-1]), bt.buildTree([-1])))
console.log(bt.isSameTree(buildTree([], []), bt.buildTree([])))
console.log(bt.isSameTree(buildTree([1, null, 3], [null, 1, 3]), bt.buildTree([1, null, 3])))
