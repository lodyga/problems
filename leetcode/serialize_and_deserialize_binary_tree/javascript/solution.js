import { TreeNode, buildTree, getTreeValues } from '../../../../JS/binary-tree.js';
import { Queue } from '@datastructures-js/queue';


/**
 * class TreeNode {
 *    constructor(val = null, left = null, right = null) {
 *       this.val = val
 *       this.left = left
 *       this.right = right
 *    };
 * }
 */


/**
 * Time complexity: O(n)
 * Auxiliary space complexity: O(n)
 * Tags:
 *     DS: binary tree, queue
 *     A: bfs, iteration, level-order traversal
 */
class Codec {
   /**
    * @param {TreeNode} root
    * @returns {string}
    */
   serialize(root) {
      if (root === null) {
         return '';
      }

      const res = [];
      const queue = new Queue([root]);

      while (!queue.isEmpty()) {
         const node = queue.pop();

         if (node) {
            res.push(node.val.toString());
            queue.push(node.left);
            queue.push(node.right);
         }
         else {
            res.push('null');
         }
      }

      while (res && res[res.length - 1] === 'null') {
         res.pop();
      }

      return res.join(',');
   };

   /**
    * @param {string} data
    * @returns {TreeNode}
    */
   deserialize(data) {
      if (data === '') {
         return null;
      }

      const nodes = data.split(',');
      const root = new TreeNode(Number(nodes[0]));
      const queue = new Queue([root]);
      let idx = 1;

      while (idx < nodes.length) {
         const node = queue.pop();

         let val = nodes[idx];

         if (val !== "null") {
            node.left = new TreeNode(Number(val));
            queue.push(node.left);
         }

         idx++;

         if (idx === nodes.length) {
            break;
         }

         val = nodes[idx];

         if (val !== "null") {
            node.right = new TreeNode(Number(val));
            queue.push(node.right);
         }

         idx++;
      }

      return root;
   }
}


/**
 * Time complexity: O(n)
 * Auxiliary space complexity: O(n)
 * Tags: binary tree, dfs, recursion, pre-order traversal
 */
class Codec {
   /**
    * @param {TreeNode} root
    * @returns {string}
    */
   serialize(root) {
      const dfs = (node) => {
         if (node === null) {
            vals.push("null")
            return;
         }

         vals.push((node.val).toString());
         dfs(node.left);
         dfs(node.right);
      };

      const vals = [];
      dfs(root);
      return vals.join(',')
   }

   /**
    * @param {string} data
    * @returns {TreeNode}
    */
   deserialize(data) {
      let vals = data.split(',');
      let idx = 0;

      const dfs = () => {
         if (vals[idx] === 'null') {
            idx++;
            return null;
         }

         const node = new TreeNode(parseInt(vals[idx]));
         idx++;
         node.left = dfs();
         node.right = dfs();
         return node;
      };

      return dfs();
   }
}


console.log(getTreeValues(new Codec().deserialize(new Codec().serialize(buildTree([4])))).toString() === [4].toString())
console.log(getTreeValues(new Codec().deserialize(new Codec().serialize(buildTree([4, 5, 6])))).toString() === [4, 5, 6].toString())
console.log(getTreeValues(new Codec().deserialize(new Codec().serialize(buildTree([4, 5])))).toString() === [4, 5].toString())
console.log(getTreeValues(new Codec().deserialize(new Codec().serialize(buildTree([4, null, 6])))).toString() === [4, null, 6].toString())
console.log(getTreeValues(new Codec().deserialize(new Codec().serialize(buildTree([])))).toString() === [].toString())
console.log(getTreeValues(new Codec().deserialize(new Codec().serialize(buildTree([1, 2, 3, null, null, 4, 5])))).toString() === [1, 2, 3, null, null, 4, 5].toString())
console.log(getTreeValues(new Codec().deserialize(new Codec().serialize(buildTree([1, 2, 3, null, null, 4, 5, 6, 7])))).toString() === [1, 2, 3, null, null, 4, 5, 6, 7].toString())
