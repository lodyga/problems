class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, recursion
    * @param {TreeNode} root
    * @return {boolean}
    */
   evaluateTree = (root) => {
      if (!root) return false
      else if (root.val === 0) {return false}
      else if (root.val === 1) {return true}
      else if (root.val === 2) {
         return (
            this.evaluateTree(root.left) ||
            this.evaluateTree(root.right))
      }
      else if (root.val === 3) {
         return (
            this.evaluateTree(root.left) &&
            this.evaluateTree(root.right))
      }
   };
}
const evaluateTree = new Solution().evaluateTree;


console.log(new Solution().evaluateTree(buildTree([0])), false)
console.log(new Solution().evaluateTree(buildTree([1])), true)
console.log(new Solution().evaluateTree(buildTree([2])), false)
console.log(new Solution().evaluateTree(buildTree([2, 1, 3, null, null, 0, 1])), true)