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
    * Time complexity: O(n*d2)
    *     n: node count
    *     d: distance
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: binary tree
    *     A: dfs, recursion, post-order traversal
    * @param {TreeNode} root
    * @param {number} distance
    * @return {number}
    */
   countPairs(root, distance) {
      let counter = 0;

      const dfs = (node) => {
         if (node === null) {
            return []
         } else if (
            node.left === null &&
            node.right === null
         ) {
            return [1]
         }

         const left = dfs(node.left);
         const right = dfs(node.right);

         for (const l of left) {
            for (const r of right) {
               if (l + r <= distance) {
                  counter++;
               }
            }
         }

         return [...left, ...right].
            filter(val => val + 2 <= distance).
            map(val => val + 1);
      }

      dfs(root)
      return counter
   };
}


const countPairs = new Solution().countPairs;
console.log(new Solution().countPairs(buildTree([1]), 1) === 0)
console.log(new Solution().countPairs(buildTree([1, 2, 3]), 2) === 1)
console.log(new Solution().countPairs(buildTree([1, 2]), 1) === 0)
console.log(new Solution().countPairs(buildTree([1, 2, 3, null, 4]), 3) === 1)
console.log(new Solution().countPairs(buildTree([1, 2, 3, 4, 5, 6, 7]), 3) === 2)
console.log(new Solution().countPairs(buildTree([7, 1, 4, 6, null, 5, 3, null, null, null, null, null, 2]), 3) === 1)
