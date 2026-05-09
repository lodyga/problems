import { TreeNode, buildTree, getTreeValues, isSameTree } from '../../../../JS/binary-tree.js';
// import * as bt from '../../../../JS/binary-tree.js';


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
    * @return {TreeNode}
    */
   buildTreeFromPreIn(preorder, inorder) {
      if (
         preorder.length === 0 ||
         preorder.length === 1 && preorder[0] === null
      ) return null

      const val = preorder[0];
      const idx = inorder.indexOf(val);
      const node = new TreeNode(val);
      node.left = buildTreeFromPreIn(
         preorder.slice(1, idx + 1),
         inorder.slice(0, idx));
      node.right = buildTreeFromPreIn(
         preorder.slice(idx + 1,),
         inorder.slice(idx + 1,));
      return node
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: binary tree
    *     A: dfs, recursion, in-order traversal, pre-order traversal
    * @param {number[]} preorder
    * @param {number[]} inorder
    * @return {TreeNode}
    */
   buildTreeFromPreIn(preorder, inorder) {
      const inorderIndex = new Map(inorder.map((value, index) => [value, index]));

      const dfs = (preStart, preEnd, inStart, inEnd) => {
         if (
            preStart > preEnd ||
            inStart > inEnd ||
            // Leetcode tests never have None in input.
            preStart === preEnd && preorder[preStart] === null
         ) return null

         const val = preorder[preStart];
         const idx = inorderIndex.get(val);
         const leftSubtreeSize = idx - inStart;
         const node = new TreeNode(val);
         node.left = dfs(
            preStart + 1,
            preStart + leftSubtreeSize,
            inStart, idx - 1
         );
         node.right = dfs(
            preStart + 1 + leftSubtreeSize,
            preEnd,
            idx + 1,
            inEnd
         );
         return node
      };

      return dfs(0, preorder.length - 1, 0, inorder.length - 1)
   }
}


const buildTreeFromPreIn = new Solution().buildTreeFromPreIn;
console.log(isSameTree(buildTreeFromPreIn([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]), buildTree([3, 9, 20, null, null, 15, 7])))
console.log(isSameTree(buildTreeFromPreIn([-1], [-1]), buildTree([-1])))
console.log(isSameTree(buildTreeFromPreIn([], []), buildTree([])))
console.log(isSameTree(buildTreeFromPreIn([1, null, 3], [null, 1, 3]), buildTree([1, null, 3])))
