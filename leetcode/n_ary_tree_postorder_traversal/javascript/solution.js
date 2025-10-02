/**
 * // Definition for a _Node.
 * function _Node(val,children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */


/**
 * Time complexity: O(n)
 * Auxiliary space complexity: O(n)
 * Tags: binary tree, dfs, recursion, post-order traversal
 * @param {_Node|null} root
 * @return {number[]}
 */
var postorder = function (root) {
   const values = [];
   const dfs = (node) => {
      if (!node)
         return

      for (const child of node.children)
         dfs(child);

      values.push(node.val);
   }
   dfs(root)
   return values
};


/**
 * Time complexity: O(n)
 * Auxiliary space complexity: O(n)
 * Tags: binary tree, dfs, iteration, post-order traversal
 * @param {_Node|null} root
 * @return {number[]}
 */
var postorder = function (root) {
   if (!root)
      return []
   const values = [];
   const stack = [[root, false]];

   while (stack.length) {
      const [node, visited] = stack.pop();

      if (visited) {
         values.push(node.val);
      } else {
         stack.append([node, true]);
         for (let index = node.children.length - 1; index > -1; index--) {
            const child = node.children[index];
            stack.push([child, false]);
         }
      }
   }
   return values
};