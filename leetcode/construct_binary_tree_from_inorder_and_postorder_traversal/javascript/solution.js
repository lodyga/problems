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
    * Tags: binary tree, dfs, recursion, in-order traversal, post-order traversal
    * @param {number[]} inorder
    * @param {number[]} postorder
    * @return {bt.TreeNode}
    */
   static buildTree(inorder, postorder) {
      if (
         postorder.length === 0 ||
         postorder.length === 1 && postorder[0] === null
      )
         return null

      const nodeValue = postorder[postorder.length - 1];
      const nodeIndex = inorder.indexOf(nodeValue);
      const node = new bt.TreeNode(nodeValue);
      node.left = buildTree(
         inorder.slice(0, nodeIndex),
         postorder.slice(0, nodeIndex));
      node.right = buildTree(
         inorder.slice(nodeIndex + 1,),
         postorder.slice(nodeIndex, postorder.length - 1));
      return node
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, recursion, in-order traversal, post-order traversal
    * @param {number[]} inorder
    * @param {number[]} postorder
    * @return {bt.TreeNode}
    */
   static buildTree(inorder, postorder) {
      const inorderIndex = new Map(inorder.map((value, index) => [value, index]));

      const dfs = (inStart, inEnd, postStart, postEnd) => {
         if (
            inStart > inEnd ||
            postStart > postEnd ||
            // Leetcode tests never have None in input.
            inStart === inEnd && postorder[inStart] === null
         )
            return null

         const nodeValue = postorder[postEnd];
         const nodeIndex = inorderIndex.get(nodeValue);
         const leftSubtreeSize = nodeIndex - inStart;
         const node = new bt.TreeNode(nodeValue);
         node.left = dfs(
            inStart, nodeIndex - 1,
            postStart, postStart + leftSubtreeSize - 1)
         node.right = dfs(
            nodeIndex + 1, inEnd,
            postStart + leftSubtreeSize, postEnd - 1)
         return node
      };
      return dfs(0, inorder.length - 1, 0, postorder.length - 1)
   };
}


// static method
const buildTree = Solution.buildTree;
console.log(bt.isSameTree(buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]), bt.buildTree([3, 9, 20, null, null, 15, 7])))
console.log(bt.isSameTree(buildTree([-1], [-1]), bt.buildTree([-1])))
console.log(bt.isSameTree(buildTree([], []), bt.buildTree([])))
console.log(bt.isSameTree(buildTree([null, 1, 3], [null, 3, 1]), bt.buildTree([1, null, 3])))