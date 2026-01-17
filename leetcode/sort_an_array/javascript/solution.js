import { MinPriorityQueue } from '@datastructures-js/priority-queue';

class Solution {
  /**
   * Time complexity: O(nlogn)
   * Auxiliary space complexity: O(n)
   * Tags:
   *     A: sorting, build-in function, in-place method
   * @param {number[]} nums
   * @return {number[]}
   */
  sortArray(nums) {
    return nums.sort((a, b) => a - b);
  };

  /**
   * Time complexity: O(nlogn)
   * Auxiliary space complexity: O(n)
   * Tags:
   *     DS: heap
   *     A: heap, sorting
   * @param {number[]} nums
   * @return {number[]}
   */
  sortArray(nums) {
    const numberHeap = new MinPriorityQueue();
    nums.forEach(num => numberHeap.enqueue(num));
    const sortedNums = [];
    while (numberHeap.size()) {
      sortedNums.push(numberHeap.dequeue());
    }
    return sortedNums
  };

  /**
   * Time complexity: O(nlogn)
   * Auxiliary space complexity: O(n)
   * Tags:
   *     DS: list
   *     A: merge sort, sorting
   * @param {number[]} nums
   * @return {number[]}
   */
  sortArray(nums) {
    const mergeSort = (left, right) => {
      if (left === right) {
        return
      }
      divide(left, right);
      merge(left, right);
    };

    const divide = (left, right) => {
      const middle = (left + right) >> 1;
      mergeSort(left, middle);
      mergeSort(middle + 1, right);
    };

    const merge = (left, right) => {
      const middle = (left + right) >> 1;
      const leftChunk = nums.slice(left, middle + 1);
      const rightChunk = nums.slice(middle + 1, right + 1);
      let index = left;
      left = 0;
      right = 0;

      while (
        left < leftChunk.length &&
        right < rightChunk.length
      ) {
        if (leftChunk[left] <= rightChunk[right]) {
          nums[index] = leftChunk[left];
          left++;
        } else {
          nums[index] = rightChunk[right];
          right++;
        }
        index++;
      }
      while (left < leftChunk.length) {
        nums[index] = leftChunk[left];
        left++;
        index++;
      }
      while (right < rightChunk.length) {
        nums[index] == rightChunk[right];
        right++;
        index++;
      }
    };

    mergeSort(0, nums.length - 1);
    return nums
  };

  /**
   * Time complexity: O(n2)
   *     avg case: O(nlogn)
   *     worst case: O(n2)
   * Auxiliary space complexity: O(n)
   * Tags:
   *     A: quick sort, sorting, in-place method
   * @param {number[]} nums
   * @return {number[]}
   */
  sortArray(nums) {
    const quickSort = (left, right) => {
      if (left >= right) {
        return
      }
      const pivot = partition(left, right)
      quickSort(left, pivot - 1);
      quickSort(pivot + 1, right);
    };

    const partition = (left, end) => {
      const pivot = nums[end];
      for (let right = left; right < end; right++) {
        if (nums[right] < pivot) {
          swapNums(left, right);
          left++;
        }
      }
      swapNums(left, end);
      return left
    };

    const swapNums = (left, right) => {
      [nums[left], nums[right]] = [nums[right], nums[left]];
    };

    quickSort(0, nums.length - 1);
    return nums
  };

  /**
   * Time complexity: O(n2)
   * Auxiliary space complexity: O(1)
   * Tags:
   *     A: insertion sort, sorting
   * @param {number[]} nums
   * @return {number[]}
   */
  sortArray(nums) {
    const insertionSort = () => {
      for (let right = 1; right < nums.length; right++) {
        const key = nums[right];
        let left = right - 1;

        while (
          left > -1 &&
          nums[left] > key
        ) {
          nums[left + 1] = nums[left];
          left--;
        }
        nums[left + 1] = key;
      }
    }
    insertionSort();
    return nums
  };

  /**
   * Time complexity: O(n2)
   * Auxiliary space complexity: O(1)
   * Tags:
   *     A: bubble sort, sorting, in-place method
   * @param {number[]} nums
   * @return {number[]}
   */
  sortArray(nums) {
    const bubbleSort = () => {
      for (let left = 0; left < nums.length; left++) {
        for (let right = left + 1; right < nums.length; right++) {
          if (nums[right] < nums[left]) {
            [nums[left], nums[right]] = [nums[right], nums[left]];
          }
        }
      }
    }
    bubbleSort();
    return nums
  };
}


const sortArray = new Solution().sortArray;
console.log(new Solution().sortArray([4]).toString() === [4].toString())
console.log(new Solution().sortArray([5, 4]).toString() === [4, 5].toString())
console.log(new Solution().sortArray([5, 2, 3, 1]).toString() === [1, 2, 3, 5].toString())
console.log(new Solution().sortArray([5, 1, 1, 2, 0, 0]).toString() === [0, 0, 1, 1, 2, 5].toString())
console.log(new Solution().sortArray([-2, 3, -5]).toString() === [-5, -2, 3].toString())
