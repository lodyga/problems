class MyDoublyLinkedNode {
   constructor(key = -1, val = -1, next = null, prev = null) {
      this.key = key;
      this.val = val;
      this.next = next;
      this.prev = prev;
   }
}


class MyDoublyLinkedList {
   constructor(nodes = []) {
      this.size = 0;
      this.first = new MyDoublyLinkedNode();
      this.last = new MyDoublyLinkedNode(-1, -1, null, this.first);
      this.first.next = this.last;

      if (nodes) {
         for (const node of nodes) {
            this.push(node);
         }
      }
   }

   push(node) {
      const right = this.last;
      const left = right.prev;

      node.next = right;
      node.prev = left;

      left.next = node;
      right.prev = node;

      this.size++;
   }

   pop() {
      if (this.size === 0) {
         return;
      }

      const node = this.last.prev;
      this.delete(node);
   }

   popLeft() {
      if (this.size === 0) {
         return;
      }

      const node = this.first.next;
      this.delete(node);
   }

   delete(node) {
      node.next.prev = node.prev;
      node.prev.next = node.next;
      this.size--;
   }

   front() {
      return this.size > 0 ? this.first.next : null;
   }
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
      this.size = 0;
      this.minFreq = 0;

      this.nodes = new Map();  // { key: MyDoublyLinkedNode(key, val, next, prev), }
      this.freqs = new Map();  // { key: frequency, }
      this.freqBuckets = new Map();  // {frequency: MyDoublyLinkedList(MyDoublyLinkedNode(), ), }
   }

   _updateBucket(node, freq) {
      if (!this.freqBuckets.has(freq)) {
         this.freqBuckets.set(freq, new MyDoublyLinkedList([node]));
      }
      else {
         this.freqBuckets.get(freq).push(node);
      }
   }

   _insert(key, val) {
      this.freqs.set(key, 1);
      const node = new MyDoublyLinkedNode(key, val);
      this.nodes.set(key, node);

      this._updateBucket(node, 1)
      this.minFreq = 1;
   }

   _update(key, val) {
      const freq = this.freqs.get(key);
      const node = this.nodes.get(key);
      node.val = val;
      const bucket = this.freqBuckets.get(freq);
      bucket.delete(node);

      if (
         freq === this.minFreq
         && bucket.size === 0
      ) {
         this.minFreq++;
      }

      this.freqs.set(key, freq + 1);
      this._updateBucket(node, freq + 1)
   }

   _popLru() {
      const lfuBucket = this.freqBuckets.get(this.minFreq);
      const lfuKey = lfuBucket.front().key;
      this.nodes.delete(lfuKey);
      this.freqs.delete(lfuKey);
      lfuBucket.popLeft();

      if (lfuBucket.size === 0) {
         this.freqBuckets.delete(this.minFreq);
      }
   }

   get(key) {
      if (!this.nodes.has(key)) {
         return -1;
      }

      const val = this.nodes.get(key).val;
      this._update(key, val);

      return val;
   }

   put(key, val) {
      // Update existing key.
      if (this.nodes.has(key)) {
         this._update(key, val);
      }
      // Capacity reached -> pop LFU key.
      else if (this.size === this.cap) {
         this._popLru();
         this._insert(key, val);
      }
      // Insert a new key.
      else {
         this._insert(key, val);
         this.size++;
      }
   }
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
