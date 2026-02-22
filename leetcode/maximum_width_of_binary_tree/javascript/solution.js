import { TreeNode, buildTree, getTreeValues } from '../../../../JS/binary-tree.js';
import { Deque } from '@datastructures-js/deque';


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
    *     DS: binary tree, deque
    *     A: bfs, iteration, level-order traversal
    * @param {TreeNode} root
    * @return {number}
    */
   widthOfBinaryTree(root) {
      let maxWidth = 1n;

      const bfs = (node) => {
         // deaue([[node, node index], ])
         const deq = new Deque([[node, 0n]]);

         while (deq.size()) {
            const queueSize = deq.size();
            let right = 0n;
            let left = 0n;

            for (let index = 0; index < queueSize; index++) {
               const [node, nodeId] = deq.popFront();

               if (index === 0) {
                  left = nodeId;
               }
               if (index === queueSize - 1) {
                  right = nodeId;
               }

               if (node.left) {
                  deq.pushBack([node.left, nodeId * 2n + 1n]);
               }
               if (node.right) {
                  deq.pushBack([node.right, nodeId * 2n + 2n]);
               }
            }

            //maxWidth = BigInt(Math.max(maxWidth, right - left + 1n));
            if (right - left + 1n > maxWidth) {
               maxWidth = right - left + 1n;
            }
         }
      }

      bfs(root)
      return Number(maxWidth)
   };
}


const widthOfBinaryTree = new Solution().widthOfBinaryTree;
console.log(new Solution().widthOfBinaryTree(buildTree([1])) === 1)
console.log(new Solution().widthOfBinaryTree(buildTree([1, 2, 3])) === 2)
console.log(new Solution().widthOfBinaryTree(buildTree([1, null, 3])) === 1)
console.log(new Solution().widthOfBinaryTree(buildTree([1, 2, null])) === 1)
console.log(new Solution().widthOfBinaryTree(buildTree([1, 3, 2, 5, 3, null, 9])) === 4)
console.log(new Solution().widthOfBinaryTree(buildTree([1, 3, 2, 5, null, null, 9, 6, null, 7])) === 7)
console.log(new Solution().widthOfBinaryTree(buildTree([1, 3, 2, 5])) === 2)
console.log(new Solution().widthOfBinaryTree(buildTree([1, 1, 1, 1, 1, 1, 1, null, null, null, 1, null, null, null, null, 2, 2, 2, 2, 2, 2, 2, null, 2, null, null, 2, null, 2])) === 8)
