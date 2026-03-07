import { MaxPriorityQueue } from "@datastructures-js/priority-queue";


class Solution {   
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: heap, list
    *     A: greedy
    * @param {number[]} nums
    * @return {number}
    */
   maxSumDivThree(nums) {
      const total = nums.reduce((sum, num) => sum + num, 0);

      if (total % 3 === 0) {
         return total
      }

      const remainder = total % 3;
      const one = new MaxPriorityQueue();
      const two = new MaxPriorityQueue();
      let res = 0;

      for (const num of nums) {
         if (num % 3 === 1) {
            one.enqueue(num);

            if (one.size() > 2) {
               one.dequeue();
            }
         } else if (num % 3 === 2) {
            two.enqueue(num);

            if (two.size() > 2) {
               two.dequeue();
            }
         }
      };

      if (remainder === 1) {
         if (one.size()) {
            res = total - one.back();
         }
         if (two.size() > 1) {
            res = Math.max(res, total - two.front() - two.back());
         }
      } else if (remainder === 2) {
         if (two.size()) {
            res = total - two.back();
         }
         if (one.size() > 1) {
            res = Math.max(res, total - one.front() - one.back());
         }
      }

      return res
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: heap, list
    *     A: greedy
    * @param {number[]} nums
    * @return {number}
    */
   maxSumDivThree(nums) {
      const total = nums.reduce((sum, num) => sum + num, 0);

      if (total % 3 === 0) {
         return total
      }

      const remainder = total % 3;
      let one = new MaxPriorityQueue();
      let two = new MaxPriorityQueue();
      let res = 0;

      for (const num of nums) {
         if (num % 3 === 1) {
            one.enqueue(num);

            if (one.size() > 2) {
               one.dequeue();
            }
         } else if (num % 3 === 2) {
            two.enqueue(num);

            if (two.size() > 2) {
               two.dequeue();
            }
         }
      };

      one = one.toArray().sort((a, b) => a - b);
      two = two.toArray().sort((a, b) => a - b);


      if (remainder === 1) {
         if (one.length) {
            res = total - one[0];
         }
         if (two.length > 1) {
            res = Math.max(res, total - two[0] - two[1]);
         }
      } else if (remainder === 2) {
         if (two.length) {
            res = total - two[0];
         }
         if (one.length > 1) {
            res = Math.max(res, total - one[0] - one[1]);
         }
      }

      return res
   };

   /**
    * Time complexity: O(2^n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: brute-force
    * @param {number[]} nums
    * @return {number}
    */
   maxSumDivThree(nums) {
      const dfs = (index, total) => {
         if (index === nums.length)
            return total % 3 === 0 ? total : 0

         const num = nums[index];
         const skip = dfs(index + 1, total);
         const take = dfs(index + 1, total + num);
         return Math.max(skip, take)
      }
      return dfs(0, 0)
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: bottom-up
    * @param {number[]} nums
    * @return {number}
    */
   maxSumDivThree(nums) {
      // Max subsequence sum divided by 3 with rest 0, 1, 2 respectively.
      const cache = [0, 0, 0];

      for (const num of nums) {
         for (const c of cache.slice()) {
            const mod = (c + num) % 3;
            cache[mod] = Math.max(cache[mod], c + num)
         }
      }
      return cache[0]
   };

}


const maxSumDivThree = new Solution().maxSumDivThree;
console.log(new Solution().maxSumDivThree([3]) === 3)
console.log(new Solution().maxSumDivThree([4]) === 0)
console.log(new Solution().maxSumDivThree([3, 6, 5, 1, 8]) === 18)
console.log(new Solution().maxSumDivThree([4]) === 0)
console.log(new Solution().maxSumDivThree([1, 2, 3, 4, 4]) === 12)
console.log(new Solution().maxSumDivThree([366, 809, 6, 792, 822, 181, 210, 588, 344, 618, 341, 410, 121, 864, 191, 749, 637, 169, 123, 472, 358, 908, 235, 914, 322, 946, 738, 754, 908, 272, 267, 326, 587, 267, 803, 281, 586, 707, 94, 627, 724, 469, 568, 57, 103, 984, 787, 552, 14, 545, 866, 494, 263, 157, 479, 823, 835, 100, 495, 773, 729, 921, 348, 871, 91, 386, 183, 979, 716, 806, 639, 290, 612, 322, 289, 910, 484, 300, 195, 546, 499, 213, 8, 623, 490, 473, 603, 721, 793, 418, 551, 331, 598, 670, 960, 483, 154, 317, 834, 352]) === 50487)
console.log(new Solution().maxSumDivThree([456, 963, 755, 656, 119, 682, 660, 305, 115, 594, 786, 646, 153, 869, 889, 56, 531, 536, 974, 667, 777, 881, 301, 54, 358, 447, 830, 585, 992, 819, 725, 66, 147, 598, 655, 771, 516, 978, 806, 768, 865, 617, 259, 486, 478, 434, 650, 430, 701, 72, 118, 194, 902, 636, 187, 919, 640, 87, 383, 787, 815, 864, 191, 769, 125, 406, 228, 171, 451, 641, 955, 197, 980, 475, 503, 600, 81, 87, 921, 862, 581, 623, 561, 429, 130, 91, 753, 480, 329, 734, 533, 181, 851, 908, 442, 133, 944, 449, 85, 560]) === 53394)
console.log(new Solution().maxSumDivThree([2, 6, 2, 2, 7]) === 15)
