class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, recursion
    * @param {TreeNode} root
    * @return {number}
    */
   diameterOfBinaryTree(root) {
      let diameter = 0;

      const dfs = (node) => {
         if (!node) {
            return 0
         }
         const leftPath = dfs(node.left);
         const rightPath = dfs(node.right);
         diameter = Math.max(diameter, leftPath + rightPath);

         return 1 + Math.max(leftPath, rightPath)
      }

      dfs(root);
      return diameter
   };
}


console.log(new Solution().diameterOfBinaryTree(buildTree([])), 0)
console.log(new Solution().diameterOfBinaryTree(buildTree([5])), 0)
console.log(new Solution().diameterOfBinaryTree(buildTree([1, 2])), 1)
console.log(new Solution().diameterOfBinaryTree(buildTree([1, 2, 3])), 2)
console.log(new Solution().diameterOfBinaryTree(buildTree([1, 2, 3, 4, 5])), 3)