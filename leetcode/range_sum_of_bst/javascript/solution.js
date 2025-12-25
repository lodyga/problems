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
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: binary tree
    *     A: dfs, recursion, pre-order traversal
    * @param {TreeNode} root
    * @param {number} low
    * @param {number} high
    * @return {number}
    */
   rangeSumBST(root, low, high) {
      const dfs = (node) => {
         if (node === null) {
            return 0
         }
         let total = 0;
         if (
            low <= node.val &&
            node.val <= high
         ) total += node.val;
         if (low < node.val)
            total += dfs(node.left)
         if (high > node.val)
            total += dfs(node.right)
         return total
      }
      return dfs(root);
   };
}


const rangeSumBST = new Solution().rangeSumBST;
console.log(new Solution().rangeSumBST(buildTree([10, 5, 15, 3, 7, null, 18]), 7, 15) === 32)
console.log(new Solution().rangeSumBST(buildTree([10, 5, 15, 3, 7, 13, 18, 1, null, 6]), 6, 10) === 23)
console.log(new Solution().rangeSumBST(buildTree([182, 107, 257, 68, 146, 221, 296, 50, 89, 128, 164, 203, 239, 278, 314, 41, 59, 80, 98, 119, 137, 155, 173, 194, 212, 230, 248, 269, 287, 305, 323, 35, 47, 56, 65, 74, 86, 95, 104, 113, 125, 134, 143, 152, 161, 170, 179, 188, 200, 209, 218, 227, 236, 245, 254, 263, 275, 284, 293, 302, 311, 320, 329, 32, 38, 44, null, 53, null, 62, null, 71, 77, 83, null, 92, null, 101, null, 110, 116, 122, null, 131, null, 140, null, 149, null, 158, null, 167, null, 176, null, 185, 191, 197, null, 206, null, 215, null, 224, null, 233, null, 242, null, 251, null, 260, 266, 272, null, 281, null, 290, null, 299, null, 308, null, 317, null, 326]), 86, 224) === 7285)
