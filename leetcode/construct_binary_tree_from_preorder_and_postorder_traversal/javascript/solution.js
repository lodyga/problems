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
    * Tags: binary tree, dfs, recursion, pre-order traversal, post-order traversal
    * @param {number[]} preorder
    * @param {number[]} postorder
    * @return {bt.TreeNode}
    */
   static constructFromPrePost(preorder, postorder) {
      if (preorder.length === 0)
         return null
      const node = new bt.TreeNode(preorder[0])
      if (preorder.length === 1)
         return node

      const value = preorder[1];
      const index = postorder.indexOf(value);
      const leftSubtreeSize = index + 1;
      node.left = constructFromPrePost(
         preorder.slice(1, 1 + leftSubtreeSize),
         postorder.slice(0, leftSubtreeSize)
      );
      if (preorder.length > 2) {
         node.right = constructFromPrePost(
            preorder.slice(1 + leftSubtreeSize,),
            postorder.slice(leftSubtreeSize, preorder.length - 1)
         );
      }
      return node
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, recursion, pre-order traversal, post-order traversal
    * @param {number[]} preorder
    * @param {number[]} postorder
    * @return {bt.TreeNode}
    */
   static constructFromPrePost(preorder, postorder) {
      const postorderIndex = new Map(postorder.map((value, index) => [value, index]));

      const dfs = (preStart, preEnd, postStart, postEnd) => {
         if (preStart > preEnd)
            return null
         const node = new bt.TreeNode(preorder[preStart]);
         if (preEnd === preStart)
            return node

         const value = preorder[preStart + 1];
         const index = postorder.indexOf(value);
         const leftSubtreeSize = index - postStart + 1;
         node.left = dfs(
            preStart + 1, preStart + leftSubtreeSize,
            postStart, postStart + leftSubtreeSize - 1
         );
         if (preEnd - preStart > 1) {
            node.right = dfs(
               preStart + 1 + leftSubtreeSize, preEnd,
               index + 1, postEnd - 1
            );
         }
         return node
      }
      return dfs(0, preorder.length - 1, 0, postorder.length - 1)
   };
}


// static method
const constructFromPrePost = Solution.constructFromPrePost;
console.log(bt.isSameTree(Solution.constructFromPrePost([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1]), bt.buildTree([1, 2, 3, 4, 5, 6, 7])))
console.log(bt.isSameTree(Solution.constructFromPrePost([1], [1]), bt.buildTree([1])))
console.log(bt.isSameTree(Solution.constructFromPrePost([2, 1], [1, 2]), bt.buildTree([2, 1])))
console.log(bt.isSameTree(Solution.constructFromPrePost([2, 1, 3], [3, 1, 2]), bt.buildTree([2, 1, null, 3])))
console.log(bt.isSameTree(Solution.constructFromPrePost([3, 9, 20, 15, 7], [9, 15, 7, 20, 3]), bt.buildTree([3, 9, 20, null, null, 15, 7])))