/**
 * Time complexity: O(1)
 * Auxiliary space complexity: O(c)
 *     O(capacity)
 * Tags: hash map
 * @param {number} capacity
 */
class LRUCache {
   constructor(capacity) {
      this.capacity = capacity;
      this.cache = new Map();
   };

   /**
    * @param {number} key
    * @return {number}
    */
   get(key) {
      if (!this.cache.has(key)) return -1
      const value = this.cache.get(key);
      this.cache.delete(key);
      this.cache.set(key, value);
      return value
   };

   /**
    * @param {number} key
    * @param {number} value
    * @return {void}
    */
   put(key, value) {
      if (this.cache.has(key)) {
         this.cache.delete(key);
      } else if (this.cache.size === this.capacity) {
         const lruKey = this.cache.keys().next().value;
         this.cache.delete(lruKey);
      }

      this.cache.set(key, value);
   };
}


class ListNode {
   constructor(key = null, val = null, next = null, prev = null) {
      this.key = key;
      this.val = val;
      this.next = next;
      this.prev = prev;
   }
}


/**
 * Time complexity: O(1)
 * Auxiliary space complexity: O(c)
 *     O(capacity)
 * Tags: linked list
 * @param {number} capacity
 */
class LRUCache {
   constructor(capacity) {
      this.capacity = capacity;
      this.cache = new Map();
      this.first = new ListNode();
      this.last = new ListNode();
      this.first.next = this.last;
      this.last.prev = this.first;
   };

   /**
    * @param {number} key
    * @return {number}
    */
   get(key) {
      if (!this.cache.has(key)) {
         return -1
      }
      const node = this.cache.get(key);
      this.popNode(node);
      this.pushNode(node);
      return node.val
   };

   /**
    * @param {number} key
    * @param {number} val
    * @return {void}
    */
   put(key, val) {
      if (this.cache.has(key)) {
         const node = this.cache.get(key);
         this.popNode(node);
      } else if (this.cache.size === this.capacity) {
         const lru = this.first.next;
         this.cache.delete(lru.key);
         this.popNode(lru);
      }

      const node = new ListNode(key, val);
      this.pushNode(node);
      this.cache.set(key, node);
   };

   pushNode(node) {
      const next = this.last;
      const prev = next.prev;
      node.next = next;
      node.prev = prev;
      next.prev = node;
      prev.next = node;
   };

   popNode(node) {
      [node.next.prev, node.prev.next] = [node.prev, node.next];
   };
}


const lRUCache1 = new LRUCache(2)
lRUCache1.put(1, 1)  // cache is {1=1}
lRUCache1.put(2, 2)  // cache is {1=1, 2=2}
console.log(lRUCache1.get(1))  // return 1
lRUCache1.put(3, 3)  // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
console.log(lRUCache1.get(2))  // returns -1 (not found)
lRUCache1.put(4, 4)  // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
console.log(lRUCache1.get(1))  // return -1 (not found)
console.log(lRUCache1.get(3))  // return 3
console.log(lRUCache1.get(4))  // return 4

const lRUCache2 = new LRUCache(2)
console.log(lRUCache2.get(2))  // return -1
lRUCache2.put(2, 6)
console.log(lRUCache2.get(1))  // return -1
lRUCache2.put(1, 5)
lRUCache2.put(1, 2)
console.log(lRUCache2.get(1))  // return 2
console.log(lRUCache2.get(2))  // return 6

const lRUCache3 = new LRUCache(2)
lRUCache3.put(2, 1)
lRUCache3.put(1, 1)
lRUCache3.put(2, 3)
lRUCache3.put(4, 1)
console.log(lRUCache3.get(1))  // return -1
console.log(lRUCache3.get(2))  // return 3