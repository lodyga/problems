class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, recursion
    * pure function
    * @param {TreeNode} root
    * @return {number[]}
    */
   goodNodes(root) {
      return dfs(root, root.val)

      function dfs(node, maxVal) {
         if (!node) 
            return 0

         maxVal = Math.max(maxVal, node.val);
         let goodNodesCount = node.val >= maxVal ? 1 : 0;
         goodNodesCount += dfs(node.left, maxVal);
         goodNodesCount += dfs(node.right, maxVal);
         return goodNodesCount
      }
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, recursion
    * side effect
    * @param {TreeNode} root
    * @return {number[]}
    */
   goodNodes(root) {
      let goodNodesCount = 0; 
      dfs(root, root.val)
      return goodNodesCount

      function dfs(node, maxVal) {
         if (!node) 
            return 

         maxVal = Math.max(maxVal, node.val);
         goodNodesCount += node.val >= maxVal ? 1 : 0;
         dfs(node.left, maxVal);
         dfs(node.right, maxVal);
      }
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, iteration, stack
    * @param {TreeNode} root
    * @return {number[]}
    */
   goodNodes(root) {
      let node = root;
      const stack = [[root, root.val]];
      let goodNodesCount = 0;

      while (stack.length) {
         const stackLength = stack.length;

         for (let index = 0; index < stackLength; index++) {
            let [node, maxValue] = stack.pop();
            maxValue = Math.max(maxValue, node.val);
            goodNodesCount += node.val >= maxValue ? 1 : 0;

            if (node.left) 
               stack.push([node.left, maxValue]);
            if (node.right) 
               stack.push([node.right, maxValue]);
         }
      }
      return goodNodesCount
   };
}
const goodNodes = new Solution().goodNodes;


console.log(new Solution().goodNodes(buildTree([1])) === 1)
console.log(new Solution().goodNodes(buildTree([1, 2, 3])) === 3)
console.log(new Solution().goodNodes(buildTree([3, 1, 4, 3, null, 1, 5])) === 4)
console.log(new Solution().goodNodes(buildTree([3, 3, null, 4, 2])) === 3)