class DoublyLinkedNode {
   constructor(val = null, next = null, prev = null) {
      // Val stores a key.
      this.val = val
      this.next = next
      this.prev = prev
   };
}

class DoublyLinkedList {
   constructor() {
      this.left = new DoublyLinkedNode()
      this.right = new DoublyLinkedNode(null, null, this.left)
      this.left.next = this.right
      this.len = 0
   };

   push(node) {
      const right = this.right;
      const left = right.prev;

      node.next = right;
      node.prev = left;

      left.next = right.prev = node;
      this.len += 1;
   };

   pop() {
      const node = this.right.prev;
      this.delete(node);
   };

   popLeft() {
      const node = this.left.next;
      this.delete(node);
   };

   delete(node) {
      [node.next.prev, node.prev.next] = [node.prev, node.next];
      this.len--;
   };

   peak() {
      return this.len > 0 ? this.left.next : null
   };
}

class LFUCache {
   /**
    * Time complexity: O(1)
    * Auxiliary space complexity: O(c)
    *     O(capacity)
    * Tags:
    *     DS: doubly linked list, hash map
    * @param {}
    * @return {}
    */
   constructor(cap) {
      this.cap = cap;
      this.nodes = new Map();  // { key: Node(val, next, prev) }
      this.vals = new Map();  // { key: val }
      this.freqs = new Map();  // { key: frequency }
      this.freqBuckets = new Map();  // {frequency: DoublyLinkedList(DoblyListNode(), ), }
      this.minFreq = 0;
   };

   _insert(key, val) {
      this.vals.set(key, val);
      this.freqs.set(key, 1);
      const node = new DoublyLinkedNode(key);
      this.nodes.set(key, node);
      if (!this.freqBuckets.has(1)) {
         this.freqBuckets.set(1, new DoublyLinkedList())
      }
      this.freqBuckets.get(1).push(node);
      this.minFreq = 1;
   };

   _update(key, val) {
      this.vals.set(key, val);

      const freq = this.freqs.get(key);
      const node = this.nodes.get(key);
      const bucket = this.freqBuckets.get(freq);

      bucket.delete(node);

      if (
         freq == this.minFreq &&
         bucket.len === 0
      ) {
         this.minFreq++;
      }

      this.freqs.set(key, freq + 1);

      if (!this.freqBuckets.has(freq + 1)) {
         this.freqBuckets.set(freq + 1, new DoublyLinkedList());
      }
      this.freqBuckets.get(freq + 1).push(node);
   };

   _popLru() {
      const lfuBucket = this.freqBuckets.get(this.minFreq);
      const lfuKey = lfuBucket.peak().val
      this.vals.delete(lfuKey);
      this.nodes.delete(lfuKey);
      this.freqs.delete(lfuKey);
      lfuBucket.popLeft();

      if (lfuBucket.len === 0) {
         this.freqBuckets.delete(this.minFreq);
      }
   };

   get(key) {
      if (!this.vals.has(key))
         return -1
      this._update(key, this.vals.get(key));
      return this.vals.get(key)
   };

   put(key, val) {
      // Update existing key.
      if (this.nodes.has(key))
         this._update(key, val);

      // Capacity reached -> pop LFU key.
      else if (this.cap === 0) {
         this._popLru();
         this._insert(key, val);
      }
      // Insert a new key.
      else {
         this._insert(key, val);
         this.cap--;
      }
   };
}


const lfu = new LFUCache(2);
lfu.put(1, 1);  // cache=[1,_], cnt(1)=1
lfu.put(2, 2);  // cache=[2,1], cnt(2)=1, cnt(1)=1
console.log(lfu.get(1) === 1);
// return 1
// cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);
// 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
// cache=[3,1], cnt(3)=1, cnt(1)=2
console.log(lfu.get(2) === -1);
console.log(lfu.get(3) === 3);
// cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);
// Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
// cache=[4,3], cnt(4)=1, cnt(3)=2
console.log(lfu.get(1) === - 1);
console.log(lfu.get(3) === 3);
// cache=[3,4], cnt(4)=1, cnt(3)=3
console.log(lfu.get(4) === 4);
// cache=[4,3], cnt(4)=2, cnt(3)=3
