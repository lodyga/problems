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
    * Time complexity: O(2^n)
    * Auxiliary space complexity: O(2^n)
    * Tags:
    *     DS: binray tree, list
    *     A: backtracking with memo
    * @param {number} n
    * @return {TreeNode[]}
    */
   allPossibleFBT(n) {
      const memo = new Map([[0, []], [1, [new TreeNode(0)]]]);

      const backtrack = (n) => {
         if (memo.has(n))
            return memo.get(n)

         const res = [];

         for (let left = 0; left < n; left++) {
            const right = n - 1 - left;
            const leftTrees = backtrack(left);
            const rightTrees = backtrack(right);

            for (const leftTree of leftTrees)
               for (const rightTree of rightTrees)
                  res.push(new TreeNode(0, leftTree, rightTree));

         }
         memo.set(n, res);
         return res
      }

      return backtrack(n)
   };
}


const allPossibleFBT = new Solution().allPossibleFBT;
console.log(new Solution().allPossibleFBT(1))
console.log(new Solution().allPossibleFBT(3))
console.log(new Solution().allPossibleFBT(7))
